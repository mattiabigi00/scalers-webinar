# FORMATO DECK — il deck in formato testo

> **Cos'è:** il formato del file `DECK_<P>_testo.md`. È lo stesso dell'export del deck Mind Reset v6 (`examples/mind-reset/Webinar_Mind_Reset_Deck_v6_testo.md`), con due aggiunte facoltative per costruire le slide.
> **Perché esiste:** un solo formato fa tre lavori. Il copy scrive le slide qui; `scripts/build_deck.py` ne ricava l'artifact Slides; `scripts/export_deck.py` riporta qui l'artifact dopo il rework del senior; `scripts/lint_deck.py` e l'agente `auditor` leggono solo questo.

---

## 1. Struttura

```
# <Nome del webinar> — v<N> · export testo
Fonte: <link artifact o "bozza"> · versione <id o -> · estratto il <AAAA-MM-GG> · <n> slide

## Blocco <n> · <nome del blocco>

### <posizione> · <id> · <Titolo della slide>
<corpo>
[immagini: alt: <descrizione> | alt: <descrizione> | svg: <descrizione>]
> Note: <note dello speaker, su una o più righe che iniziano con ">">
```

| Elemento | Regola |
|---|---|
| `# ` | una sola riga, il titolo del deck |
| `Fonte:` | la riga subito sotto. In bozza: `Fonte: bozza · versione - · estratto il 2026-10-01 · 0 slide` (il numero lo aggiorna `build_deck.py`) |
| `## Blocco n · nome` | apre un blocco (diventa una `section` dell'indice dell'artifact). I nomi dei blocchi seguono l'architettura |
| `### pos · id · Titolo` | una slide. `pos` = posizione (1, 2, 3…); `id` = `[A-Za-z0-9_-]`, stabile per tutta la vita della slide (non si rinumera quando si sposta); titolo = il testo a schermo, 2-5 parole di norma (H2) |
| corpo | tutto quello che sta tra il `###` e la prima riga `[immagini:` o `> Note:`. Paragrafi separati da **una riga vuota**. Elenchi: righe che iniziano con `• `. Grassetto con `**…**`, corsivo con `*…*` (citazioni e dialoghi: blueprint §2.2) |
| `[immagini: …]` | facoltativa. Descrive le immagini: `alt:` per foto e 3D, `svg:` per le grafiche di concetto. **Non va a schermo in giro 1**: `build_deck.py` la mette nelle note (H10, I1) |
| `> Note:` | facoltative, le note dello speaker: blocco di script da cui viene la slide, parlato che non sta a schermo, regia, verifiche aperte. Diventano l'`<aside>` della slide |

Una slide senza corpo è una **statement slide** (H6): solo il titolo, grande e centrato.

**Stack slide.** Perché il lint controlli somme e ripetizioni, le voci si scrivono così (euro prima o dopo il numero, separatore delle migliaia `.` o `'`):

```
• La mappatura (valore 1.000 €)
• I ventun giorni di preparazione (valore €5'000)
• La box (non te la metto in euro)

Valore totale: 17.000 €
```

Una voce senza cifra si scrive tra parentesi ("non ha prezzo", "non te la metto in euro"). Le stack slide ripetute hanno le stesse righe, più quelle nuove.

## 2. Le due aggiunte per la costruzione

Entrambe facoltative, entrambe ignorate da lint e audit.

**Parola evidenziata nel titolo** (blueprint §2.1, H3): `==parola==`.

```
### 12 · s031 · L'unica via è ==da dentro==
```

`build_deck.py` la rende con il colore d'accento **dentro lo stesso blocco del titolo** (mai un blocco separato: H3 ⛔). `export_deck.py` la riporta come `==…==`.

**Layout esplicito**: una riga `[layout: <tipo>]` **subito** sotto il `###` (se la metti più giù finisce a schermo: il lint lo segnala). Tipi: `densa` · `statement` · `build` · `muro` · `mappa` · `stack` · `segnaposto`. Se manca, `build_deck.py` lo deduce:

| Se… | Layout |
|---|---|
| il corpo è vuoto | `statement` |
| il titolo inizia con `PROOF`, `[PROOF`, `[WALL` o il corpo contiene `[PROOF:` / `Inserire qui` | `segnaposto` |
| il corpo contiene `Valore totale` | `stack` |
| altrimenti | `densa` |

## 3. Cosa non si scrive mai nel corpo

- Indicazioni di regia, flag, numeri di blueprint, "Immagine: …" (H10): vanno in `> Note:`.
- `[INVENTATO]`: il plugin non lo usa (vedi `CANCELLI.md`, Segnaposto).
- Nomi della colonna "Non si dice" del glossario della scheda §9 (H8).

I segnaposto `[DA CLIENTE: …]` e `[PROOF: …]` **stanno** nel corpo finché non sono chiusi: così il lint li conta e il deck non va in onda con un buco invisibile.

## 4. Dall'artifact al testo e ritorno

```
DECK_<P>_testo.md  ──build_deck.py──▶  deck/project/deck.json + deck/project/slides/<id>.html  ──Artifact publish──▶  Slides
        ▲                                                                                                           │
        └──────────────────────────── export_deck.py ◀── Artifact read (project/deck.json + project/slides/*.html) ─┘
```

- **Andata** (giro 1): `build_deck.py` scrive slide bianche, testo nero, un `<h2>` per il titolo e **al più un `<p>`** per il corpo (nessuno nelle statement) con i paragrafi separati da `<br><br>` e gli elenchi con `• ` (H3 ⛔). Grafiche solo di concetto (I1).
- **Ritorno**: dopo il rework del senior sull'artifact, `export_deck.py` rilegge i file e riscrive il testo nello stesso formato. Con `--check-h3` conta i blocchi di testo per slide e segnala le violazioni H3 (è l'unico modo per verificare H3: sul testo non si vede).
- La **versione live vince** sul file testo: prima di modificare, si esporta (M6).
- Layout e immagini fanno andata e ritorno: `build_deck.py` li scrive nelle note (`LAYOUT: …`, `IMMAGINI PER LA GRAFICA: …`) e `export_deck.py` li rimette al loro posto.
