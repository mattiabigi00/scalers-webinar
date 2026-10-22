# Regressione · l'auditor del plugin sul deck Mind Reset v6

> **Cosa si misura:** se l'agente `auditor`, lavorando in modo indipendente, ritrova le correzioni dell'audit fatto a mano il 30/9 (`examples/mind-reset/AUDIT_DECK_V6_2026-09-30.md`).
> **Input dell'auditor:** solo l'export del deck v6 (versione 1790783640-9275), la scheda (senza le due righe che citano l'audit: §13 riga 11 e §14 riga "Audit deck v6"), `REGOLE_WEBINAR.md`, `FORMATO_DECK.md` e il lint. Niente `CLAUDE.md` e `voce.md` del cliente (non disponibili), niente scaletta.
> **Base:** il deck v6 ha già 4 delle 30 correzioni applicate (righe 12, 21, 23, 26). Restano **26** righe trovabili, di cui **3 ⛔** (righe 3, 16, 30).

## Esito

| | v1 · auditor com'era | v2 · auditor calibrato |
|---|---|---|
| Righe dell'audit originale ritrovate | **21 / 26** (81%) | **23 / 26** (88%) |
| ⛔ ritrovate | 3 / 3 (una messa "bassa") | **3 / 3, tutte ⛔** |
| Righe in più, valide | 20 circa (tra cui 3 delle 9 domande dell'audit originale diventate correzioni: s127 F12, box, esempi D5) | 20 circa |
| Unione v1 + v2 | **26 / 26** | |
| File | `AUDIT_AUTO_2026-09-30.md` | `AUDIT_AUTO_v2_2026-09-30.md` |

La soglia di L3 per un copywriter (15 su 26 con tutte le ⛔) è superata da entrambe le versioni.

## Riga per riga

| # orig. | Slide | Problema (audit originale) | Gravità orig. | v1 | v2 |
|---|---|---|---|---|---|
| 1 | s004 | nota superata "42 giorni" | bassa | ✅ | ✅ |
| 2 | s009 | promessa di prova con segnaposto vuoti | alta | ✅ | ✅ |
| 3 | s006/s052 | domino breve non identico | ⛔ | ✅ (messa bassa) | ✅ ⛔ |
| 4 | vari | spazi prima della punteggiatura | bassa | ✅ | ✅ |
| 5 | s011 | "paziente" (parola vietata come aggettivo) | bassa | ❌ scartata come falso positivo | ✅ |
| 6 | s011b | "lievi gibbosità" non parlato | bassa | ❌ | ✅ |
| 7 | s017 | "i tre passaggi" | alta | ✅ | ✅ |
| 8 | s021b | Bonolis sembra ospitata TV · "MTV America" | bassa | ✅ | ❌ |
| 9 | s021d | aziende senza prova visiva · formula Parlamento Europeo | bassa | ✅ | ~ solo la formula, tra gli aperti |
| 10 | s021e | Roberto Carlos sembra un cliente | alta | ~ solo il consenso | ✅ |
| 11 | s035 | nota su Marco (tolto) | bassa | ✅ | ✅ |
| 12 | s045 | "Mind Reset Coaching" | — | già corretta | già corretta |
| 13 | 259955d3 | etichetta "La sessione" | alta | ✅ | ✅ |
| 14 | 259955d3 | "cementificare", "cause che ti hanno reso effetto" | bassa | ✅ | ✅ |
| 15 | s047 | anni di studio incoerenti | alta | ✅ | ✅ |
| 16 | s051 | domino lungo congelato assente | ⛔ | ✅ ⛔ | ✅ ⛔ |
| 17 | r04 | Fase 1 "mette in ordine" (metafora) | alta | ✅ | ✅ |
| 18 | r05 | "guarire" fuori override | alta | ✅ | ✅ |
| 19 | r13w | "centinaia di testimonianze" e muro vuoto | alta | ✅ | ✅ |
| 20 | r21 | storia attribuita a Selye invece che a Robbins | alta | ✅ | ✅ |
| 21 | r22 | "sul figlio" | — | già corretta | già corretta |
| 22 | Domandina | "guarirlo" | alta | ✅ | ✅ |
| 23 | s123 | "dal vivo" | — | già corretta | già corretta |
| 24 | s137 | etichetta "Sessione" | bassa | ❌ | ✅ |
| 25 | s141 | "si muove solo un po'" allarga la garanzia | alta | ✅ | ❌ |
| 26 | s147 | FAQ "non te lo vendiamo" | — | già corretta | già corretta |
| 27 | s150/s151 | "subito" contro "calendario del mese dopo" | bassa | ~ altra contraddizione, stessa zona | ✅ |
| 28 | s151 | regia a schermo | alta | ✅ | ✅ |
| 29 | s152 | frase ripetuta | bassa | ✅ | ✅ |
| 30 | citazioni, s021f, foto | consensi dei terzi | ⛔ | ✅ ⛔ | ✅ ⛔ |

## Cosa è cambiato tra v1 e v2

Dopo la v1 è stata aggiunta ad `agents/auditor.md` una sezione **Calibrazione**, con cinque regole prese dalle righe mancate:
1. una frase congelata ripetuta con anche solo un connettivo diverso resta ⛔ (riga 3);
2. una parola della lista vietata usata in un altro senso si segnala lo stesso, bassa (riga 5);
3. i nomi del glossario valgono anche nelle etichette delle grafiche (riga 24);
4. le slide vicine si confrontano tra loro (riga 27);
5. le frasi da brochure si segnalano sempre, bassa (riga 6).

Le due righe perse dalla v2 (8 e 25) sono di tipo diverso: una credenziale presentata in modo ambiguo e una condizione di garanzia allargata. Per queste due sono state aggiunte altre due righe alla Calibrazione (garanzia con le stesse condizioni della scheda §2; la posizione di una foto con un personaggio decide come la si legge). Da verificare con un terzo giro quando arriva il deck definitivo.

## Cosa trova l'auditor in più (valido, non nell'audit originale)

Titoli troncati a metà parola nelle citazioni (s050, s056, s063, s076) · "il foglio" della camera oscura che si confonde con il foglio di chi guarda (r11, r12) · domino breve ripetuto 2 volte invece di 4-5 (C10) · deroga alla battuta della scimmia (G16) non registrata · stack compatta finale senza le voci (G17) · "appena finita la scuola" contro "a scuola non ci andavo più" (E12) · "Da quel momento… più di quindici anni" dopo il 2017 (E12) · testimonianze s046 dentro l'Epiphany Bridge (E6) · l'aperto 11 citato in §6 ma assente in §13.

## Come si rilancia

Quando arriva il deck Mind Reset definitivo: sostituire l'export in `examples/mind-reset/`, rifare la copia della scheda senza le righe che citano l'audit, lanciare l'agente `auditor` con il messaggio di `CONSEGNA_AUDITOR.md`, e aggiornare questa tabella e `academy/L3-caso-reale/chiave-tutor.md`.
