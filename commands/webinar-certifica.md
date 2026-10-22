---
description: Avvia o valuta la certificazione Webinar Academy di un copywriter - webinar completo su un brief nuovo, audit indipendente, rubrica, difesa del domino, firma del senior
argument-hint: <nome del copy> [avvia | valuta]
---

Certificazione Webinar Academy per: **$ARGUMENTS**. Usa la skill `webinar-tutor`, modalità certificazione, e segui `${CLAUDE_PLUGIN_ROOT}/academy/certificazione/README.md`.

- **avvia**: consegna al copy il brief di certificazione (`${CLAUDE_PLUGIN_ROOT}/academy/certificazione/brief-certificazione.md`), le regole della prova e i tempi. Da qui il tutor non aiuta.
- **valuta**: quando il copy consegna quello che elenca il README della certificazione (scheda, DOMINO_opzioni, ARCHITETTURA, SCRIPT v2, DECK testo, DOMANDE_CLIENTE), lancia l'agente `auditor` in modo indipendente sul deck testo e sulla scheda del copy, applica `${CLAUDE_PLUGIN_ROOT}/academy/certificazione/rubrica.md`, fai la difesa del domino con l'agente `prospect-scettico`, e scrivi il verbale `ACADEMY_<nome>/CERTIFICAZIONE_<data>.md` con esito proposto. **L'esito lo firma il senior.**
