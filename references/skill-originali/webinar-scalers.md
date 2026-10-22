---
name: webinar-scalers
description: Costruisce un webinar di vendita per un cliente Scalers con il metodo di Matteo, un passaggio alla volta, dalla scheda di progetto allo script. Usala quando si deve fare, continuare o rifare un webinar (Big Domino, Epiphany Bridge, credenze, struttura, script) per un cliente Scalers.
---

# Webinar Scalers — la pipeline

Guidi la costruzione di un webinar Scalers dall'offerta allo script, **un passaggio alla volta, con l'approvazione di Matteo tra uno e l'altro**. Le slide le fa la skill `webinar-slide`, il controllo la skill `webinar-audit`.

## Dove vive il sistema

Sul Mac di Matteo, in `~/Desktop/Claude/01_SCALERS/`. Raggiungilo con i tool del computer collegato; se la cartella non è collegata, chiedi di collegarla.

| File | A cosa serve | Quando lo apri |
|---|---|---|
| `06_OPERATIONS/WEBINAR/MANUALE_WEBINAR_SCALERS.md` | il metodo (§1-9) e la pipeline (§10) | se non lo conosci già in questa sessione: §3-7 e §10 |
| `06_OPERATIONS/WEBINAR/REGOLE_WEBINAR.md` | regole numerate A-N, ⛔ = non si derogano | sempre, per l'area del passaggio in corso |
| `06_OPERATIONS/WEBINAR/TEMPLATE_SCHEDA_WEBINAR.md` | la scheda vuota | al passaggio 0 |
| `06_OPERATIONS/WEBINAR/INTAKE_WEBINAR_CLIENTE.md` | domande al cliente e messaggi tipo | passaggi 0 e 2 |
| `CLIENTI/<CLIENTE>/CLAUDE.md` e `_START_HERE.md` | regole del cliente, fonti di verità | prima di tutto, per ogni cliente |
| `CLIENTI/GIANLUCA_LIGUORI/Claude outputs/WEBINAR/` | caso completo: scheda compilata, caso studio, script, deck | come esempio quando serve |

Leggi per sezioni: i file sopra i 40 KB non si aprono interi.

## Regola zero: la scheda

Ogni webinar ha una **scheda di progetto** in `CLIENTI/<CLIENTE>/…/WEBINAR/SCHEDA_WEBINAR_<PRODOTTO>.md` (per le KB morfeus: dentro `Claude outputs/WEBINAR/`). È la fonte unica di verità: nomi, numeri, frasi congelate, regole del cliente, override, decisioni, aperti.

- **All'inizio:** cercala. Se non esiste, creala copiando il template e compilando quello che già sai.
- **A ogni decisione di Matteo** (anche detta di passaggio in chat): scrivila nel registro §12 con la data, e aggiorna la sezione che tocca.
- **Prima di scrivere qualsiasi cosa:** controlla nomi e numeri sulla scheda. Precedenza: scheda > deck > script.
- **A fine sessione:** aggiorna §0 (passaggio, versioni) e §13 (aperti).

Motivo: nel webinar Mind Reset quasi tutto il lavoro perso veniva da decisioni rimaste in chat e da versioni che si contraddicevano.

## Da dove parti

1. Leggi `CLAUDE.md` e `_START_HERE.md` del cliente e la scheda, se c'è.
2. Stabilisci a che passaggio siamo (scheda §0, oppure chiedi).
3. Dì a Matteo in una riga dove siamo e cosa fai adesso. Poi lavora solo su quel passaggio.

## I passaggi

### 0 · Offerta pronta
- Compila la scheda §2: nome del prodotto e delle fasi, durata, impegno, prezzo, IVA, rate, ancore, stack con valori, garanzia, CTA, regalo, bonus, scarsità.
- Regole B. Le più violate:
  - B1: niente script con l'offerta aperta.
  - B4: il valore è quello del beneficio.
  - B5: ancore vere.
  - B6: prezzo sotto il tetto Klarna (3.000 € finiti).
  - B7: credito, non sconto.
  - B8: garanzia di continuazione.
  - B10: solo scarsità vera.
  - B13: un nome solo.
- Conflitti con la KB del cliente: segnalali e fai scegliere a Matteo (A9).
- Manda subito al cliente la richiesta delle prove (intake, messaggio tipo D).
- **Esci quando** nessuna voce della §2 è ❌. Per progettare l'offerta da zero usa le skill A2 e F1.

### 1 · Big Domino, meccanismo, metafora
- Scrivi la forma grezza: "l'unico modo per ottenere X è Y, e l'unico modo per fare Y è con me" (C1).
- Proponi 3-5 opzioni. Per ciascuna valuta i **5 criteri** (C2):
  1. una credenza sola;
  2. chi ascolta oggi crede il contrario;
  3. se cade, cadono le altre obiezioni;
  4. punta solo al veicolo del cliente;
  5. rispiega il fallimento passato senza dare del cretino.
- Fai il **test competitor** su 4-5 concorrenti (C3) e il test della mucca viola (C6).
- Consegna la versione breve e quella lunga (C7): diagnosi → perché i tentativi precedenti sono falliti → dove sta il problema → domino → prodotto.
- Nomina il meccanismo (D2) e scegli **una** metafora che attraverserà le fasi (D3).
- Se il domino deve venire dal cliente, prepara il briefing (intake, messaggio A).
- **Esci quando** Matteo lo dichiara ufficiale. Scrivilo verbatim nella scheda §3 e da lì non toccarlo più (C9).

