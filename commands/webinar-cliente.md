---
description: Scrive il messaggio da mandare al cliente del webinar (briefing, storia da rifare, pezzi mancanti, prove, pre-volo) o aggiorna le domande aperte
argument-hint: A | B | C | D | E | domande
---

Messaggio al cliente del webinar in corso. Tipo: **$ARGUMENTS**. Usa la skill `webinar-intake`.

I modelli sono nella Parte 2 di `${CLAUDE_PLUGIN_ROOT}/templates/INTAKE_WEBINAR_CLIENTE.md`:
- **A** briefing iniziale (domino, meccanismo, storia, credenze) · **B** la storia non funziona · **C** i pezzi mancanti dell'Epiphany Bridge · **D** le prove · **E** il pre-volo prima di registrare.
- **domande**: un messaggio unico con tutte le righe aperte di `DOMANDE_CLIENTE_<P>.md`, raggruppate per tema, ognuna con il perché in mezza riga.

Compila il modello con i dati della scheda. Regole (M4, M5): per iscritto o trascrizione, mai vocali; cosa non va, perché, cosa deve fare la versione giusta; esempio **inventato di un altro settore** che mostri la forma; **mai** la risposta già scritta.

Consegna il messaggio pronto da incollare. Poi segna in scheda §13 cosa è stato chiesto, a chi e quando. Il messaggio lo manda il copy, non tu.
