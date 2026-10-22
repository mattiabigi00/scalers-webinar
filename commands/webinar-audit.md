---
description: Audit indipendente del deck o dello script - lint meccanico più agente auditor che vede solo il risultato - senza modificare niente
argument-hint: [link dell'artifact Slides o percorso del file]
---

Audit del webinar. Oggetto: **$ARGUMENTS** (se vuoto: il deck vivo indicato in scheda §0). Usa la skill `webinar-audit`.

1. Prepara l'export testo: se è un artifact Slides leggine i file e lancia `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/export_deck.py" <cartella letta> --url <link> --versione <id> --out DECK_<P>_testo.md --check-h3`.
2. Lint: `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/lint_deck.py" DECK_<P>_testo.md --scheda <scheda> --out LINT_<P>.md`.
3. Lancia l'agente `auditor` passandogli **solo** i percorsi di: export, scheda, `${CLAUDE_PLUGIN_ROOT}/references/REGOLE_WEBINAR.md`, radice del plugin `${CLAUDE_PLUGIN_ROOT}`, regole di parola del cliente e scaletta se ci sono, e il file da scrivere `AUDIT_<P>_<AAAA-MM-GG>.md`. Niente conversazione, niente file di produzione.
4. Consegna le tre righe di testa dell'audit e cosa blocca. **Non correggere niente** finché il senior non dice quali righe applicare.