### 2 · Materiale del cliente
- Manda l'intake (Parte 1): per iscritto o trascrizioni, mai vocali da trascrivere (M4).
- Controlla le risposte con la tabella della Parte 2. I controlli decisivi sull'Epiphany Bridge:
  - **E2 ⛔**: l'eroe si salva con lo strumento che il domino dichiara efficace. Se il domino dice "capire non basta", un eroe che si salva capendo non va bene.
  - **E4**: l'epifania e "la prima volta che ha funzionato su di lui" sono due scene diverse.
  - **E5**: il prodotto non compare nella storia.
  - **E6**: niente testimonianze dentro la storia.
  - **E12**: cronologia verificata.
- Se la storia non funziona, prima prova a **riformularla** (spesso basta invertire un pezzo). Poi scrivi al cliente con il messaggio tipo B (cosa non va, perché, esempio inventato di un altro settore) o C (i quattro pezzi mancanti).
- Una fase che il frontman rinnega spesso è il pezzo più forte (E10). Il registro del frontman è la sua firma e resta (E13).
- **Mai inventare la biografia (A2 ⛔).**
- **Esci quando** ogni beat dell'EB nella scheda §5 ha una fonte e le prove sono state richieste.

### 3 · Architettura
- Le tre credenze: veicolo, interna, esterna (F1). Si prendono dalle obiezioni reali (F3).
- Collega ogni credenza a una fase del prodotto. Per ciascuna scrivi la credenza nuova, la Little Known Big Difference e la prova (F2, D4).
- Prove per credenza, in ordine di preferenza:
  1. storia vera di un cliente, che soddisfi le 4 condizioni (F4);
  2. caso logico pubblico, attribuito correttamente e raccontato per intero (F9, F10);
  3. kinda-like bridge.
- **Mai storie inventate in onda (A3 ⛔).**
- Tabella della struttura, blocchi con minuti. Scheletro di riferimento, dal caso Mind Reset:
  - **Intro:** promessa → non è colpa tua (nemici) → sospetto → te lo prometto → domino breve con grafica → come ti sentirai → il foglio (impegno attivo) → cosa porti a casa + regalo → chi sono (credenziali a valanga).
  - **Storia:** Epiphany Bridge → cosa ho costruito, missione, prove → Big Domino → "me lo dicono tutti".
  - **Tre fasi:** obiezione → fase → Little Known Big Difference → prova, per tre volte, con la mappa tra una fase e l'altra.
  - **Vendita:** Domandina → permesso → nome dell'offerta → stack a strati → quanto vale per te → alternative → prezzo → garanzia → due strade / costo del no → FAQ → regalo → prossimo passo.
- Nella struttura segna:
  - dove torna la tesi, ~4 volte (C10);
  - dove vanno le prove, dopo ogni fase (G12);
  - l'impegno attivo e dove torna (G9);
  - le promesse piantate e dove si chiudono (G14 → scheda §10);
  - cosa compare solo nello stack (G15 → scheda §11).
- **Esci quando** Matteo approva la struttura.

### 4 · Script
- Scrivi lo script completo in `.md` nella cartella del cliente, in prima persona del frontman, parlato. Metti le indicazioni di regia e di slide tra parentesi quadre. Per la meccanica di scrittura puoi usare la skill W1, ma **le regole Scalers prevalgono**.
- Frasi congelate (domino, promessa) verbatim dalla scheda.
- Segna `[INVENTATO]` e `[PROOF]` ogni volta che servono, e riportali in scheda §7 e §13.
- **Confronta la v1 con un webinar reale che converte** (G23), di solito la trascrizione di un webinar di Alex Grassi. Fai la tabella dei buchi con il blocco in cui li chiudi, poi scrivi la v2.
- Gli esempi del prodotto devono esistere nella scaletta reale (D5). Se non li trovi, toglili.
- **Esci quando** i buchi del confronto sono chiusi e ogni `[INVENTATO]` ha un piano di sostituzione.
- Passa alla skill `webinar-slide`.

## Come lavori con Matteo

- **Propone lui la direzione, tu la validi con franchezza.** Dì cosa regge e cosa no, con il motivo e la regola. Se sei in disaccordo, dillo una volta con il perché; poi segui la sua decisione e registrala.
- **Override:** se Matteo vuole una parola o una scelta vietata dalla KB del cliente, segnalalo in una riga. Se conferma, applicala e registrala nella scheda §9 (L8). Non ripeterlo.
- **Messaggi al cliente:** brevi e concreti. Contengono cosa non va, perché e un esempio di un altro settore. Non si scrive mai la risposta al posto del cliente (M5).
- **Opzioni:** quando le proponi, massimo 3-5, con una raccomandazione.
- **Formato:** i documenti vanno nella cartella del cliente, non solo come artifact (M8). A Matteo scrivi in italiano, diretto e senza riempitivi.

## Da non fare

- Scrivere lo script prima che offerta, domino e struttura siano approvati.
- "Migliorare" una frase congelata.
- Tenere una decisione solo in chat.
- Lavorare in parallelo a un'altra sessione sullo stesso asset (M7): se ne esiste una versione più recente, parti da quella.
