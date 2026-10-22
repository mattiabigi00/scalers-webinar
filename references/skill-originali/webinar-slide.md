---
name: webinar-slide
description: Trasforma lo script di un webinar Scalers in slide (artifact Slides), prima solo copy e poi grafica nel design system del cliente, applicando il rework di Matteo a tutto il deck. Usala quando c'è da fare, sistemare, rifare o impaginare le slide di un webinar Scalers.
---

# Webinar Slide — dallo script al deck

Porti lo script di un webinar Scalers in slide, in due giri separati: **prima il copy, poi la grafica**. Le slide si fanno come artifact di tipo Slides, così Matteo le modifica direttamente.

## Fonti

Sul Mac di Matteo, `~/Desktop/Claude/01_SCALERS/`. Raggiungile con i tool del computer collegato. Leggi per sezioni: i file sopra i 40 KB non si aprono interi.

- `06_OPERATIONS/WEBINAR/BLUEPRINT_SLIDE_WEBINAR.md`: il deck modello (Alex Grassi, 114 slide). Contiene la mappa macro, la densità (§3), le formule slide per slide (§4), i layout, cosa non copiare (§5) e la checklist (§6).
- `06_OPERATIONS/WEBINAR/REGOLE_WEBINAR.md`: soprattutto le aree **H** (copy) e **I** (grafica), più F12, G14 e G15.
- La **scheda di progetto** del webinar in `CLIENTI/<CLIENTE>/…/WEBINAR/`: nomi, numeri, frasi congelate, glossario "si dice / non si dice", promesse piantate, cosa compare solo nello stack. Se non esiste, fermati e proponi di crearla con la skill `webinar-scalers`.
- Il design system del cliente (percorso nella scheda §1).

## Giro 1 · Il copy (slide bianche)

**Obiettivo:** verificare che il passaggio da script a slide sia corretto. Niente estetica: sfondo bianco, testo nero. Le uniche grafiche sono quelle che spiegano un concetto: la metafora del meccanismo, schemi, tabelle, la mappa delle fasi, la stack slide.

1. **Mappa lo script sul blueprint.** Per ogni blocco dello script, scegli la formula e il layout corrispondenti (blueprint §4). Intro e stack seguono il modello fedelmente; Epiphany Bridge e fasi seguono la struttura, con una lunghezza che dipende dal materiale.
2. **Le slide sono lo script** (H1): sulla slide c'è quasi tutto quello che si dice.
   - Densità: slide dense 90-150 parole (massimo ~220 sulle slide chiave).
   - Titoli di 2-5 parole con una parola evidenziata.
   - Circa un quarto delle slide leggere: build, statement, muri di prove.
   - Oltre i 5-6 punti, dividi su due slide (H2).
3. **⛔ Titolo = un unico blocco di testo. Corpo = un unico blocco di testo** (H3).
   - Nel corpo, un solo `<p>`, paragrafi separati da `<br><br>`, elenchi con "• ".
   - La parola evidenziata va dentro lo stesso blocco del titolo, con colore o corsivo. Mai uno sfondo evidenziatore, mai blocchi separati per parola.
   - Matteo modifica il deck a mano: blocchi separati gli fanno perdere ore.
4. **Frasi congelate verbatim** dalla scheda (domino, promessa). Nomi e numeri solo dal glossario della scheda.
5. **Note dello speaker** (`<aside>`), per ogni slide: blocco dello script da cui viene, parlato che non sta a schermo, indicazioni di regia, immagine da mettere, verifiche aperte. **Nella slide non va niente di tutto questo**: niente flag rossi, footer, numeri di blueprint (H10).
6. **Segnaposto dichiarati:** una slide vuota con l'indicazione di cosa va messo, per esempio "[WALL OF LOVE] testimonianze" o "PROOF · clip di 15 secondi". Riportali nella scheda §7.
7. **Export testuale:** salva nella cartella del cliente un `.md` con, per ogni slide, posizione, id, sezione, titolo, corpo e note. Serve a Matteo per rileggere e alla skill `webinar-audit`.
8. Consegna. Poi aspetta il rework di Matteo.

## Il rework di Matteo

Matteo riscrive a mano una parte del deck, direttamente nell'artifact, e spesso ti dà altre istruzioni per trascrizione o documento.

