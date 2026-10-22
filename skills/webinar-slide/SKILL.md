---
name: webinar-slide
description: Trasforma lo script di un webinar Scalers nel deck - prima il copy su slide bianche, poi la grafica nel design system del cliente - come artifact Slides, con il deck testo come fonte e gli script che garantiscono un blocco di testo per titolo e corpo. Usala quando il copy dice "facciamo le slide", "passa lo script in slide", "costruisci il deck", "aggiorna il deck", "il senior ha fatto il rework", "applica le correzioni a tutto il deck", "facciamo la grafica del webinar", "esporta il deck".
---

# Webinar Scalers · dallo script al deck

Due giri separati: **prima il copy, poi la grafica** (I1). Il deck è un **artifact Slides**, così il senior lo modifica direttamente. La fonte del copy è il file `DECK_<P>_testo.md` nel formato `R/references/FORMATO_DECK.md`: da lì si costruisce l'artifact, e lì si torna dopo ogni rework.

`R/` = radice del plugin. Leggi: `R/references/BLUEPRINT_SLIDE_WEBINAR.md` (§1 mappa, §3 densità, §4 formule slide per slide, §5 cosa non copiare, §6 checklist); `R/references/REGOLE_WEBINAR.md` aree **H** e **I**, più **F12, G14, G15, B10**; la scheda (glossario §9, promesse piantate §10, solo-stack §11). Se la scheda non c'è, fermati.

**Avvertenza sul blueprint.** Il blueprint chiede fedeltà totale su intro (1-11) e stack (70-114) del deck di Alex. Quella fedeltà vale per **struttura, layout e densità**, non per le slide che violano le regole: S72, S101, S103, S114 (scarsità "ultima volta / ultimi 50 posti", sconto -90%) e le "ciliegine" bonus prima del prezzo. Vincono le REGOLE (B10 ⛔, B11). L'ordine dell'intro segue G3-G11 (vedi `webinar-script`).

## Giro 1 · il copy (slide bianche)

1. **Scrivi `DECK_<P>_testo.md`** mappando ogni blocco dello script sulla formula e sul layout del blueprint §4. Le slide sono lo script (H1): sulla slide c'è quasi tutto quello che si dice.
   - Densità: slide dense 90-150 parole (max ~220 solo sulle slide chiave), titoli di 2-5 parole con **una** parola evidenziata `==così==`, circa un quarto di slide leggere (build, statement, muri di prove); oltre i 5-6 punti si divide (H2).
   - Ogni slide densa chiude con un **gancio** verso la successiva (H9). Statement slide per le frasi chiave (H6). Grassetto sulla frase che conta (H7).
   - Frasi congelate e nomi **verbatim** dalla scheda (M2 ⛔, H8). Stack slide ripetute **identiche** salvo le aggiunte.
   - Regia, immagini, verifiche: nelle `> Note:`, mai nel corpo (H10). Segnaposto dichiarati nel corpo: `[PROOF: …]`, `[DA CLIENTE: …]`.
   - Id delle slide stabili e leggibili (`intro-promessa`, `eb-garage`, `stack-3`…), non numeri.
2. **Lint:** `python3 R/scripts/lint_deck.py DECK_<P>_testo.md --scheda <scheda> --out LINT_<P>.md`. Chiudi le ⛔ e le alte prima di costruire.
3. **Costruisci:** `python3 R/scripts/build_deck.py DECK_<P>_testo.md --out <cartella WEBINAR>/deck`. Genera `deck/project/deck.json` e `deck/project/slides/<id>.html`: sfondo chiaro, testo nero, **un `<h2>` e al più un `<p>` per slide** (H3 ⛔ garantita per costruzione), note in `<aside>` (lì finiscono anche layout e immagini). Stack slide scritte con la sintassi di `FORMATO_DECK.md` §1, così il lint ne controlla somme e ripetizioni.
4. **Pubblica** come artifact Slides:
   - la prima volta: crea l'artifact dal tipo Slides (`type_url` del tipo Slides nella lista dei tipi, `title` = "Webinar <Prodotto> — v1 copy"), poi pubblica i file generati su quel `url` con `root` = `<cartella WEBINAR>/deck` (file `project/deck.json` più tutti `project/slides/*.html`);
   - le volte dopo: stesso `url`, prima **rileggi la versione live** (M6).
   - Segui le istruzioni che il tipo Slides restituisce alla creazione (sono il contratto del formato). Niente design system in giro 1: bianco e nero.
