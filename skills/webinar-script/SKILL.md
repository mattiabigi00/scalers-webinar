---
name: webinar-script
description: Scrive l'architettura (tabella dei blocchi con minuti) e lo script completo di un webinar Scalers - v1, confronto con un webinar reale che converte, v2 - con le frasi congelate verbatim dalla scheda. Usala quando il copy dice "facciamo la struttura del webinar", "scrivi lo script", "script del webinar di X", "confronta lo script con un webinar vero", "v2 dello script", "quanto dura il webinar".
---

# Webinar Scalers · architettura e script

Due passaggi:
- **3 · Architettura**: la tabella dei blocchi, dopo che `webinar-tre-segreti` ha fissato credenze e prove.
- **4 · Script**: v1 completa → confronto con un webinar reale che converte → v2 con i buchi chiusi.

`R/` = radice del plugin. Leggi: `R/references/MANUALE_WEBINAR_SCALERS.md` §5, §7, §9, §10; `R/references/REGOLE_WEBINAR.md` area **G** e **A1-A3, C9-C10, E, F12, D5**; tutta la scheda. Per la meccanica di scrittura puoi usare la skill W1 del pacchetto marketing, ma **le regole Scalers prevalgono**.

## Prerequisiti

Offerta (§2), domino (§3), storia (§5) e credenze (§6) chiusi. Se uno manca, fermati e dillo con il passaggio a cui tornare (B1, M1).

## 3 · Architettura (`ARCHITETTURA_<P>.md`)

**L'intro canonica** è quella delle regole G3-G11 (nata dal rework di Matteo su Mind Reset). Il `BLUEPRINT_SLIDE_WEBINAR.md` resta il riferimento per densità, layout e formule, ma non per l'ordine dell'intro (conflitto registrato in `R/REVISIONE.md`).

Scheletro di riferimento (dal caso Mind Reset, skill originale `webinar-scalers`):
- **Intro:** promessa (G3, G4) → non è colpa tua, due nemici (G5) → sospetto confermato → te lo prometto (G6) → **domino breve con la sua grafica** (C10) → come ti sentirai quando… (G7) → impegno attivo, es. il foglio (G9) → cosa porti a casa + regalo → chi sono, credenziali a valanga (G11).
- **Storia:** Epiphany Bridge → cosa ho costruito, missione, prove → Big Domino (identico) → "me lo dicono tutti".
- **Tre fasi o tre step:** obiezione → fase → Little Known Big Difference → prova, tre volte, con la mappa tra una fase e l'altra (G12, G13). Architettura A o B come deciso al passaggio 3.
- **Vendita:** Domandina → permesso → nome dell'offerta → stack a strati → quanto vale per te → alternative → prezzo → garanzia → due strade / costo del no → FAQ → regalo → prossimo passo (dettaglio in `webinar-stack`).

La tabella:

| # | Blocco | Cosa fa (credenza / funzione) | Contenuto (fonte in scheda) | Prova | Minuti | Regole |
|---|---|---|---|---|---|---|

Più quattro elenchi sotto la tabella:
- **Dove torna la tesi**: 4-5 punti, identica (C10).
- **Impegno attivo**: dove nasce, dove torna (prezzo, garanzia, CTA) (G9).
- **Promesse piantate → dove si chiudono** (G14) → copiale in scheda §10.
- **Solo nello stack** (G15) → scheda §11.
- **Obiezioni vinte**: dove, e da lì in poi non tornano (F12 ⛔).

Minuti: circa 140 parole al minuto; ~10.000 parole di slide ≈ 75 minuti (H1). Niente slide di servizio (G10).

**La lunghezza la decide il materiale vero.** Se le storie e le prove vere reggono 40 minuti, il webinar dura 40 minuti: non si riempie per arrivare a 75 (G1, A1). Scrivi la durata reale stimata in scheda §0 e, se è molto sotto il riferimento, dillo al senior con cosa servirebbe dal cliente per allungare (storie, prove).

## 4 · Script

### v1 (`SCRIPT_<P>_v1.md`)

- Prima persona del frontman, **registro parlato** (H4). Chi ascolta arriva nuovo.
- Un blocco dell'architettura = una sezione `## Blocco n · nome`. Indicazioni di regia e di slide tra parentesi quadre: `[SLIDE: …]`, `[PAUSA]`, `[CAMBIO TONO]`.
- **Frasi congelate verbatim** dalla scheda: domino breve e lungo, promessa, nomi (M2 ⛔, C9). Mai "migliorarle".
- Il webinar è **emotivo, non didattico** (G1): ogni argomento razionale che può diventare una storia, diventa una storia (G2).
- Gli esempi del prodotto esistono nella scaletta reale (D5); se non puoi verificarlo: `[DA CLIENTE: esiste l'esercizio …?]`.
- **Niente invenzioni**: ogni dato che non è in scheda è `[DA CLIENTE: …]`; ogni prova attesa è `[PROOF: …]`. Tutti finiscono in `DOMANDE_CLIENTE_<P>.md` e in scheda §7/§13 (A1 ⛔, A2 ⛔, A3 ⛔).
- Status: niente che renda l'acquisto imbarazzante (G22).

### Confronto (`CONFRONTO_<P>.md`)

G23: la v1 si confronta con **un webinar reale che converte**. Usa, in ordine: una trascrizione di un webinar vero se il copy la fornisce; altrimenti `R/references/BLUEPRINT_SLIDE_WEBINAR.md` (Grassi) e il deck Mind Reset in `R/examples/`. Cerca i buchi di struttura, non di stile:

| # | Buco | Dove sta nel riferimento | Regola | Blocco della v2 in cui si chiude |
|---|---|---|---|---|

Controlla almeno: impegno attivo · tesi ripetuta · prove dopo ogni step · trial close (Domandina) · FAQ · finale e CTA · regalo consegnato · mappa delle fasi · scena al rallentatore · credenziali con prova · **lunghezza per blocco** (parole o minuti) contro il riferimento. Nel caso Mind Reset i buchi erano 19, i cinque grossi: niente finale, niente impegno attivo, tesi detta una volta, prove tutte alla fine, niente trial close né FAQ.

### v2 (`SCRIPT_<P>_v2.md`)

Tutti i buchi chiusi. Poi i controlli:
- [ ] frasi congelate verbatim (verificalo con `python3 R/scripts/lint_deck.py SCRIPT_<P>_v2.md --scheda <scheda>` se lo script è scritto nel formato `### n · id · titolo`; altrimenti a mano, con una ricerca)
- [ ] nessun `[INVENTATO]`; ogni `[DA CLIENTE]` e `[PROOF]` è nelle domande e nella scheda
- [ ] nessuna obiezione vinta riaperta (F12 ⛔)
- [ ] l'eroe si salva con lo strumento del domino (E2 ⛔)
- [ ] ogni promessa piantata si chiude in modo esplicito ("ricordi…?") (G14)

Poi passa a `webinar-slide`.

## Uscita

Checklist dei passaggi 3 e 4 in `R/references/CANCELLI.md`.

## Da non fare

- Scrivere lo script con offerta, domino o architettura aperti.
- Aprire con una scena prima della promessa (G3).
- Lasciare lo script solo in chat o in un artifact: va nella cartella del cliente (M8).
- Lavorare su uno script di cui esiste una versione più recente fatta da un'altra sessione (M7).
