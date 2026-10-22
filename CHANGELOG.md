# Changelog

Formato: [Keep a Changelog](https://keepachangelog.com/it/1.1.0/) · versioni [SemVer](https://semver.org/lang/it/).

## [1.0.0] · 2026-09-30

Prima versione, da rivedere (vedi `REVISIONE.md`).

### Fonti (copie identiche, nessuna correzione)
- `references/`: MANUALE v2, REGOLE (A-N, 12 ⛔), BLUEPRINT (Grassi, 114 slide), GUIDA_STACK; le tre skill originali in `references/skill-originali/`.
- `templates/`: scheda di progetto, intake cliente v2.
- `examples/mind-reset/`: scheda, caso studio, deck v6 (export testo), audit del 30/9. Il webinar non è ancora definitivo.

### Plugin
- `references/CANCELLI.md`: la pipeline 0-8 con uscite verificabili, ⛔ che bloccano, decisioni umane; il cancello 5 in due tempi (5a automatico, 5b rework del senior).
- `references/FORMATO_DECK.md`: il deck in formato testo, fonte dell'artifact Slides e input dell'audit.
- 10 skill: `webinar-pipeline` (orchestratore, modalità guidata e automatica), `-intake`, `-big-domino`, `-epiphany-bridge`, `-tre-segreti`, `-stack`, `-script`, `-slide`, `-audit`, `-tutor`.
- 8 comandi: `/webinar-nuovo`, `-stato`, `-avanti [auto]`, `-decidi`, `-cliente`, `-audit`, `-palestra`, `-certifica`.
- 2 agenti: `auditor` (indipendente, con calibrazione dalla regressione), `prospect-scettico`.
- 5 script Python senza dipendenze: `stato_scheda`, `lint_deck`, `build_deck` (H3 garantita per costruzione), `export_deck` (con `--check-h3`), `copertura`.
- `templates/CONSEGNA_WEBINAR.md`: la consegna ai venditori con N5 ⛔.

### Webinar Academy
- L0 (3 moduli), L1 (10 moduli), L2 palestra (3 nicchie × 5 esercizi con rubriche e chiavi del tutor), L3 caso reale Mind Reset, certificazione (brief, rubrica, chiave), onboarding di 2 settimane, il metodo su un foglio.

### Collaudo
- End-to-end su cliente finto: 5 trappole su 5, deck di 110 slide pubblicato come artifact Slides, H3 0 violazioni, andata e ritorno 110/110.
- Regressione Mind Reset: auditor 21/26 → 23/26 dopo la calibrazione, ⛔ 3/3.
- Palestra: il tutor non dà la risposta sotto pressione, rubrica applicata.
- Copertura ⛔: 12/12.
