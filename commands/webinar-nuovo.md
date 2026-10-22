---
description: Apre un nuovo webinar per un cliente - crea la cartella WEBINAR, la scheda di progetto e le domande per il cliente, e parte dal passaggio 0
argument-hint: <cliente> <prodotto>
---

Apri un nuovo webinar Scalers per: **$ARGUMENTS**. Usa la skill `webinar-pipeline`.

1. Individua la cartella del cliente nella cartella di lavoro. Se l'argomento contiene solo il prodotto, il cliente è la cartella in cui stai lavorando (o chiedi se non è chiaro). Crea `WEBINAR/` dentro, se non c'è.
2. Se esiste già una `SCHEDA_WEBINAR_*.md` per questo prodotto, **non crearne un'altra**: fermati e lancia lo stato (`/webinar-stato`).
3. Copia `${CLAUDE_PLUGIN_ROOT}/templates/TEMPLATE_SCHEDA_WEBINAR.md` in `WEBINAR/SCHEDA_WEBINAR_<PRODOTTO>.md` (maiuscolo, senza spazi). Compila solo quello che sai già con certezza (cliente, prodotto, frontman, fonti del cliente in §1, data). Tutto il resto resta vuoto o ❌: niente valori plausibili.
4. Chiedi chi è il **senior** del webinar e scrivilo in §0 (riga "Frontman" resta il frontman; aggiungi il senior nella prima riga del registro §12: `| <data> | Webinar aperto · senior: <nome> | <chi> | scheda |`).
5. Crea `WEBINAR/DOMANDE_CLIENTE_<PRODOTTO>.md` con l'intestazione e nessuna domanda.
6. Se ci sono file della KB del cliente (`CLAUDE.md`, `_START_HERE.md`, `numeri-baseline.md`, `voce.md`, file offerta), leggili e riporta i percorsi in scheda §1.
7. Parti dal **passaggio 0** (offerta + richiesta prove) con le skill `webinar-stack` e `webinar-intake`.

Chiudi con lo stato in quattro righe: dove sei, cosa manca, cosa blocca, prossima azione.
