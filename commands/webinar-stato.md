---
description: Dice a che punto è un webinar - dove sei, cosa manca, cosa blocca, prossima azione - leggendo la scheda di progetto
argument-hint: [cliente o prodotto]
---

Stato del webinar **$ARGUMENTS** (se vuoto: l'unica scheda nella cartella di lavoro, o chiedi quale).

1. Trova `**/WEBINAR/SCHEDA_WEBINAR_*.md`.
2. Lancia: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/stato_scheda.py" <scheda> --cartella <cartella WEBINAR>`
3. Apri la sezione del passaggio in corso in `${CLAUDE_PLUGIN_ROOT}/references/CANCELLI.md` e spunta la checklist di uscita voce per voce guardando la scheda e i file (✅ verificata · ❌ no · ? non verificabile da qui).
4. Se ci sono cancelli chiusi in automatico dal plugin, elencali: il senior li deve rileggere.

Rispondi **sempre** in quattro blocchi, brevi:
- **Dove sei** · passaggio e nome.
- **Cosa manca** per chiudere questo cancello.
- **Cosa blocca** la messa in onda (⛔ aperte, prove, consensi, domande al cliente).
- **Prossima azione** · una sola, con chi la fa.

Non modificare niente.
