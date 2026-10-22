#!/usr/bin/env python3
"""DECK testo (.md) -> file dell'artifact Slides (giro 1: bianco e nero).

Uso:
  python3 build_deck.py DECK_<P>_testo.md --out <cartella>/deck [--update <deck.json esistente>]

Scrive <out>/project/deck.json e <out>/project/slides/<id>.html.
Ogni slide ha UN <h2> (titolo) e UN <p> (corpo): regola H3 garantita per costruzione.
Le immagini e la regia vanno nelle note (<aside>), mai a schermo (H10, I1).
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deckfmt  # noqa: E402

BG = "#FAFAF7"
INK = "#1A1A1A"
MUTED = "#5A5F66"
ACCENT = "#1F6FEB"
FONT = "Poppins, Arial, sans-serif"
FACES = {"poppins": {"family": "Poppins", "href": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap"}}
ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)([^*\n]+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"==(.+?)==", rf'<span style="color:{ACCENT}">\1</span>', t)
    return t


def body_html(body: str) -> str:
    paras = [p for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    return "<br><br>".join("<br>".join(inline(l.strip()) for l in p.splitlines() if l.strip()) for p in paras)


def body_size(words: int) -> int:
    if words <= 60:
        return 40
    if words <= 110:
        return 34
    if words <= 160:
        return 30
    return 26


def notes_text(s: deckfmt.Slide) -> str:
    parts = []
    if s.layout:
        parts.append(f"LAYOUT: {s.layout}")
    if s.notes:
        parts.append(s.notes)
    if s.images:
        parts.append("IMMAGINI PER LA GRAFICA: " + s.images)
    t = "\n".join(parts)
    return t[:3990]


def slide_html(s: deckfmt.Slide) -> str:
    lay = s.inferred_layout()
    title = inline(s.title)
    aside = f"<aside>{html.escape(notes_text(s), quote=False)}</aside>" if (s.notes or s.images) else ""
    base = f"background:{BG};color:{INK};font-family:{FONT};padding:128px;display:flex;flex-direction:column;gap:40px"
    if lay == "statement":
        return (f'<section id="{s.id}" data-transition="fade" style="{base};justify-content:center;align-items:center">'
                f'<h2 style="font-size:88px;font-weight:800;line-height:1.15;text-align:center;width:1500px">{title}</h2>{aside}</section>')
    size = body_size(s.words)
    if lay == "segnaposto":
        return (f'<section id="{s.id}" style="{base};justify-content:center">'
                f'<h2 style="font-size:56px;font-weight:800;line-height:1.1">{title}</h2>'
                f'<div style="border:4px dashed {MUTED};border-radius:24px;padding:64px">'
                f'<p style="font-size:32px;line-height:1.4;color:{MUTED}">{body_html(s.body)}</p></div>{aside}</section>')
    if lay == "stack":
        b = body_html(s.body)
        return (f'<section id="{s.id}" style="{base};align-items:center">'
                f'<h2 style="font-size:64px;font-weight:800;line-height:1.1;text-align:center">{title}</h2>'
                f'<p style="font-size:{min(size, 30)}px;line-height:1.35;width:1200px">{b}</p>{aside}</section>')
    # densa, build, muro, mappa
    return (f'<section id="{s.id}" style="{base};justify-content:flex-start">'
            f'<h2 style="font-size:64px;font-weight:800;line-height:1.1">{title}</h2>'
            f'<p style="font-size:{size}px;line-height:1.4;width:1500px">{body_html(s.body)}</p>{aside}</section>')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--out", required=True)
    ap.add_argument("--update", help="deck.json esistente da aggiornare (tiene le sue chiavi, niente 'lists')")
    a = ap.parse_args()
    deck = deckfmt.parse(Path(a.deck).read_text(encoding="utf-8"))
    if not deck.slides:
        print("Nessuna slide trovata: controlla il formato (references/FORMATO_DECK.md)", file=sys.stderr)
        return 2
    ids = [s.id for s in deck.slides]
    bad = [i for i in ids if not ID_RE.match(i)]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    if bad or dup:
        print(f"Id non validi: {bad} · duplicati: {dup}", file=sys.stderr)
        return 2
    out = Path(a.out) / "project"
    (out / "slides").mkdir(parents=True, exist_ok=True)
    for s in deck.slides:
        (out / "slides" / f"{s.id}.html").write_text(slide_html(s), encoding="utf-8")
    sections = {f"s{n+1}": {"description": (b or "Senza blocco")[:200], "start": sid} for n, (b, sid) in enumerate(deck.blocks)}
    if a.update:
        idx = json.loads(Path(a.update).read_text(encoding="utf-8"))
        idx.update({"order": ids, "sections": sections})
        idx.setdefault("faces", {}).update(FACES)
        idx.setdefault("cover", ids[0])
    else:
        idx = {"v": 4, "createdOnFiles": {"v": 1, "at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
               "lists": "css", "title": re.sub(r"\s*·\s*export testo\s*$", "", deck.title) or "Webinar",
               "order": ids, "sections": sections, "cover": ids[0], "faces": FACES, "designSystems": []}
    (out / "deck.json").write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"OK · {len(ids)} slide · {len(sections)} blocchi · {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
