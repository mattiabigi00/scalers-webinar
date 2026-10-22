# L1.8 · Slide copy

> **Cos'è:** come lo script diventa slide: le slide **sono** lo script, un blocco di testo per titolo e uno per corpo, densità, layout, e cosa ha insegnato il rework di Matteo. **Durata:** ~45 minuti. **Prerequisiti:** L1.1-L1.7.
> **Regole:** H1-H11 con **H3 ⛔**, I1, N4 · **Manuale:** §10 (passaggio 5) · `references/BLUEPRINT_SLIDE_WEBINAR.md` §2-3 · `references/FORMATO_DECK.md`

---

## La regola in breve

**H1 Le slide sono lo script.** Il presentatore legge e recita il testo a schermo: scrivere le slide = scrivere quello che dice. ~10.000 parole ≈ 75 minuti a 140 parole/minuto. Non è un deck "tre parole e parlo io" (blueprint §1).

**H3 ⛔ Titolo = un unico blocco di testo. Corpo = un unico blocco di testo.** Paragrafi separati da a capo doppio, elenchi con "•", parola evidenziata con colore o corsivo **dentro** lo stesso blocco. Perché esiste: *"Blocchi separati rendono l'editing lento"* (H3); nelle parole di Matteo, *"altrimenti modificarle è un incubo"* (caso studio, passaggio 5). Il senior riscrive a mano il deck: se ogni paragrafo è una casella a sé, il rework diventa lavoro di impaginazione.

| Codice | Cosa dice, in parole semplici |
|---|---|
| **H2** | Slide dense 90-150 parole (max ~220 solo sulle slide chiave); titoli di 2-5 parole con **una** parola evidenziata; circa un quarto di slide leggere; sopra i 5-6 punti si divide. |
| **H4** | Registro parlato, basso carico cognitivo. *"Se una frase va spiegata, va riscritta."* |
| **H5** | Si coinvolge, non si scredita (*"Immagina di poter pranzare con il bambino che eri…"*, non *"…e quasi ci parli"*). |
| **H6** | Statement slide per le frasi chiave: una frase sola, grande, centrata. |
| **H7** | Il grassetto va sulla frase che conta, non sparso. |
| **H8** | Nomi identici ovunque; stack slide ripetute identiche. |
| **H9** | Ogni slide densa chiude con un **gancio** verso la successiva. |
| **H10** | Il deck consegnato è pulito: regia, flag, verifiche nelle note dello speaker. |
| **H11** | Zero refusi. |

**Prima il copy, poi la grafica** (I1): il primo deck è bianco con testo nero; la grafica si fa su un duplicato quando il copy è approvato.

**I layout del blueprint** (§2.4) e il loro nome nel deck testo (`FORMATO_DECK.md` §2):

| Blueprint | Com'è | Parole | In `FORMATO_DECK` |
|---|---|---|---|
| **A** / **A'** | titolo + corpo denso (~60%) + immagine a destra / a sinistra | 80-220 / 60-180 | `densa` |
| **B** | solo testo a tutta larghezza, titolo centrato | 50-215 | `densa`; senza corpo è `statement` |
| **C** | build progressivo: stesso titolo, una riga in più per slide | 3-33 | `build` |
| **D** | muro di prove | 5-50 | `muro` (finché le prove non ci sono: `segnaposto`) |
| **E** | mappa a 3 colonne degli step | 30-45 | `mappa` |
| **F** | stack slide | 30-90 | `stack` |
| **G** | meme / video | 3-7 | nessun tipo dedicato: l'immagine si descrive in `[immagini: …]`, che in giro 1 va nelle note |

**Il rework di Matteo delle prime 46 slide** (24/9, scheda §12: *"promessa con 43 giorni, domino in slide 3-6, niente slide di servizio, un blocco di testo"*) è diventato il modello, oggi nelle regole G3-G11 e H1-H11 (caso studio, passaggio 5). Le sue correzioni ricorrenti:

> - *titolo e corpo in un unico blocco di testo, altrimenti modificarle è un incubo;*
> - *frasi parlate, chiare a chi arriva nuovo, senza righe "da slide";*
> - *non screditare quello che si offre ("e quasi ci parli" → "immagina di poterci parlare");*
> - *non riaprire un'obiezione già risolta (via "nessuno ti lava il cervello" dal recap);*
> - *WhatsApp solo nello stack, la box annunciata come sorpresa e ripresa dopo.*

E il metodo per usarlo: il rework si fa su una parte, poi **le sue mosse si applicano a tutto il deck** (manuale §10, passaggio 5).

## Esempio buono

