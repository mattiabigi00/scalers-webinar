# scalers-webinar

Il metodo webinar di Scalers come plugin per Claude. Due cose che usano **la stessa fonte**:

1. **La pipeline**: dall'intake del cliente al deck (artifact Slides), passando per un audit indipendente. Il controllo umano resta solo nei punti di decisione.
2. **La Webinar Academy**: porta un copywriter da zero ad autonomo sui webinar, e lo certifica. In modalità formazione il plugin diventa il tutor.

Metodo: Perfect Webinar di Russell Brunson (*Expert Secrets*), semplificato da Scalers. Quattro blocchi: intro/rapport · Epiphany Bridge + Big Domino · tre segreti · stack. **Si convince solo di cose vere.**

---

## Installazione (3 righe)

In Claude Code, dalla cartella che contiene questo repo:

```
/plugin marketplace add ./scalers-webinar
/plugin install scalers-webinar@scalers
/webinar-stato
```

Quando il repo sarà su GitHub: `/plugin marketplace add <owner>/scalers-webinar`. Nell'app desktop si installa anche come file `.plugin` (lo zip di questa cartella).

## Il tuo primo webinar in 20 minuti

1. Apri la cartella del cliente e lancia `/webinar-nuovo <cliente> <prodotto>`. Nasce `WEBINAR/SCHEDA_WEBINAR_<PRODOTTO>.md`: da qui in poi **la scheda è lo stato** del webinar.
2. Chiudi l'offerta con il plugin (prezzo, stack, garanzia, scarsità): è una decisione del senior. Il plugin prepara la richiesta delle prove per il cliente (`/webinar-cliente D`).
3. Manda l'intake al cliente (`/webinar-cliente A`, poi la Parte 1 di `templates/INTAKE_WEBINAR_CLIENTE.md`). Quando torna compilato, salvalo in `WEBINAR/INTAKE_<PRODOTTO>_risposte.md`.
4. Lancia `/webinar-avanti auto`. Il plugin porta il webinar fino al deck e si ferma solo su: scelta del Big Domino, prove mancanti, architettura delle credenze. Ogni dato che manca diventa `[DA CLIENTE]` in `DOMANDE_CLIENTE_<PRODOTTO>.md`, mai un'invenzione.
5. `/webinar-stato` in qualsiasi momento: dove sei, cosa manca, cosa blocca, prossima azione.
6. `/webinar-audit` sul deck pubblicato: l'agente `auditor` lo controlla senza vedere come è stato fatto.

Per un copy nuovo: `/webinar-palestra <nome>` e segue `academy/onboarding-2-settimane.md`.

## Comandi

| Comando | Cosa fa |
|---|---|
| `/webinar-nuovo <cliente> <prodotto>` | apre scheda, cartella e domande per il cliente; parte dal passaggio 0 |
| `/webinar-stato` | dove sei, cosa manca, cosa blocca, prossima azione |
| `/webinar-avanti [auto]` | un cancello (guidata) o fino al deck più un audit (automatica) |
| `/webinar-decidi <decisione>` | la scrive nel registro della scheda e aggiorna la sezione |
| `/webinar-cliente A\|B\|C\|D\|E\|domande` | il messaggio al cliente, pronto da incollare |
| `/webinar-audit [deck]` | lint + audit indipendente, senza toccare niente |
| `/webinar-palestra <nome>` | Academy: spiegazioni, palestra col tutor socratico, caso reale |
| `/webinar-certifica <nome> avvia\|valuta` | la certificazione |

## Com'è fatto

```
scalers-webinar/
├── .claude-plugin/        plugin.json · marketplace.json
├── references/            LA FONTE: manuale, regole, blueprint, guida stack (copie identiche)
│   ├── CANCELLI.md        la pipeline come la esegue il plugin (uscite verificabili, ⛔, decisioni umane)
│   ├── FORMATO_DECK.md    il deck in formato testo (fonte del deck Slides, input dell'audit)
│   └── skill-originali/   le tre skill da cui nasce il plugin, per confronto
├── skills/                10 skill: pipeline · intake · big-domino · epiphany-bridge · tre-segreti
│                          · stack · script · slide · audit · tutor
├── commands/              8 comandi (sopra)
├── agents/                auditor (indipendente) · prospect-scettico
├── templates/             scheda · intake cliente · consegna ai venditori
├── scripts/               stato_scheda · lint_deck · build_deck · export_deck · copertura (Python, nessuna dipendenza)
├── academy/               L0 · L1 (10 moduli) · L2 palestra (3 nicchie) · L3 caso reale · certificazione
│                          · onboarding 2 settimane · il metodo su un foglio
├── examples/mind-reset/   il caso vero: scheda, caso studio, deck v6, audit
├── tests/                 collaudo: caso finto end-to-end, regressione Mind Reset, palestra, copertura ⛔
└── REVISIONE.md           contraddizioni tra le fonti e scelte da approvare
```

**Una regola cambia in un punto solo.** Il testo delle regole vive in `references/REGOLE_WEBINAR.md`. Skill, cancelli e Academy citano i codici (es. `E2 ⛔`). `python3 scripts/copertura.py` controlla che ogni ⛔ blocchi almeno un cancello e compaia in almeno un modulo dell'Academy.

**Gerarchia in caso di conflitto:** REGOLE > MANUALE > skill > BLUEPRINT > caso studio. I conflitti noti sono in `REVISIONE.md`.

## Per chi rivede

Parti da `REVISIONE.md`, poi `references/CANCELLI.md`, poi `skills/webinar-pipeline/SKILL.md`. Il collaudo è in `tests/`.

Owner del metodo: Matteo Gaggio · Scalers.