1. **Leggi sempre la versione live prima di toccare qualcosa.** Matteo modifica in diretta.
2. **Non toccare il copy che ha sistemato lui**, salvo che te lo chieda. Se ti dice "fino alla slide 46 è a posto", verifica con un confronto programmatico che dopo il tuo intervento quelle slide siano identiche.
3. **Estrai il modello del suo rework.** Confronta la sua versione con la tua e scrivi le mosse ricorrenti: cosa ha tolto, spostato, allungato, riformulato. Applicale alle slide che non ha toccato.
4. Correzioni che Matteo fa quasi sempre:
   - frasi parlate e chiare a chi arriva nuovo, niente righe "da slide" (H4);
   - coinvolgere senza screditare ("immagina di poterci parlare", non "e quasi ci parli") (H5);
   - togliere le slide di servizio (G10);
   - statement slide per le frasi chiave (H6);
   - non riaprire obiezioni già risolte, neanche nei recap (F12);
   - piantare le sorprese e chiuderle (G14);
   - niente spoiler dello stack (G15);
   - esempi presi dal prodotto reale (D5).
5. Se una sua mossa è nuova e generale, proponi di aggiungerla a `REGOLE_WEBINAR.md` (M10). Se contraddice una regola del cliente, segnalalo in una riga e registra l'override nella scheda.
6. **Nomi e numeri cambiati** (fasi, durata, componenti): aggiorna subito la scheda. Poi cerca le occorrenze vecchie in **tutto** il deck, stack, FAQ e note compresi.

## Giro 2 · La grafica

**Sempre su un duplicato** del deck approvato ("duplica, non modificare questo"). **Il copy resta identico:** alla fine verificalo in modo programmatico, slide per slide.

- **Design system del cliente** (I2): colori, font, componenti dalla cartella del cliente, non inventati.
- **La metafora del meccanismo diventa grafica ricorrente** (I4). Esempi dal caso Mind Reset: l'iceberg 5/95; il palazzo con 21 finestre che si accendono; le due vasche della camera oscura con la sagoma sfocata e poi nitida.
- **Foto del frontman** (I5):
  - passato in polaroid inclinate, con il nastro e toni caldi;
  - presente a tutta altezza su un lato, che sfuma nel fondo;
  - le foto vere sostituiscono le immagini generate con l'AI;
  - non tagliare il volto (niente esagoni che tagliano male).
- **Credenziali a valanga** (I6): una credenziale per slide con la sua prova visiva (fermo immagine TV, copertine, mosaico di palchi con loghi leggibili, foto con personaggi). Se il testo non combacia con le prove, proponi a Matteo di allinearlo.
- **Citazioni di terzi** (I7, I8): una scheda per persona con foto, nome, qualifica, frase e fonte. Va messa dove rinforza l'argomento in corso, mai nei muri di testimonianze. Nelle note scrivi le verifiche (audio da riascoltare, consenso).
- **Lo sfondo non passa mai sotto il testo** (I9). Se un effetto disturba la lettura, spostalo di lato o abbassane l'intensità.
- **Controllo a schermo di ogni slide toccata prima di pubblicare** (I12):
  - testo schiacciato su un lato, sovrapposizioni;
  - corpo sotto i 24 px;
  - foto tagliate male;
  - titoli duplicati.
  Se il testo non entra, stringi la foto, non il testo.
- **Terzi senza consenso in un deck condiviso con link** (L11): fermati prima di pubblicare e chiedi a Matteo l'ok esplicito. Metti le verifiche aperte nelle note.

## Dopo ogni pubblicazione

- Dì a Matteo in poche righe cosa è cambiato, con i numeri di slide. Se la numerazione è scalata, dillo ("lo stack ora parte dalla 80").
- Aggiorna la scheda: versione del deck (§0, §14), decisioni (§12), segnaposto (§7).
- Aggiorna l'export testuale nella cartella del cliente.
- Dopo un rework o un giro grafico importante, proponi di lanciare `webinar-audit`.

## Da non fare

- Cambiare il copy durante il giro grafico.
- Toccare slide già sistemate da Matteo senza che lo chieda.
- Copiare dal deck di Alex la scarsità finta ("ultimi 50 posti") o lo sconto in percentuale (B10).
- Pubblicare senza aver letto la versione live.
