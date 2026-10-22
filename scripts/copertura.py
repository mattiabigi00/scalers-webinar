#!/usr/bin/env python3
"""Tabella di copertura delle regole ⛔: ogni ⛔ di REGOLE_WEBINAR.md deve comparire
in almeno un cancello (references/CANCELLI.md, righe "⛔ bloccanti") e in almeno un modulo dell'Academy.

Uso:
  python3 copertura.py [--root <radice del plugin>] [--out COPERTURA.md]
Esce con 1 se una ⛔ è scoperta.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--out")
    a = ap.parse_args()
    root = Path(a.root)
    regole = (root / "references" / "REGOLE_WEBINAR.md").read_text(encoding="utf-8")
    stop = re.findall(r"^- \*\*([A-N]\d+) ⛔ (.+?)\*\*", regole, re.M)
    canc = (root / "references" / "CANCELLI.md").read_text(encoding="utf-8")
    gates: dict[str, list[str]] = {}
    cur = None
    for line in canc.splitlines():
        m = re.match(r"^## (\d) · (.+)$", line)
        if m:
            cur = m.group(1)
            continue
        if cur and "⛔ bloccanti" in line:
            for code in re.findall(r"\*\*([A-N]\d+)\*\*", line):
                gates.setdefault(code, []).append(cur)
        if cur and line.startswith("## ") and not re.match(r"^## \d", line):
            cur = None
    academy = {}
    for f in sorted((root / "academy").rglob("*.md")):
        t = f.read_text(encoding="utf-8")
        for code, _ in stop:
            if re.search(r"(?<![A-Za-z0-9])" + code + r"(?!\d)", t):
                academy.setdefault(code, []).append(str(f.relative_to(root / "academy")))
    skills = {}
    for f in sorted(list((root / "skills").rglob("SKILL.md")) + list((root / "agents").glob("*.md"))):
        t = f.read_text(encoding="utf-8")
        for code, _ in stop:
            if re.search(r"(?<![A-Za-z0-9])" + code + r"(?!\d)", t):
                skills.setdefault(code, []).append(f.parent.name if f.name == "SKILL.md" else f.stem)
    out = ["# Copertura delle regole ⛔", "",
           f"{len(stop)} regole ⛔ in `REGOLE_WEBINAR.md`. Una riga è ✅ se la regola blocca almeno un cancello **e** compare in almeno un modulo dell'Academy.", "",
           "| ⛔ | Regola | Cancelli che blocca | Skill / agenti che la citano | Moduli Academy | Esito |", "|---|---|---|---|---|---|"]
    miss = 0
    for code, title in stop:
        g, ac, sk = gates.get(code, []), academy.get(code, []), skills.get(code, [])
        ok = bool(g) and bool(ac)
        miss += not ok
        acs = ", ".join(sorted(set(ac))[:4]) + (f" (+{len(set(ac))-4})" if len(set(ac)) > 4 else "")
        out.append(f"| {code} | {title.rstrip('.')} | {', '.join(g) or '—'} | {', '.join(sorted(set(sk))) or '—'} | {acs or '—'} | {'✅' if ok else '❌'} |")
    out.append("")
    out.append(f"**Esito:** {'tutte coperte' if not miss else f'{miss} ⛔ scoperte'}.")
    text = "\n".join(out) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 1 if miss else 0


if __name__ == "__main__":
    sys.exit(main())
