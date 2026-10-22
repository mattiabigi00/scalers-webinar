#!/usr/bin/env python3
"""File dell'artifact Slides -> DECK testo (.md), con controllo H3.

Uso:
  python3 export_deck.py <cartella che contiene project/> [--url <link artifact>] [--versione <id>]
                          [--out DECK_<P>_testo.md] [--check-h3]

<cartella> è quella in cui l'Artifact tool ha salvato i file letti (project/deck.json e project/slides/*.html).
--check-h3: per ogni slide conta i blocchi di testo (titoli h1-h3, corpi p/ul/ol fuori da svg, table e aside).
            Più di un titolo o più di un corpo = possibile violazione H3 ⛔. Esce con codice 1 se ne trova.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deckfmt  # noqa: E402

VOID = {"br", "img", "hr", "x-icon", "x-shape", "x-connector"}


class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.title: list[str] = []
        self.body: list[str] = []
        self.notes: list[str] = []
        self.images: list[str] = []
        self.n_titles = 0
        self.n_bodies = 0
        self.cur: list[str] | None = None
        self.cur_kind = ""
        self.hl = 0

    def _in(self, *tags):
        return any(t in self.stack for t in tags)

    def handle_starttag(self, tag, attrs):
        at = dict(attrs)
        if tag == "img":
            if at.get("alt"):
                self.images.append("alt: " + at["alt"])
            return
        if tag == "svg" and at.get("aria-label"):
            self.images.append("svg: " + at["aria-label"])
        if tag in VOID:
            if tag == "br" and self.cur is not None:
                self.cur.append("\n")
            return
        self.stack.append(tag)
        if self._in("aside"):
            return
        if tag in ("h1", "h2", "h3") and not self._in("svg", "table") and self.cur is None:
            self.n_titles += 1
            self.cur = []
            self.cur_kind = "title" if self.n_titles == 1 else "body"
        elif tag in ("p", "ul", "ol") and not self._in("svg", "table") and self.cur is None:
            self.n_bodies += 1
            self.cur, self.cur_kind = [], "body"
        elif tag == "li" and self.cur is not None:
            self.cur.append("\n• ")
        elif tag == "b" and self.cur is not None:
            self.cur.append("**")
        elif tag == "i" and self.cur is not None:
            self.cur.append("*")
        elif tag == "span" and self.cur is not None and self.cur_kind == "title" and "color" in (at.get("style") or ""):
            self.cur.append("==")
            self.hl += 1

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag == "b" and self.cur is not None:
            self.cur.append("**")
        if tag == "i" and self.cur is not None:
            self.cur.append("*")
        if tag == "span" and self.cur is not None and self.cur_kind == "title" and self.hl:
            self.cur.append("==")
            self.hl -= 1
        if tag in ("h1", "h2", "h3", "p", "ul", "ol") and self.cur is not None and self.stack and self.stack[-1] == tag:
            text = "".join(self.cur).strip()
            if self.cur_kind == "title":
                self.title.append(text.replace("\n", " "))
            else:
                self.body.append(text)
            self.cur, self.cur_kind = None, ""
        while self.stack:
            t = self.stack.pop()
            if t == tag:
                break

    def handle_data(self, data):
        if self._in("aside"):
            self.notes.append(data)
            return
        if self.cur is not None:
            self.cur.append(re.sub(r"\s+", " ", data))


def clean_body(parts: list[str]) -> str:
    out = []
    for p in parts:
        p = re.sub(r"[ \t]*\n[ \t]*", "\n", p).strip()
        p = re.sub(r"\n{2,}", "\n\n", p)
        p = p.replace("****", "")
        out.append(p)
    return "\n\n".join(x for x in out if x)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--url", default="")
    ap.add_argument("--versione", default="-")
    ap.add_argument("--out")
    ap.add_argument("--check-h3", action="store_true")
    a = ap.parse_args()
    proj = Path(a.root)
    if (proj / "project").is_dir():
        proj = proj / "project"
    idx = json.loads((proj / "deck.json").read_text(encoding="utf-8"))
    order = list(idx.get("order", []))
    files = sorted((proj / "slides").glob("*.html"))
    order += [f.stem for f in files if f.stem not in order]
    starts = {v.get("start"): v.get("description", "") for v in (idx.get("sections") or {}).values()}
    deck = deckfmt.Deck(title=f"{idx.get('title', 'Webinar')} · export testo",
                        source=f"Fonte: {a.url or 'artifact'} · versione {a.versione} · estratto il {dt.date.today().isoformat()} · 0 slide")
    viol = []
    block = ""
    for pos, sid in enumerate(order, start=1):
        f = proj / "slides" / f"{sid}.html"
        if not f.exists():
            continue
        if sid in starts:
            block = starts[sid]
        sp = SlideParser()
        sp.feed(f.read_text(encoding="utf-8"))
        title = sp.title[0] if sp.title else ""
        raw_notes = "".join(sp.notes)
        layout, imgs, keep = "", list(sp.images), []
        for nl in raw_notes.splitlines():
            m = re.match(r"\s*LAYOUT:\s*([a-z]+)\s*$", nl)
            if m:
                layout = m.group(1)
                continue
            m = re.match(r"\s*IMMAGINI PER LA GRAFICA:\s*(.+)$", nl)
            if m:
                imgs.insert(0, m.group(1).strip())
                continue
            keep.append(nl)
        s = deckfmt.Slide(pos=pos, id=sid, title=title, block=block, body=clean_body(sp.body), layout=layout,
                          images=" | ".join(x for x in imgs if x), notes=" ".join(" ".join(keep).split()))
        deck.slides.append(s)
        if sp.n_titles > 1 or sp.n_bodies > 1:
            viol.append((pos, sid, title, sp.n_titles, sp.n_bodies))
    text = deckfmt.render(deck)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"OK · {len(deck.slides)} slide · {a.out}")
    else:
        sys.stdout.write(text)
    if a.check_h3:
        print(f"\nControllo H3 ⛔ · {len(viol)} slide con più blocchi di testo", file=sys.stderr)
        for pos, sid, t, nt, nb in viol:
            print(f"- {pos} · {sid} · {t[:60]} · titoli {nt} · corpi {nb}", file=sys.stderr)
        return 1 if viol else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
