# Consegna usata per la regressione (identica per v1 e v2)

1. Copiare in una cartella temporanea l'export del deck e la scheda; dalla copia della scheda togliere le righe che citano l'audit precedente (§13 riga 11, §14 riga "Audit deck v6").
2. Lanciare l'agente `auditor` con questo messaggio (percorsi da adattare):

> Sei l'agente `auditor` del plugin scalers-webinar. Le tue istruzioni complete sono in `agents/auditor.md`: leggilo per intero e seguilo alla lettera. È un collaudo di regressione: conta l'indipendenza.
> INPUT (leggi SOLO questi file): oggetto = `<tmp>/Webinar_Mind_Reset_Deck_v6_testo.md`; scheda = `<tmp>/SCHEDA_WEBINAR_MIND_RESET.md`; regole = `references/REGOLE_WEBINAR.md`; formato = `references/FORMATO_DECK.md`; lint = `python3 scripts/lint_deck.py <oggetto> --scheda <scheda> --out <tmp>/lint.md`. Regole di parola del cliente e scaletta: non disponibili, dillo in testa.
> VIETATO leggere: `examples/`, `academy/`, `tests/`, qualsiasi audit precedente.
> Scrivi il risultato in `tests/regressione-mind-reset/AUDIT_AUTO_<versione>_<data>.md`.

3. Confrontare riga per riga con `examples/mind-reset/AUDIT_DECK_V6_2026-09-30.md` e aggiornare `RISULTATO.md`.