**Una slide nel formato del deck testo** (`examples/mind-reset/Webinar_Mind_Reset_Deck_v6_testo.md`, slide 109 · s134, citata per intero):

```
### 109 · s134 · Un quarto
Posso tenerlo a un quarto per un motivo semplice.

In quella stanza, quello che ti arriva è la mia voce, e la voce c'è.

Quello che non c'è è la mia ora.
> Note: Slide 128 · Blocco 21 · Blueprint S102–S103 · Layout B. FONTE/NOTE: FONTE: blocco 21. Titolo mio. È la ragione del prezzo (S103 del blueprint).
```

Titolo di due parole. Corpo in un blocco, tre paragrafi brevi, parlato. Nessuna regia a schermo: fonte e layout stanno nella nota (H10).

**H5, coinvolgere senza screditare.** Slide 64 · r05: *"Immagina di avere l'occasione di pranzare con il bambino che eri, e di poterci parlare. In uno dei 21 giorni faremo esattamente questo."*

**H9, il gancio.** Le slide dense di Grassi chiudono sempre verso la successiva: *"Vuoi sapere come? · Quindi ti chiedo… · Ti spiego… · Ecco le prove… · Vuoi sapere come si chiama?"* (blueprint §3.3). In Mind Reset, il testo di slide 60 · r03 finisce con *"E magari ti starai chiedendo: ma perché non fare direttamente la sessione, se funziona così bene?"* (la nota: *"Chiude con la domanda che porta al palazzo al buio."*), e la slide dopo è il palazzo al buio.

**H6, statement slide.** Slide 58 · r01: solo il titolo, *"«Sì, ma io non voglio farmi lavare il cervello.»"*. Slide 55 · s053: *"Ed è esattamente quello che fa Mind Reset."*

**H2 in numeri.** Deck di Grassi: media 90 parole per slide, dense tra 90 e 150, sopra le 200 solo le slide-chiave (blueprint §3.1). Deck Mind Reset v6: nessuna slide oltre 220 parole, massimo 176 (s047) (audit, "Cosa è pulito").

## Esempio sbagliato e perché

Tutti dall'audit del deck v6 (`examples/mind-reset/AUDIT_DECK_V6_2026-09-30.md`).

| Riga | Slide | Testo | Regola | Perché |
|---|---|---|---|---|
| 6 | 9 · s011b | *"ora sono solo lievi gibbosità"* | H4 | nessuno lo direbbe a voce; proposta: *"…ora sono solo colline"* |
| 14 | 49 · 259955d3 | *"Individui le cause che ti hanno reso effetto"*, *"cementificare"* | H4 | *"frasi da brochure, non parlate"* |
| 13 · 24 | 49 · 259955d3 · 112 · s137 | etichetta grafica *"La sessione"*, *"Sessione"* | H8 | il nome è "Sessione di Trasformazione", anche nelle etichette |
| 28 | 126 · s151 | *"Da mostrare vero: niente countdown, niente 'ultimi posti'."* a schermo | H10 | è un'indicazione di regia: va nelle note |
| nota | 26 · s024 · 35 · s033 | *"Immagine: 3D: un omino dentro una scatola chiusa"* nel corpo | H10 | se è visibile, è un segnaposto a schermo |
| 21 | 89 · r22 | *"la frase che hai scritto **sul figlio**"* | H11, G9 | refuso che rompe il richiamo al foglio (applicata: "sul foglio") |
| 29 | 127 · s152 | *"Un blocco. Uno solo."* due volte di fila | H11 | ripetizione |
| 1 | 1 · s004 e altre | FLAG superate nelle note (*"in 42 giorni"*, *"Build 6 di 6"* su cinque slide) | H10 | *"Chi recita legge le note"* |

**H3 ⛔ non si vede nel testo.** L'audit lo dice in chiaro: *"Non verificabile dall'export: H3 ⛔ (titolo e corpo in un solo blocco di testo), font e tagli delle foto (I12). Serve il controllo a schermo."* Per questo il plugin lo verifica sull'HTML (sotto).

> **Attenzione:** il blueprint chiede **fedeltà totale** sulle slide 1-11 e 70-114 di Grassi, ma alcune di quelle slide violano le regole (S72, S101, S103, S114: B10 ⛔) e l'ordine dell'intro canonico è G3-G11, non quello di Alex. Dal blueprint si prendono struttura, layout e densità (skill `webinar-slide`, "Avvertenza sul blueprint"). Conflitto registrato in `REVISIONE.md` alla radice del repo.