5. **Scheda:** link e versione dell'artifact in §0 e §14, segnaposto in §7. Se nel deck ci sono terzi con consenso ❌, il link resta nel team finché il senior non dà l'ok (L4 ⛔, L11). Riga "Cancello 5a chiuso". Consegna al senior con una riga su cosa guardare: il rework è il 5b.

## Il rework del senior

Il senior riscrive a mano una parte del deck direttamente nell'artifact.
1. **Leggi sempre la versione live prima di toccare qualcosa** (M6): leggi `project/deck.json` e le slide dall'artifact, poi `python3 R/scripts/export_deck.py <cartella letta> --url <link> --versione <id> --out DECK_<P>_testo.md --check-h3`. Il file testo ora è la versione del senior.
2. **Non toccare il copy che ha sistemato lui**, salvo richiesta. Se dice "fino alla slide 46 è a posto", dopo il tuo intervento verifica con un diff sull'export che quelle slide siano identiche.
3. **Estrai il modello del suo rework**: confronta la sua versione con la tua e scrivi le mosse ricorrenti (tolto, spostato, allungato, riformulato). Applicale alle slide che non ha toccato. Correzioni che tornano quasi sempre: registro parlato (H4), coinvolgere senza screditare (H5), via le slide di servizio (G10), statement per le frasi chiave (H6), nessuna obiezione riaperta nei recap (F12 ⛔), piantare e chiudere (G14), niente spoiler dello stack (G15), esempi dal prodotto reale (D5).
4. Una mossa nuova e generale: **proponi** di aggiungerla a `REGOLE_WEBINAR.md` (M10). Non modificare le regole.
5. **Nomi e numeri cambiati**: aggiorna subito la scheda (e il registro), poi cerca le occorrenze vecchie in **tutto** il deck, stack, FAQ e note comprese.
6. Ricostruisci (`build_deck.py --update deck/project/deck.json`) solo le slide che cambi e ripubblica **solo quelle** più l'indice se cambia.

## Giro 2 · la grafica

**Sempre su un duplicato** del deck approvato: nuovo artifact Slides "Webinar <Prodotto> — v<N> grafica", stessi file di partenza. **Il copy resta identico**: alla fine esporta e fai il diff slide per slide con il deck approvato.

- **Design system del cliente** (I2): colori, font, componenti dalla cartella del cliente (scheda §1) o dal design system del cliente tra quelli disponibili. Non inventato.
- **La metafora del meccanismo diventa grafica ricorrente** (I4). Esempi Mind Reset: l'iceberg 5/95, il palazzo con 21 finestre che si accendono, le due vasche della camera oscura.
- **Foto del frontman** (I5): il passato in polaroid inclinate con il nastro, il presente a tutta altezza su un lato; le foto vere sostituiscono le immagini generate. Carica i file come asset dell'artifact.
- **Credenziali a valanga** (I6): una credenziale per slide con la sua prova; se il testo non combacia con le prove, proponi al senior di allinearlo.
- **Citazioni di terzi** (I7, I8): una scheda per persona, mai nei muri di testimonianze. Nelle note: consenso e audio riascoltato.
- **Lo sfondo non passa sotto il testo** (I9). Slide-colpo nude, animazioni solo fade (I10).
- **H3 ⛔ resta**: titolo e corpo restano un blocco ciascuno anche con la grafica. Dopo il giro: `export_deck.py … --check-h3`, zero violazioni.
- **Controllo a schermo di ogni slide toccata** (I12): testo schiacciato, corpo sotto i 24 px, foto tagliate male, titoli duplicati. Se il testo non entra, stringi la foto, non il testo.
- **Terzi senza consenso in un deck condiviso con link** (L4 ⛔, L11): fermati prima di pubblicare e chiedi l'ok esplicito del senior; verifiche aperte nelle note.

## Dopo ogni pubblicazione

- Al senior: poche righe su cosa è cambiato, con i numeri di slide (e se la numerazione è scalata).
- Scheda: versione del deck (§0, §14), decisioni (§12), segnaposto (§7).
- Export testuale aggiornato nella cartella del cliente.
- Dopo un rework o un giro grafico importante: proponi `/webinar-audit` (M9).

## Da non fare

- Cambiare il copy durante il giro grafico.
- Toccare slide già sistemate dal senior senza che lo chieda.
- Pubblicare senza aver letto la versione live.
- Spezzare titolo o corpo in più blocchi di testo (H3 ⛔).
- Copiare la scarsità finta o lo sconto in percentuale dal deck di Alex (B10 ⛔).
