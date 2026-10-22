---
description: Porta avanti il webinar di un cancello (o, con "auto", fino al deck più un audit), fermandosi solo sulle decisioni umane
argument-hint: [auto]
---

Porta avanti il webinar nella cartella di lavoro con la skill `webinar-pipeline`. Argomento: `$ARGUMENTS`.

1. Leggi lo stato: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/stato_scheda.py" <scheda> --cartella <cartella WEBINAR>`.
2. Leggi la sezione del passaggio in corso in `${CLAUDE_PLUGIN_ROOT}/references/CANCELLI.md`.
3. **Senza argomento (modalità guidata):** fai il lavoro del passaggio con la sua skill, spunta la checklist di uscita, e chiedi l'approvazione del senior per chiudere il cancello. Un passaggio solo.
4. **Con `auto` (modalità automatica):** di' una volta che la modalità automatica sostituisce l'approvazione tra i passaggi con i criteri verificati di CANCELLI.md. Poi ripeti: lavora il passaggio → verifica l'uscita → se è tutta verificata e non c'è una decisione 🧑, chiudi il cancello con la riga di registro "chiuso in automatico, criteri verificati" (chi = plugin) e passa al successivo. **Ti fermi solo** su: offerta (prezzo, stack, garanzia, scarsità), scelta del Big Domino, prove mancanti, scelta dell'architettura A/B, una ⛔ violata che non puoi risolvere senza il cliente. Ti fermi comunque dopo il cancello **5a** (deck giro 1 pubblicato, privato): lanci un audit di controllo con `/webinar-audit` (M9) e aspetti il rework del senior (5b). Grafica (6) e messa in onda (8) mai in automatico.
5. A ogni fermata: la decisione in una riga, 3-5 opzioni con pro e contro, la tua raccomandazione, cosa succede dopo.
6. Prima di chiudere il turno aggiorna la scheda (§0, §12, §13) e riporta lo stato in quattro righe.

Mai chiudere un cancello con una ⛔ violata. Mai riempire un dato mancante: `[DA CLIENTE: …]` e riga in `DOMANDE_CLIENTE_<P>.md`.
