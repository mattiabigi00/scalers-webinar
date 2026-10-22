#!/usr/bin/env python3
"""Controlli meccanici su un deck testo (o uno script nello stesso formato) contro la scheda.

Uso:
  python3 lint_deck.py DECK_<P>_testo.md --scheda SCHEDA_WEBINAR_<P>.md [--out LINT.md]

Fa solo i controlli che si possono fare senza giudizio: segnaposto, frasi congelate verbatim,
stack (somme e ripetizioni identiche), glossario "non si dice", parole vietate e override,
pezzi tolti ancora citati, regia a schermo, densità, refusi tipografici, ripetizioni.
Il giudizio (obiezioni riaperte, metafora, storie, terzi, KB del cliente) lo fa l'agente auditor.

Esce con 1 se trova almeno un problema ⛔.
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deckfmt  # noqa: E402
import schedafmt as sf  # noqa: E402

PLACEHOLDER_RE = re.compile(r"\[(?:PROOF|DA CLIENTE|INVENTATO|WALL|PROVE|IPOTESI|link|Calendario)[^\]]*\]|Inserire qui|\{[A-Z][^}]*\}|\(in arrivo\)|DA VERIFICARE", re.I)
REGIA_RE = re.compile(r"^(Immagine|Grafica|Regia|FLAG|NOTA|Nota di regia|Da mostrare|Mostrare)\b", re.M)
EURO_RE = re.compile(r"(\d{1,3}(?:[.'’]\d{3})+|\d+)\s*€|€\s*(\d{1,3}(?:[.'’]\d{3})+|\d+)")
VAL_RE = re.compile(r"\(valore\s*(?:€\s*([\d.'’]+)|([\d.'’]+)\s*€)\)", re.I)
TOT_RE = re.compile(r"Valore totale:?\s*(?:€\s*([\d.'’]+)|([\d.'’]+)\s*€)", re.I)


def eur(s: str) -> int:
    return int(re.sub(r"[.'’]", "", s))


class Finding:
    def __init__(self, slide, problema, regola, gravita, correzione=""):
        self.slide, self.problema, self.regola, self.gravita, self.correzione = slide, problema, regola, gravita, correzione


def sl(s: deckfmt.Slide) -> str:
    return f"{s.pos} · {s.id} · {s.title_plain[:60]}"


def visible(s: deckfmt.Slide) -> str:
    return s.title_plain + "\n" + s.body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--scheda", help="scheda di progetto: senza, salta i controlli che dipendono dalla scheda (frasi congelate, glossario, parole vietate, pezzi tolti, importi)")
    ap.add_argument("--out")
    a = ap.parse_args()
    deck = deckfmt.parse(Path(a.deck).read_text(encoding="utf-8"))
    scheda_txt = Path(a.scheda).read_text(encoding="utf-8") if a.scheda else ""
    sec = sf.sections(scheda_txt)
    F: list[Finding] = []
    placeholders: list[tuple[str, str]] = []

    # 1 · Segnaposto
    for s in deck.slides:
        hits = PLACEHOLDER_RE.findall(visible(s))
        if s.inferred_layout() == "segnaposto" or hits:
            placeholders.append((sl(s), "; ".join(sorted(set(hits))) or s.title_plain[:60]))
        if re.search(r"\[INVENTATO", visible(s)):
            F.append(Finding(sl(s), "`[INVENTATO]` nel testo: storia o dato inventato", "A3 ⛔", "⛔", "sostituire con un caso vero, un caso logico (F9) o `[DA CLIENTE]`"))

    # 2 · Frasi congelate
    s3 = sec.get(3, "")
    breve = sf.quote_after(s3, r"Versione breve")
    lunga = sf.quote_after(s3, r"Versione lunga")
    all_vis = [(s, sf.norm(visible(s))) for s in deck.slides]
    if breve:
        nb = sf.norm(breve).rstrip(".")
        occ = [s for s, t in all_vis if nb in t]
        if not occ:
            # cerca varianti
            best = max(((difflib.SequenceMatcher(None, nb, sf.norm(p)).ratio(), s, p) for s in deck.slides for p in re.split(r"\n\s*\n", s.body) if p.strip()), default=(0, None, ""), key=lambda x: x[0])
            F.append(Finding(sl(best[1]) if best[1] else "—", f"Big Domino breve congelato non trovato verbatim. Più simile ({best[0]:.0%}): «{best[2][:120]}»", "C9 · M2 ⛔", "⛔", "riportare il testo della scheda §3"))
        else:
            paras = {}
            for s in occ:
                for p in re.split(r"\n\s*\n", s.body):
                    if nb in sf.norm(p):
                        paras.setdefault(sf.norm(p), []).append(s)
            if len(paras) > 1:
                ver = " / ".join(f"{', '.join(x.id for x in v)}: «{k[:70]}»" for k, v in paras.items())
                F.append(Finding(", ".join(s.id for s in occ), f"Il Big Domino breve compare in {len(paras)} versioni diverse: {ver}", "C9 · C10", "⛔", "la slide riusata deve essere identica: stesso testo in tutte le ripetizioni"))
    if lunga:
        deck_all = sf.norm("\n".join(visible(s) for s in deck.slides))
        sentences = [x for x in re.split(r"(?<=[.!?])\s+|\n", lunga) if len(x.split()) >= 4]
        missing = [x for x in sentences if sf.norm(x).rstrip(".").rstrip("…").rstrip(".") not in deck_all]
        if missing:
            F.append(Finding("—", f"Big Domino lungo congelato: {len(missing)} frasi su {len(sentences)} non compaiono verbatim nel deck, es. «{missing[0][:100]}»", "C9 · M2 ⛔", "⛔", "ripristinare il testo congelato, oppure registrare in scheda la nuova versione come decisione"))
    for r in sf.table_rows(sec.get(4, "")):
        if r and r[0].lower().startswith("promessa") and len(r) > 1 and deck.slides:
            prom = sf.norm(r[1]).rstrip(".")
            first = sf.norm(visible(deck.slides[0]))
            if prom and prom not in first:
                ratio = difflib.SequenceMatcher(None, prom, first).ratio()
                F.append(Finding(sl(deck.slides[0]), f"Promessa della slide 1 diversa da quella congelata in scheda §4 (somiglianza {ratio:.0%})", "C9 · M2", "⛔" if ratio < 0.9 else "bassa", "allineare alla scheda"))

    # 3 · Stack
    prev_items: list[str] = []
    stack_slides = [s for s in deck.slides if s.inferred_layout() == "stack"]
    for s in stack_slides:
        items = [l.strip() for l in s.body.splitlines() if VAL_RE.search(l) or re.search(r"\(non [^)]*euro\)|non ha prezzo", l, re.I)]
        vals = [eur(a1 or b1) for l in items for a1, b1 in VAL_RE.findall(l)]
        tot = TOT_RE.search(s.body)
        totv = eur(tot.group(1) or tot.group(2)) if tot else None
        if items and tot and vals and sum(vals) != totv:
            F.append(Finding(sl(s), f"Somma delle voci {sum(vals):,} € ≠ valore totale {totv:,} €".replace(",", "."), "G17 · A6", "⛔", "correggere il totale o i valori (poi la scheda §2)"))
        if items and prev_items:
            changed = [p for p in prev_items if p not in items]
            if changed:
                F.append(Finding(sl(s), f"Stack slide ripetuta non identica alla precedente: voce cambiata o sparita «{changed[0][:80]}»", "G17 · H8 · A6", "alta", "le stack slide ripetute sono identiche salvo le aggiunte"))
        if items:
            prev_items = items

    # 4 · Glossario "non si dice" e parole vietate
    s9 = sec.get(9, "")
    for si_dice, non_si_dice in sf.glossary(s9):
        qualified = "(" in non_si_dice
        only_titles = bool(re.search(r"come titol", non_si_dice, re.I))
        for term in sf.split_terms(re.sub(r"\bcome titol\w*", "", non_si_dice, flags=re.I)):
            if len(term.split()) > 4:
                continue
            proper = any(w[:1].isupper() for w in term.split() if w[:1].isalpha())
            rx = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", 0 if proper else re.I)
            hit = [s for s in deck.slides if rx.search(s.title_plain if only_titles else visible(s))]
            if hit:
                where = ", ".join(s.id for s in hit[:8]) + (f" (+{len(hit)-8})" if len(hit) > 8 else "")
                grav = "alta" if (len(hit) <= 5 and not qualified) else "verifica"
                F.append(Finding(where, f"Glossario: «{term}» non si dice (si dice «{si_dice}») · {len(hit)} slide" + (" · molte occorrenze: controlla il contesto, può essere uso legittimo" if grav == "verifica" else ""), "H8 · A6 · B13", grav, f"«{si_dice}»"))
    ovr = sf.overrides(s9)
    for w in sf.forbidden(s9):
        base = re.sub(r"\s*\(.*$", "", w).strip()
        if not base:
            continue
        stem = base[:-2] if (" " not in base and len(base) >= 6 and re.search(r"(are|ere|ire)$", base)) else base
        rx = re.compile(r"(?<!\w)" + re.escape(stem) + (r"\w*" if stem != base else r"(?!\w)"), re.I)
        for s in deck.slides:
            m = rx.search(visible(s))
            if not m:
                continue
            cov = [o for o in ovr if stem.lower() in sf.norm(o[0])]
            if cov:
                F.append(Finding(sl(s), f"Parola vietata «{m.group(0)}»: c'è un override registrato solo per «{cov[0][1]}». Verifica che questo punto sia coperto", "L8 · L9", "verifica"))
            else:
                grav = "verifica" if "(" in w else "alta"
                F.append(Finding(sl(s), f"Parola vietata dal cliente: «{m.group(0)}» (lista: {w})" + (" · la lista la vieta solo in un contesto: controlla" if grav == "verifica" else ""), "L8 · L9", grav, "riformulare o registrare un override"))

    # 5 · Pezzi tolti ancora citati (F13)
    tolti = set()
    for line in scheda_txt.splitlines():
        if re.search(r"\btolt[aeio]\b", line, re.I):
            seg = re.split(r"\btolt[aeio]\b", line, flags=re.I)[0]
            for name in re.findall(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-zà-ù]{2,})\b", seg):
                if name not in {"Le", "La", "Il", "Lo", "Gli", "Una", "Un", "Storia", "Storie", "Matteo", "Fase", "Nel", "Nella"}:
                    tolti.add(name)
    for name in sorted(tolti):
        rx = re.compile(r"\b" + re.escape(name) + r"\b")
        for s in deck.slides:
            mv = rx.search(visible(s))
            if mv:
                surname = re.match(r"\s+[A-Z]", visible(s)[mv.end():])
                F.append(Finding(sl(s), f"«{name}» risulta tolto in scheda ma è ancora nel testo visibile" + (" (seguito da un cognome: forse è un'altra persona)" if surname else ""), "F13", "verifica" if surname else "alta", "togliere ovunque"))
            elif rx.search(s.notes):
                F.append(Finding(sl(s), f"«{name}» risulta tolto in scheda ma è ancora citato nelle note", "F13", "bassa", "togliere dalla nota"))

    # 6 · Regia a schermo, densità, tipografia, ripetizioni
    for s in deck.slides:
        if s.inferred_layout() != "segnaposto":
            for m in REGIA_RE.finditer(s.body):
                line = s.body[m.start():].splitlines()[0]
                F.append(Finding(sl(s), f"Indicazione di regia a schermo: «{line[:80]}»", "H10", "alta", "spostare nelle note"))
        if s.words > 220:
            F.append(Finding(sl(s), f"{s.words} parole: oltre il massimo (~220)", "H2", "alta", "dividere su due slide"))
        for m in re.finditer(r"(?<=[\w%»\"”])\s+([.,;:!?»])(?=\s|$)|(?<=\w)\s+([\"”])\s*$", visible(s), re.M):
            F.append(Finding(sl(s), f"Spazio prima della punteggiatura: «…{visible(s)[max(0, m.start()-12):m.end()+1].strip()}»", "H11", "bassa", "togliere lo spazio"))
            break
        paras = [p.strip() for p in re.split(r"\n\s*\n", s.body) if p.strip()]
        for x, y in zip(paras, paras[1:]):
            if x == y or (len(x) >= 15 and x[-1] in ".!?" and y.startswith(x)):
                F.append(Finding(sl(s), f"Frase ripetuta di fila: «{x[:60]}»", "H11", "bassa", "tenerne una"))

        if re.search(r"^\[layout:", s.body, re.M):
            F.append(Finding(sl(s), "Riga `[layout: …]` dentro il corpo: va subito sotto il `###`, altrimenti finisce a schermo", "H10 · FORMATO_DECK", "alta", "spostarla sotto il titolo"))
        if re.search(r"(?<!\*)\*(?!\*)[^*\n]+(?<!\*)\*(?!\*)", s.title):
            pass
    leggere = sum(1 for s in deck.slides if s.words < 40)
    if deck.slides and not (0.15 <= leggere / len(deck.slides) <= 0.40):
        F.append(Finding("—", f"Slide leggere (sotto 40 parole): {leggere} su {len(deck.slides)} ({leggere/len(deck.slides):.0%}). Il blueprint ne vuole circa un quarto", "H2", "verifica", "rivedere il ritmo: accorpare o dividere"))

    # 7 · Numeri in euro non presenti in scheda
    allowed = {eur(a or b) for a, b in EURO_RE.findall(scheda_txt)}
    check_euro = bool(scheda_txt)
    for s in stack_slides:
        allowed |= {eur(x) for x in re.findall(r"^([\d.'’]+)\s*€\s*$", s.body, re.M)}
        allowed |= {eur(x) for x in re.findall(r"^€\s*([\d.'’]+)\s*$", s.body, re.M)}
        t = TOT_RE.search(s.body)
        if t:
            allowed.add(eur(t.group(1) or t.group(2)))
    for s in (deck.slides if check_euro else []):
        for a1, b1 in EURO_RE.findall(visible(s)):
            v = eur(a1 or b1)
            if v not in allowed:
                F.append(Finding(sl(s), f"Importo {a1 or b1} € non presente in scheda", "A4 · A6", "verifica", "controllare sulla scheda §2 o sulla fonte primaria"))

    # Output
    order = {"⛔": 0, "alta": 1, "bassa": 2, "verifica": 3}
    F.sort(key=lambda f: (order.get(f.gravita, 9), f.slide))
    cnt = {g: sum(1 for f in F if f.gravita == g) for g in order}
    out = [f"# LINT · {deck.title}", "",
           f"**Controllato:** `{Path(a.deck).name}` ({len(deck.slides)} slide) contro " + (f"`{Path(a.scheda).name}`." if a.scheda else "nessuna scheda: controlli sulla scheda saltati."),
           f"**Esito:** ⛔ {cnt['⛔']} · alta {cnt['alta']} · bassa {cnt['bassa']} · da verificare {cnt['verifica']} · segnaposto {len(placeholders)}.",
           "Solo controlli meccanici: il giudizio lo dà l'agente `auditor`.", "",
           "| # | Slide | Problema | Regola | Correzione | Gravità |", "|---|---|---|---|---|---|"]
    for i, f in enumerate(F, 1):
        out.append(f"| {i} | {f.slide} | {f.problema.replace('|', '/')} | {f.regola} | {f.correzione.replace('|', '/')} | {f.gravita} |")
    out += ["", f"## Segnaposto aperti ({len(placeholders)})", "", "| Slide | Cosa manca |", "|---|---|"]
    out += [f"| {a1} | {b1.replace('|', '/')} |" for a1, b1 in placeholders]
    text = "\n".join(out) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"OK · {len(F)} problemi (⛔ {cnt['⛔']}) · {len(placeholders)} segnaposto · {a.out}")
    else:
        sys.stdout.write(text)
    return 1 if cnt["⛔"] else 0


if __name__ == "__main__":
    sys.exit(main())
