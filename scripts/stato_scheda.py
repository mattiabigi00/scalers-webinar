#!/usr/bin/env python3
"""Stato di un webinar dalla sua scheda: dove sei, cosa manca, cosa blocca, prossima azione.

Uso:
  python3 stato_scheda.py SCHEDA_WEBINAR_<P>.md [--cartella <cartella WEBINAR del cliente>]

Il passaggio si ricava dalle righe "Cancello N chiuso" del registro §12 (references/CANCELLI.md);
se non ce ne sono, dal campo "Passaggio attuale" della §0.
Con --cartella conta anche i segnaposto aperti nei file DECK_*/SCRIPT_* e le domande per il cliente.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import schedafmt as sf  # noqa: E402

PASSI = ["Offerta pronta", "Big Domino + meccanismo + metafora", "Materiale del cliente", "Architettura",
         "Script", "Slide copy", "Grafica", "Audit", "Recita e messa in onda"]
SEZ_PER_PASSO = {0: [2], 1: [3], 2: [4, 5, 7, 8, 9], 3: [6, 10, 11], 4: [], 5: [], 6: [7, 8], 7: [13], 8: [7, 8, 13]}
PROSSIMA = {
    0: "Chiudere l'offerta (scheda §2): skill webinar-stack. Richiesta prove al cliente (intake §4, messaggio D).",
    1: "Big Domino: forma grezza, 3-5 opzioni, 5 criteri, test competitor, stress test del prospect-scettico. Il senior sceglie e dichiara la versione ufficiale.",
    2: "Materiale del cliente: intake Parte 1, controllo delle risposte (E2 ⛔), beat dell'Epiphany Bridge in §5, decisione sulle prove mancanti.",
    3: "Architettura: scegliere A (una credenza per fase) o B (LKBD in ogni step + muro), tabella dei blocchi, §6 §10 §11.",
    4: "Script v1 → confronto con un webinar reale (G23) → v2.",
    5: "Slide copy: DECK_<P>_testo.md → build_deck.py → artifact Slides (giro 1) → rework del senior.",
    6: "Grafica su un duplicato, nel design system del cliente. Copy identico.",
    7: "Audit indipendente: lint_deck.py + agente auditor. Poi correzioni approvate.",
    8: "Pre-volo al cliente (messaggio E), ~10 prove, consegna ai venditori con call già fissata (N5 ⛔).",
    9: "Webinar in onda. Aggiornare REGOLE con le lezioni (M10).",
}
PH_RE = re.compile(r"\[(?:PROOF|DA CLIENTE|INVENTATO|WALL|PROVE)[^\]]*\]|Inserire qui", re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("scheda")
    ap.add_argument("--cartella")
    a = ap.parse_args()
    txt = Path(a.scheda).read_text(encoding="utf-8")
    sec = sf.sections(txt)

    chiusi = {}
    chiusi_5a = False
    for r in sf.table_rows(sec.get(12, "")):
        for c in r:
            m = re.search(r"Cancello\s+(\d)\s+chiuso", c, re.I)
            if m:
                chiusi[int(m.group(1))] = (r[0], r[2] if len(r) > 2 else "")
            if re.search(r"Cancello\s+5a\s+chiuso", c, re.I):
                chiusi_5a = True
    if chiusi:
        n = 0
        while n in chiusi:
            n += 1
        fonte = "registro §12"
    else:
        n = None
        for r in sf.table_rows(sec.get(0, "")):
            if r and r[0].lower().startswith("passaggio"):
                m = re.search(r"(\d)", r[1] if len(r) > 1 else "")
                n = int(m.group(1)) if m else 0
        n = 0 if n is None else n
        fonte = "campo 'Passaggio attuale' della §0 (nessuna riga 'Cancello N chiuso' nel registro)"

    STATUS_COLS = ("stato", "consenso", "liberatoria")

    def aperti(s: int) -> list[str]:
        """Voci aperte di una sezione: nelle tabelle con una colonna Stato/Consenso/Liberatoria,
        le righe con quella cella vuota o ❌; fuori dalle tabelle, le righe con ❌.
        Il registro (§12) e le versioni (§14) non si contano."""
        if s in (12, 14):
            return []
        out, hdr, col = [], None, None
        for line in sec.get(s, "").splitlines():
            st = line.strip()
            low = st.lower()
            if not st.startswith("|"):
                hdr, col = None, None
                if "❌" in st and not low.startswith(">") and "legenda" not in low and "(✅ / 🟡 / ❌" not in st and "competitor" not in low:
                    out.append(st[:70])
                continue
            if re.match(r"^\|[\s\-:|]+\|$", st):
                continue
            cells = [c.strip() for c in st.strip("|").split("|")]
            if hdr is None:
                hdr = [c.lower() for c in cells]
                col = next((i for i, c in enumerate(hdr) if any(k in c for k in STATUS_COLS)), None)
                continue
            if "competitor" in low or "può dire" in low:
                continue
            name = cells[0][:70] if cells else ""
            if col is not None and col < len(cells):
                cell = cells[col]
                if (not cell or "❌" in cell) and any(c for c in cells[:col]):
                    out.append(name)
            elif "❌" in st:
                out.append(name)
        return out

    def gialli(s: int) -> int:
        return sum(line.count("🟡") for line in sec.get(s, "").splitlines())

    print(f"# Stato · {txt.splitlines()[0].lstrip('# ').strip()}\n")
    etichetta = PASSI[n] if n < 9 else "in onda"
    if n == 5 and chiusi_5a:
        etichetta += " · 5a chiuso (deck giro 1 pubblicato): manca 5b, il rework del senior"
    print(f"**Dove sei:** passaggio {min(n, 9)} · {etichetta} (da {fonte}).")
    if chiusi:
        print("**Cancelli chiusi:** " + " · ".join(f"{k} ({v[0]}, {v[1]})" for k, v in sorted(chiusi.items())))
    print("\n**Cosa manca per chiudere questo passaggio** (voci ❌ nelle sezioni della scheda che lo riguardano):")
    manca = []
    for s in SEZ_PER_PASSO.get(n, []):
        for x in aperti(s):
            manca.append(f"- §{s}: {x}")
    print("\n".join(manca) if manca else "- nessuna voce ❌ nelle sezioni del passaggio: controlla la checklist di uscita in references/CANCELLI.md")

    print("\n**Cosa blocca la messa in onda** (❌ in tutta la scheda):")
    tot = {s: aperti(s) for s in sec}
    blocchi = [f"- §{s}: {len(v)} ❌ ({'; '.join(v[:3])}{'…' if len(v) > 3 else ''})" for s, v in sorted(tot.items()) if v]
    print("\n".join(blocchi) if blocchi else "- niente ❌ in scheda")
    g = sum(gialli(s) for s in sec)
    if g:
        print(f"- 🟡 da confermare col cliente: {g}")
    ap13 = [r for r in sf.table_rows(sec.get(13, "")) if r and r[0] not in ("#",) and not r[0].startswith("~~")]
    ap13 = [r for r in ap13 if not (len(r) > 1 and r[1].startswith("~~"))]
    if ap13:
        print(f"- aperti in §13: {len(ap13)}")

    # Controlli automatici dei cancelli (le voci 🤖 di CANCELLI.md che si leggono dalla scheda)
    print("\n**Controlli automatici sulla scheda:**")
    tot_v, prezzo = None, None
    for r in sf.table_rows(sec.get(2, "")):
        if not r:
            continue
        head = r[0].replace("*", "").strip().lower()
        nums = [int(re.sub(r"[.'’]", "", x)) for x in re.findall(r"(\d{1,3}(?:[.'’]\d{3})+|\d{3,})", " ".join(r[1:]))]
        if head == "totale" and nums:
            tot_v = nums[-1]
        if head == "prezzo" and nums:
            prezzo = nums[0]
    if tot_v and prezzo:
        ratio = tot_v / prezzo
        esito = "ok" if 5 <= ratio <= 10 else "fuori da 5-10: serve un override registrato (B5)"
        print(f"- rapporto valore/prezzo (B5): {tot_v:,} / {prezzo:,} = {ratio:.1f} volte · {esito}".replace(",", "."))
    else:
        print("- rapporto valore/prezzo (B5): non calcolabile (manca Totale o Prezzo nella tabella stack della §2)")
    senza = []
    rows7 = sf.table_rows(sec.get(7, ""))
    if rows7:
        hdr = [c.lower() for c in rows7[0]]
        li = next((i for i, c in enumerate(hdr) if "liberatoria" in c), None)
        for r in rows7[1:]:
            if li is not None and li < len(r) and r[0] and not r[0].startswith("["):
                if "✅" not in r[li] and "—" not in r[li]:
                    senza.append(r[0][:50])
    print(f"- prove senza liberatoria ✅ in §7 (L2 ⛔ se vanno in onda con nome e volto): {len(senza)}" + (f" ({'; '.join(senza[:4])}{'…' if len(senza) > 4 else ''})" if senza else ""))
    terzi = []
    rows8 = sf.table_rows(sec.get(8, ""))
    if rows8:
        hdr = [c.lower() for c in rows8[0]]
        ci = next((i for i, c in enumerate(hdr) if "consenso" in c), None)
        for r in rows8[1:]:
            if ci is not None and ci < len(r) and r[0] and "✅" not in r[ci]:
                terzi.append(r[0][:40])
    print(f"- terzi senza consenso ✅ in §8 (L4 ⛔ prima dell'onda): {len(terzi)}" + (f" ({'; '.join(terzi[:4])}{'…' if len(terzi) > 4 else ''})" if terzi else ""))

    if a.cartella:
        c = Path(a.cartella)
        print("\n**Segnaposto nei file di lavoro:**")
        import deckfmt
        for f in sorted(list(c.glob("DECK_*.md")) + list(c.glob("SCRIPT_*.md"))):
            t = f.read_text(encoding="utf-8")
            d = deckfmt.parse(t)
            vis = "\n".join(x.title + "\n" + x.body for x in d.slides) if d.slides else t
            print(f"- {f.name}: {len(PH_RE.findall(vis))} (solo testo visibile)")
        dq = list(c.glob("DOMANDE_CLIENTE_*.md"))
        for f in dq:
            aperte = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip().startswith("- [ ]")]
            print(f"- {f.name}: {len(aperte)} domande aperte")

    print(f"\n**Prossima azione:** {PROSSIMA[min(n, 9)]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
