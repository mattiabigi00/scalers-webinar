"""Parser e writer del formato DECK testo (references/FORMATO_DECK.md).

Solo libreria standard. Usato da build_deck.py, export_deck.py e lint_deck.py.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

SLIDE_RE = re.compile(r"^###\s+(\d+)\s*·\s*([^·]+?)\s*·\s*(.*)$")
BLOCK_RE = re.compile(r"^##\s+(?!#)(.*)$")
LAYOUT_RE = re.compile(r"^\[layout:\s*([a-z]+)\s*\]\s*$")
IMG_RE = re.compile(r"^\[immagini:\s*(.*)\]\s*$")


@dataclass
class Slide:
    pos: int
    id: str
    title: str
    block: str = ""
    body: str = ""
    images: str = ""
    notes: str = ""
    layout: str = ""
    line: int = 0  # riga del ### nel file

    @property
    def title_plain(self) -> str:
        return self.title.replace("==", "")

    @property
    def words(self) -> int:
        return len(re.findall(r"\w+", self.body, flags=re.UNICODE))

    def inferred_layout(self) -> str:
        if self.layout:
            return self.layout
        t = self.title.strip().upper()
        if not self.body.strip():
            return "statement"
        if t.startswith(("PROOF", "[PROOF", "[WALL", "[PROVE")) or "[PROOF:" in self.body or "Inserire qui" in self.body:
            return "segnaposto"
        if "Valore totale" in self.body:
            return "stack"
        return "densa"


@dataclass
class Deck:
    title: str = ""
    source: str = ""
    slides: list[Slide] = field(default_factory=list)
    blocks: list[tuple[str, str]] = field(default_factory=list)  # (nome blocco, id prima slide)


def parse(text: str) -> Deck:
    deck = Deck()
    cur: Slide | None = None
    block = ""
    body: list[str] = []
    notes: list[str] = []
    in_notes = False

    def close():
        nonlocal cur, body, notes, in_notes
        if cur is not None:
            cur.body = "\n".join(body).strip("\n")
            cur.notes = "\n".join(notes).strip()
            deck.slides.append(cur)
        cur, body, notes, in_notes = None, [], [], False

    for i, raw in enumerate(text.splitlines(), start=1):
        line = raw.rstrip()
        if line.startswith("# ") and not deck.title:
            deck.title = line[2:].strip()
            continue
        if line.startswith("Fonte:") and cur is None and not deck.source:
            deck.source = line
            continue
        m = SLIDE_RE.match(line)
        if m:
            close()
            cur = Slide(pos=int(m.group(1)), id=m.group(2).strip(), title=m.group(3).strip(), block=block, line=i)
            if not deck.blocks or deck.blocks[-1][0] != block:
                deck.blocks.append((block, cur.id))
            continue
        m = BLOCK_RE.match(line)
        if m and not line.startswith("###"):
            close()
            block = m.group(1).strip()
            continue
        if cur is None:
            continue
        if line.startswith(">"):
            in_notes = True
            t = line[1:].lstrip()
            if t.startswith("Note:"):
                t = t[5:].lstrip()
            notes.append(t)
            continue
        if in_notes:
            # dopo le note, righe non ">" sono ancora note solo se non vuote e continuano il blocco
            if line.strip():
                notes.append(line.strip())
            continue
        m = LAYOUT_RE.match(line)
        if m and not body:
            cur.layout = m.group(1)
            continue
        m = IMG_RE.match(line)
        if m:
            cur.images = m.group(1).strip()
            continue
        body.append(line)
    close()
    return deck


def render(deck: Deck) -> str:
    out = [f"# {deck.title}"]
    src = deck.source or "Fonte: bozza · versione - · estratto il - · 0 slide"
    src = re.sub(r"·\s*\d+\s*slide\s*$", f"· {len(deck.slides)} slide", src)
    out.append(src)
    last_block = None
    for s in deck.slides:
        if s.block != last_block:
            out.append("")
            out.append(f"## {s.block}" if s.block else "## Senza blocco")
            last_block = s.block
        out.append("")
        out.append(f"### {s.pos} · {s.id} · {s.title}")
        if s.layout:
            out.append(f"[layout: {s.layout}]")
        if s.body.strip():
            out.append(s.body.strip("\n"))
        if s.images:
            out.append(f"[immagini: {s.images}]")
        if s.notes:
            for j, nl in enumerate(s.notes.splitlines()):
                out.append(("> Note: " if j == 0 else "> ") + nl)
    return "\n".join(out).rstrip() + "\n"
