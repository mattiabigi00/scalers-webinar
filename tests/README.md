# Collaudo del plugin (Fase 3)

| Test | Cosa dimostra | Esito | Dettaglio |
|---|---|---|---|
| **1 · End-to-end su caso finto** | il plugin porta un webinar dall'intake al deck pubblicato fermandosi solo sulle decisioni umane, senza inventare | ✅ 5 trappole su 5 intercettate · deck di 110 slide pubblicato come artifact Slides · H3 0 violazioni · andata e ritorno 110/110 · 33 punti di inceppamento, quelli del plugin corretti | `caso-finto/RISULTATO.md` |
| **2 · Regressione Mind Reset** | l'auditor indipendente ritrova le correzioni dell'audit manuale | ✅ v1 21/26, v2 23/26, ⛔ 3/3 · unione 26/26 | `regressione-mind-reset/RISULTATO.md` |
| **3 · Palestra** | il tutor non dà la risposta al junior che sbaglia il Big Domino | ✅ tre turni, nessuna riscrittura, rubrica applicata | `palestra/RISULTATO.md` |
| **4 · Copertura ⛔** | ogni ⛔ blocca almeno un cancello e compare in almeno un modulo | ✅ 12/12 | `COPERTURA.md` (rigenerare con `python3 scripts/copertura.py --out tests/COPERTURA.md`) |

Controlli automatici da rilanciare dopo ogni modifica:

```
python3 scripts/copertura.py
python3 scripts/lint_deck.py examples/mind-reset/Webinar_Mind_Reset_Deck_v6_testo.md --scheda examples/mind-reset/SCHEDA_WEBINAR_MIND_RESET.md
python3 scripts/build_deck.py tests/caso-finto/WEBINAR/DECK_RITMOSICURO_testo.md --out /tmp/deck && python3 scripts/export_deck.py /tmp/deck --check-h3 --out /tmp/rt.md
```