> **Attenzione:** N4 dice *"Meglio molte slide quasi vuote che poche piene"*, mentre H1-H2 vogliono slide dense che contengono lo script (con circa un quarto di slide leggere). Sono entrambe REGOLE, quindi la gerarchia non scioglie la tensione. Nel deck Mind Reset v6, 49 slide su 127 hanno meno di 40 parole di corpo. Nel dubbio, chiedi al senior. Conflitto registrato in `REVISIONE.md` alla radice del repo.

## Gli errori tipici

- **Titolo e corpo spezzati in più caselle** (H3 ⛔), di solito nel giro grafico.
- **Righe "da slide"**, astratte e compresse, che nessuno direbbe a voce (H4).
- **Slide dense che finiscono piatte**, senza gancio (H9).
- **Regia, flag e "Immagine: …" nel corpo** invece che nelle note (H10).
- **Nomi vecchi rimasti** in un'etichetta, in una stack slide, in una FAQ dopo un cambio (H8).
- **Toccare le slide già sistemate dal senior**, o lavorare su una versione vecchia (M6: prima si legge la versione live).

## Nel plugin

- **Skill:** `webinar-slide`. Giro 1: scrivi `DECK_<P>_testo.md` nel formato di `FORMATO_DECK.md` (`### pos · id · Titolo`, corpo, `[immagini: …]`, `> Note:`; parola evidenziata `==così==`; layout esplicito `[layout: …]` facoltativo) → lint → `build_deck.py` → artifact Slides bianco e nero → rework del senior → `export_deck.py` riporta la sua versione nel file testo. Giro 2 (grafica) su un duplicato, copy identico.
- **Cancello 5 · Slide copy:** ⛔ **H3**, F12, B10, M2; decisione 🧑: il rework del senior. **Cancello 6 · Grafica:** ⛔ **H3** (*"il giro grafico non spezza i blocchi di testo"*), L2, L4, M2.
- **Controlli automatici:**
  - `scripts/build_deck.py` genera **un solo `<h2>` e un solo `<p>` per slide**: H3 ⛔ garantita per costruzione;
  - `scripts/export_deck.py --check-h3` conta i blocchi di testo sull'HTML pubblicato ed esce con errore se una slide ne ha più di uno per titolo o per corpo (è l'unico modo di verificare H3);
  - `scripts/lint_deck.py`: slide oltre ~220 parole (H2), regia a schermo (H10), spazi prima della punteggiatura e frasi ripetute di fila (H11), glossario "non si dice" (H8), segnaposto.

---

## Domande di verifica

**1. Nel giro grafico il designer mette ogni paragrafo del corpo in una casella di testo separata "per allinearlo meglio alla foto". Cosa succede e cosa fai?**

<details><summary>Risposta attesa</summary>

È una violazione di H3 ⛔: il corpo deve restare un unico blocco di testo. Blocca i cancelli 6 e 7. Si ripristina un blocco solo; se il testo non entra, si stringe la foto, non il testo (I12). Si verifica con `export_deck.py --check-h3`.
</details>

**2. Dove scrivi "qui mostrare la foto delle sessioni, consenso già raccolto"?**

<details><summary>Risposta attesa</summary>

Nelle note dello speaker (`> Note:`) o nella riga `[immagini: …]`, mai nel corpo (H10, FORMATO_DECK §3). In giro 1 `build_deck.py` mette le immagini nelle note.
</details>

**3. Il senior ha rifatto le prime 30 slide. Qual è il tuo lavoro dopo?**

<details><summary>Risposta attesa</summary>

Leggere la versione live ed esportarla (M6), non toccare le slide che ha sistemato lui, estrarre le sue mosse ricorrenti (tolto, spostato, riformulato) e applicarle al resto del deck (manuale §10, passaggio 5). Se cambia nomi o numeri: prima la scheda, poi tutte le occorrenze nel deck. Poi proporre un audit (M9).
</details>

## Esercizio flash (5-10 minuti)

*Esempio costruito, inventato per l'esercizio: non usarlo fuori dall'Academy.*

Una slide di "Lievita" nel formato del deck testo:

```
### 31 · s031 · La fase di nutrimento del lievito madre nei primi dieci giorni
Nei primi dieci giorni si effettua il processo di rinfresco con cadenza quotidiana, finalizzato all'ottimizzazione della flora batterica.

IMMAGINE: barattolo con il lievito che cresce

Ogni giorno ti mando un video. Nel kit c'è anche il cestino in vimini, valore 40 €, e il gruppo WhatsApp dove Nora risponde entro un'ora.

Così alla fine dei dieci giorni il lievito è pronto.
```

Elenca **tutti** i problemi che trovi, ognuno con il codice della regola (H, G, I…). Poi rispondi: se questa slide fosse costruita con quattro caselle di testo, quale regola ⛔ violerebbe e quale script la troverebbe? Non riscrivere la slide.
