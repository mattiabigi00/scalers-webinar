"""Lettura della scheda di progetto (templates/TEMPLATE_SCHEDA_WEBINAR.md compilata)."""
from __future__ import annotations

import re
import unicodedata

SEC_RE = re.compile(r"^##\s+(\d+)\s*·\s*(.*)$")


def norm(t: str) -> str:
    """Normalizza per confronti verbatim: virgolette, trattini, spazi, grassetti, maiuscole."""
    t = unicodedata.normalize("NFC", t)
    t = t.replace("**", "").replace("*", "")
    t = re.sub(r"[“”«»\"]", '"', t)
    t = re.sub(r"[’‘`]", "'", t)
    t = re.sub(r"[—–]", "-", t)
    t = t.replace("…", "...")
    t = re.sub(r"\s+", " ", t)
    return t.strip().lower()


def sections(text: str) -> dict[int, str]:
    out: dict[int, list[str]] = {}
    cur = None
    for line in text.splitlines():
        m = SEC_RE.match(line)
        if m:
            cur = int(m.group(1))
            out[cur] = []
            continue
        if cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.splitlines():
        s = line.strip()
        if not s.startswith("|") or re.match(r"^\|[\s\-:|]+\|$", s):
            continue
        rows.append([c.strip() for c in s.strip("|").split("|")])
    return rows


def quote_after(block: str, label_regex: str) -> str:
    """Testo del blockquote (righe '>') che segue la prima riga che contiene label_regex."""
    lines = block.splitlines()
    for i, l in enumerate(lines):
        if re.search(label_regex, l, flags=re.I):
            q = []
            for m in lines[i + 1:]:
                if m.strip().startswith(">"):
                    q.append(m.strip()[1:].strip())
                elif q:
                    break
                elif m.strip():
                    break
            return "\n".join(q).strip()
    return ""


def glossary(sec9: str) -> list[tuple[str, str]]:
    """Coppie (si dice, non si dice) dalla tabella del glossario §9."""
    part = sec9.split("Si dice / non si dice", 1)
    if len(part) < 2:
        return []
    pairs = []
    for r in table_rows(part[1]):
        if len(r) >= 2 and r[0].lower() not in ("si dice",):
            pairs.append((r[0], r[1]))
    return pairs


def split_terms(cell: str) -> list[str]:
    cell = re.sub(r"\([^)]*\)", "", cell)
    out = []
    for t in re.split(r",|·|;", cell):
        t = t.strip().strip("\"'«»“”").strip()
        t = re.sub(r"^\{|\}$", "", t) if t.startswith("{") else t
        if t and len(t) > 1:
            out.append(t)
    return out


def forbidden(sec9: str) -> list[str]:
    m = re.search(r"\*\*Vietate dal cliente[^*]*\*\*\s*(.+)", sec9)
    words = []
    if m:
        words += split_terms(m.group(1).rstrip("."))
    m = re.search(r"\*\*Vietate da noi[^*]*\*\*\s*(.+)", sec9)
    if m and m.group(1).strip():
        words += split_terms(m.group(1).rstrip("."))
    return words


def overrides(sec9: str) -> list[tuple[str, str]]:
    part = sec9.split("Override", 1)
    if len(part) < 2:
        return []
    seg = part[1].split("Si dice / non si dice", 1)[0]
    out = []
    for r in table_rows(seg):
        if len(r) >= 2 and not r[0].lower().startswith("parola"):
            out.append((r[0].strip('"“” '), r[1]))
    return out
