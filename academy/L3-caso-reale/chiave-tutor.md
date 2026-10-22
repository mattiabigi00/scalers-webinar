# L3 · Chiave del tutor · Mind Reset

> **Cos'è:** SOLO PER IL TUTOR E IL SENIOR. Le 30 righe dell'audit reale del deck v6 con lo stato nel deck di `examples/`, i criteri per contare corrispondenze e falsi positivi, le 9 domande dell'audit, i punti di confronto e gli errori attesi del compito 1.
> **Durata:** si consulta durante i compiti 1-3 (circa 40 minuti di lavoro del tutor per copy).
> **Prerequisiti:** `L3-caso-reale/README.md`, `examples/mind-reset/AUDIT_DECK_V6_2026-09-30.md`, `examples/mind-reset/SCHEDA_WEBINAR_MIND_RESET.md`.

---

**Non mostrarla, non citarla, non parafrasarla al copy** (skill `webinar-tutor`). Al copy dai solo i tre numeri (trovate, ⛔, falsi positivi) prima che apra l'audit reale.

## 0 · Prima del compito 2: la scheda da dare al copy

La scheda di `examples/` è stata compilata il 30/9 **dopo** l'audit, e in tre punti ne riassume i risultati. Prima di darla al copy, prepara una copia in `ACADEMY_<nome>/L3/SCHEDA_MIND_RESET_per_audit.md` e togli solo:

1. **§13, riga 11** ("Audit del 30/9: 30 correzioni e 9 domande…"): elenca le righe 3, 16, 20 e il "guarire oltre l'override".
2. **§14, riga "Audit deck v6"** (dà il numero delle correzioni).
3. **§6, riga "Esterna", colonna "Prova"**: la frase "; il deck (r21) la attribuisce a Hans Selye → da allineare (aperto 11)". L'audit reale (riga 20) dice che la scheda riportava solo Tony Robbins: togliendola torni alla scheda che l'auditor aveva.

Tutto il resto resta com'è. Alcune voci aiutano il copy e **sono legittime**, perché le aveva anche l'auditor: gli aperti §13 n. 4 (consensi → riga 30), n. 5-6 (cronologia e libri → righe 9 e 15), n. 8 ("tre passaggi" → riga 7), n. 10 (ancora 10.000 €), e il registro §12 del 30/9 che elenca le 4 correzioni già applicate.

## 1 · Le 30 righe dell'audit e il loro stato nel deck

Deck controllato: `examples/mind-reset/Webinar_Mind_Reset_Deck_v6_testo.md`, **versione 1790783640-9275**, cioè dopo le 4 correzioni applicate il 30/9 (righe 12, 21, 23, 26). L'audit reale era stato fatto sulla versione precedente (1790774429-643f).

Legenda stato: **✅ ancora presente e trovabile** · **❌ già corretta nel deck: non si può trovare**. "Riga file" = numero di riga nel file del deck dove si vede il problema.

| # | Slide | Problema in breve | Regola | Gravità | Stato | Riga file | Basta per la corrispondenza |
|---|---|---|---|---|---|---|---|
| 1 | 1 · s004 (+ note di s047, s053, s123, s124, s129, Domandina) | note superate che chi recita legge: FLAG "in 42 giorni" in s004, mentorship dal 2019, "il Reset", cue "Ti prepari" / "La fissi", "Build 6 di 6" su 5 slide | H10, A7 | bassa | ✅ | 9, 512, 538, 997, 1006, 1057, 919-955 | almeno una delle note superate elencate (la più probabile: la FLAG dei 42 giorni). La nota su Marco è la riga 11 |
| 2 | 4 · s009 | "dati, esempi e un'infinità di testimonianze": le prove sono tutte segnaposto e "dati" nel deck non ce ne sono; la scheda §4 dice "dati, esempi e testimonianze" | G14, G6, L1 | alta | ✅ | 48 | la promessa di prova di s009 non mantenuta, oppure "un'infinità di" che non è in scheda |
| 3 | 6 · 7b1388dd e 54 · s052 | domino breve non identico: "E non puoi…" contro "Perché non puoi…" | C9, C10 | **⛔** | ✅ | 58, 523 | la differenza tra le due slide del domino breve |
| 4 | 7 · 3405b995 (+ r01, r15, r20, r21d, s131, s145) | spazi prima della punteggiatura nei titoli | H11 | bassa | ✅ | 68, 554, 810, 848, 897, 1088, 1315 | almeno un titolo con lo spazio |
| 5 | 8 · s011 | "Sei **paziente**": parola vietata dal cliente | L8, R2 | bassa | ✅ | 76 | "paziente" in s011 |
| 6 | 9 · s011b | "lievi gibbosità": non è parlato | H4 | bassa | ✅ | 87 | la frase, come non parlata |
| 7 | 13 · s017 | "I tre **passaggi**": il glossario dice "le tre fasi" (aperto §13 n. 8) | A6, H8, B13 | alta | ✅ | 137 | "passaggi" in s017 |
| 8 | 18 · s021b | foto con Bonolis nella slide TV (è un incontro); "MTV America" non è in scheda | L6, A4 | bassa | ✅ | 168, 170 | Bonolis presentato come TV, oppure "MTV America" da verificare |
| 9 | 20 · s021d | Tiffany, Rolex, Porsche, Amazon senza prova visiva; formula "Parlamento Europeo" aperta | I6, A4 | bassa | ✅ | 192 | aziende senza foto, oppure la formula del Parlamento Europeo |
| 10 | 21 · s021e | foto con Roberto Carlos sopra "Con me lavorano…": sembra un cliente, in scheda è un incontro | L6 | alta | ✅ | 197-199 | Roberto Carlos che si legge come cliente |
| 11 | 37 · s035 | nota "Tornerà nella storia di Marco": Marco è stato tolto il 25/9 | F13 | bassa | ✅ | 361 | Marco ancora citato, anche solo in nota |
| 12 | 48 · s045 | "Mind Reset Coaching" dentro la storia; refuso "nefaccio" | E5, B13, H8, R4, H11 | alta | **❌** corretta 30/9 | 466 (ora "le mie coaching") | — |
| 13 | 49 · 259955d3 | etichetta della grafica "La sessione" | A6, H8 | alta | ✅ | 488 | l'etichetta "La sessione" nella striscia |
| 14 | 49 · 259955d3 | "ti hanno reso effetto", "cementificare": frasi da brochure | H4 | bassa | ✅ | 478, 482 | una delle due frasi |
| 15 | 52 · s047 (con s021, s044) | anni di studio che non tornano: "oltre vent'anni", "più di quindici anni", "15 anni" | A6, E12 | alta | ✅ | 159, 451, 506 | almeno due dei tre numeri messi a confronto |
| 16 | 53 · s051 | il domino lungo congelato il 23/9 non è nel deck; cerniera diversa dalla scheda | C9, M2 ⛔ | **⛔** | ✅ | 514-518 ("Da bambino hai iniziato" non compare in tutto il file) | il domino lungo di §3 manca o è diverso nel deck |
| 17 | 62 · r04 | "mettiamo in ordine" in Fase 1: è il lavoro della Fase 2 (contraddice s060, s095) | D3 | alta | ✅ | 627 | la Fase 1 che fa il lavoro della Fase 2 |
| 18 | 64 · r05 | "aiutato a **guarire**": l'override vale solo per promessa e sogno | L8, L9 | alta | ✅ | 643 | "guarire" in r05 fuori dall'override |
| 19 | 74 · r13w (con r13, r16) | "centinaia di testimonianze", "Tutte le persone che stai per vedere": seguono 4 slide vuote | G14, L1, L2 ⛔ | alta | ✅ | 767, 772, 827, 834-843 | la promessa di r13/r16 seguita dai segnaposto vuoti |
| 20 | 83 · r21 | storia attribuita a Hans Selye; scheda §6 e nota dicono Tony Robbins | F10, A1 | alta | ✅ | 857 | l'attribuzione diversa dalla scheda |
| 21 | 89 · r22 | "sul **figlio**" invece di "sul foglio" | H11, G9 | alta | **❌** corretta 30/9 | 907 (ora "sul foglio") | — |
| 22 | 92-95 · Domandina | "e **guarirlo**": override non previsto qui | L8, L9 | alta | ✅ | 924, 930, 938, 948 | "guarirlo" nella Domandina |
| 23 | 98 · s123 | "Lo stesso percorso che faccio **dal vivo**" | R3, R4, H8 | alta | **❌** corretta 30/9 | 978 (ora "Il mio metodo, a casa tua…") | — |
| 24 | 112 · s137 | etichetta "Sessione" nella grafica della garanzia | H8 | bassa | ✅ | 1214 | l'etichetta in s137 |
| 25 | 116 · s141 | "quel blocco si muove solo un po'… E hai diritto a un altro giro": la garanzia vale se il blocco "è ancora lì" | B8, G20 | alta | ✅ | 1282 | il "metti caso" che promette più della garanzia |
| 26 | 122 · s147 | FAQ "non te lo vendiamo" contro il rimborso previsto dalla KB | G20, B10 | alta | **❌** corretta 30/9 | 1336 (ora "ti restituiamo…") | — |
| 27 | 125-126 · s150 / s151 | "prenotare **subito**" contro "calendario del mese successivo" | A6 | bassa | ✅ | 1365, 1371 | la contraddizione subito / mese dopo |
| 28 | 126 · s151 | regia a schermo "Da mostrare vero: niente countdown, niente 'ultimi posti'"; e "ultimi posti" è vietato | H10, L8 | alta | ✅ | 1377 | la riga di regia nel corpo |
| 29 | 127 · s152 | "Un blocco. Uno solo." due volte di fila | H11 | bassa | ✅ | 1401, 1403 | la ripetizione |
| 30 | 47, 50, 56, 63, 69, 76 (citazioni) + 22 · s021f + 18, 21 (foto) | consensi dei terzi ❌ e audio non riascoltato per le 6 citazioni; Vernetti e Maniscalco senza ok; foto con Amadeus, Bonolis, Roberto Carlos | L4 ⛔ | **⛔** | ✅ | 459, 493, 540, 633, 702, 802, 203 · scheda §8 | terzi senza consenso o audio non riascoltato (bastano le citazioni, anche in una riga sola) |

**Base del compito 2: 26 righe** (30 meno le 4 corrette). Di queste: **⛔ 3** (righe 3, 16, 30) · **alta 12** (2, 7, 10, 13, 15, 17, 18, 19, 20, 22, 25, 28) · **bassa 11** (1, 4, 5, 6, 8, 9, 11, 14, 24, 27, 29).

**Soglia:** almeno **15 su 26**, comprese **tutte e tre le ⛔**, con **al massimo 5 falsi positivi**.

### Verifica fatta sul deck

Il 30/9/2026 ho cercato nel file del deck il testo citato da ogni riga (versione 1790783640-9275, 127 slide). Esito:
- **tutte le 26 righe ✅ sono presenti** e trovabili, alle righe del file indicate in tabella;
- **le righe 12, 21, 23, 26 sono davvero corrette**: "Mind Reset Coaching", "nefaccio", "sul figlio", "faccio dal vivo" e "non te lo vendiamo" non compaiono nel corpo di nessuna slide;
- **riga 16** è un'assenza: il problema c'è perché il testo congelato manca. Del domino lungo della scheda §3 compaiono nel deck solo le frasi finali ("Cambiarla si può", "Ma non decidendolo, e non capendolo", "…scritta nel tuo inconscio, ed è lì che va riscritta", la riga del 5/95 e "Ed è esattamente quello che fa Mind Reset"); tutta la parte da "Da bambino hai iniziato…" a "…chi saresti senza" non c'è, e manca "quell'immagine non è scritta dove pensi";
- **riga 26**: il corpo è corretto, ma la nota di s147 conserva la FLAG "'Non te lo vendiamo' va allineato" (riga 1339 del file). È una nota superata nuova: se il copy la trova vale come segnalazione valida in più (tipo riga 1), non come riga 26.

## 2 · Le tre ⛔

| Riga | Cosa | Perché è ⛔ |
|---|---|---|
| **3** | domino breve diverso tra s006 e s052 | per la regola di gravità dell'auditor (`agents/auditor.md` §3: "cambia una frase congelata"). C9 e C10 non sono ⛔ in `REGOLE_WEBINAR.md`; la ⛔ sottostante è **M2** (script e slide si allineano alla scheda) |
| **16** | domino lungo congelato assente nel deck | frase congelata non verbatim: C9, **M2 ⛔** |
| **30** | terzi senza consenso, audio non riascoltato | **L4 ⛔**: blocca la registrazione |

Se il copy trova una di queste ma le dà una gravità più bassa, **conta come trovata**. In discussione chiedi: "Che gravità dà l'auditor a una frase congelata che cambia? E a un terzo senza consenso?" (`agents/auditor.md` §3).

## 3 · Come si conta

### Corrispondenza

Una riga del copy **corrisponde** a una riga dell'audit se parla **della stessa slide (o dello stesso gruppo di slide) e dello stesso problema**, anche con parole diverse, un'altra regola citata o un'altra gravità. In più:
- una riga del copy che copre più righe dell'audit (es. "guarire fuori dall'override in r05 e nella Domandina") vale per **ognuna** di quelle che nomina in modo concreto (qui 18 e 22);
- una riga generica senza slide ("le prove sono tutte vuote") vale **al massimo per una** riga dell'audit, quella più vicina; chiedi al copy dove l'ha vista;
- un problema messo tra le **domande** invece che in tabella conta se è lo stesso problema (es. "domino lungo: vale la scheda o il deck?" → riga 16; l'audit reale l'ha messo in entrambe);
- l'elenco dei **segnaposto** non conta come correzione, salvo quando il copy lo collega a una promessa fatta (righe 2 e 19);
- le 4 righe corrette (12, 21, 23, 26) **non si possono trovare**: se il copy le segnala come presenti, è un falso positivo.

### Falsi positivi

Una segnalazione è un **falso positivo** se:
1. contraddice una **decisione registrata** nel registro della scheda (§12), oppure
2. contraddice un **override** della scheda (§9), oppure
3. **non viola nessuna regola** (gusto personale, "titolo poco incisivo", proposte di stile su frasi congelate: `agents/auditor.md`, "Da non fare").

I falsi positivi più probabili:

| Segnalazione del copy | Perché è falso positivo | Fonte |
|---|---|---|
| "guarire le ferite" in s004 (promessa) o "Guarisci le ferite" in s011 (sogno) | override di Matteo del 25/9 per promessa e sogno | scheda §9 |
| "sbloccare il tuo massimo potenziale" in s004 | override del 24/9 | scheda §9 |
| il 95/5 o "cambiare la tua vita" nel domino (L8, A1) | override del 23/9, compliance gestita da Matteo | scheda §3 e §9 |
| il registro esoterico (432 Hz, voce sovrana) nella storia | override del 23/9, "è la firma di Gianluca" | scheda §9, regola E13 |
| la stack ripetuta dopo la garanzia (s139) | decisione del 30/9 | scheda §12 |
| la camera oscura nella Fase 3, "manca il palazzo in Fase 3" | decisione del 25/9; D3 ammette una seconda metafora se prende una fase intera | scheda §3, regola D3 |
| valori dello stack "gonfiati" o B4 generico sullo stack | decisione del 23/9 confermata il 30/9 ("i valori in stack lasciali così"); in s124, s127, s129 ogni valore ha la sua frase-beneficio | scheda §2 e §12 |
| l'ancora da 10.000 € come correzione del deck | è una decisione 🟡 con conflitto aperto in scheda (§13 n. 10): come domanda o aperto va bene, come errore del deck no | scheda §2, §13 |
| "medico" nelle qualifiche (s021f, citazioni), "terapeutico" nel disclaimer di s017, "segreto" nel racconto di s022, "Paolo" (Bonolis) come storia tolta, "dal vivo" in s046, s055, s132, s133, "21 giorni" per una fase | nessuna regola violata: la lista vieta "medico (come promessa)" e "segreto" come claim; il disclaimer c'è apposta; Paolo tolto è un'altra persona; "dal vivo" è vietato solo per la sessione registrata; "21 giorni" solo come durata totale. Sono le righe "verifica" del lint | scheda §9 |
| il domino mostrato prima della storia (s005-s007) | lo chiede C10 | regola C10 |
| WhatsApp nominato nella garanzia (s137) | la garanzia viene dopo lo stack: G15 è rispettata | scheda §11 |
| "H3 violata" detto come fatto | dall'export non si verifica (`agents/auditor.md`, controllo 16). "H3 non verificabile" va bene | FORMATO_DECK §4 |

**Il dubbio sul 95/5.** Se il copy lo segnala come domanda ("è un dato non dimostrato: A1 ⛔ non si deroga, come fa a esserci un override?"), **non è un falso positivo**: è una buona domanda. Attenzione: il conflitto tra A1 ⛔ non derogabile e l'override registrato sul 95/5 (e la frase di `CANCELLI.md` passaggio 1 "se un dato è discutibile ma il senior lo tiene, override registrato") è una contraddizione delle fonti (conflitto registrato in REVISIONE.md alla radice del repo). Discutila, non risolverla.

### Né corrispondenza né falso positivo

Queste non contano e non tolgono. Riconosci il merito in discussione.

**Segnalazioni valide che l'audit reale non ha in tabella:**
- "Immagine: 3D…" nel corpo di s024 e s033 (H10): l'audit la mette in una nota sotto la tabella e tra i segnaposto;
- "Immagine: 2-3 foto…" nel corpo di r08 e "Immagine: QR…" in s148 (H10): l'audit le mette tra i segnaposto;
- la FLAG superata nella nota di s147 (vedi "Verifica fatta sul deck");
- manca la battuta prima del permesso (G16): la nota di s122 spiega la scelta ("non è nella voce di Gianluca"), ma non è registrata in §12. Buon tema di discussione.

**Le 9 domande dell'audit reale.** Se il copy ne fa una, è una domanda buona:

| # | Domanda dell'audit | Stato nella scheda di oggi |
|---|---|---|
| 1 | Domino lungo: vale quello congelato o quello del deck? (è anche la riga 16) | aperta |
| 2 | "Guarire" in r10 (e in r05, Domandina): si aggiunge al registro o si toglie? | aperta |
| 3 | s127 "La mia voce, la stessa sessione che faccio a casa mia": ripresa di un'obiezione vinta (F12 ⛔) o richiesta della KB (R3)? | aperta. Il copy non ha la KB: se la segna come F12 ⛔ in tabella, contala come domanda buona e discuti perché l'auditor ha scelto di chiedere |
| 4 | "Registrata" non si dice mai: lo si dice in chiaro? | aperta |
| 5 | La box: il contenuto è confermato? | aperta (il fornitore della box non è trovato, dice la KB) |
| 6 | Medici e prodotto: le frasi di Vernetti, Panfili, Fantechi si leggono come parere sul metodo (L5)? | aperta |
| 7 | Palazzo nella Fase 3 | **già risolta nella scheda di oggi** (§3, decisione del 25/9, e D3 aggiornata). Se il copy la fa, chiedigli dove poteva trovare la risposta. Se la mette in tabella come errore, è un falso positivo |
| 8 | Gli esempi del palazzo esistono nella scaletta reale (D5)? | aperta (la scaletta non è in `examples/`) |
| 9 | Numeri e lessico di grado D ("migliaia di persone", "trauma", "psiconcologia") | aperta |

## 4 · Compito 1 · punti di confronto

Il compito 1 non ha punteggio. Serve a discutere, con le domande, dove il copy ha ragionato bene e dove no. Fonti: scheda §2, §3, §12; caso studio passaggi 0 e 1.

### Cosa ha fatto il team

| Pezzo | Cosa ha fatto il team | Dove |
|---|---|---|
| Forma grezza | "l'unico modo per smettere di vivere dentro l'immagine di te che hai imparato è riscriverla dove è scritta, nell'inconscio; e l'unico modo per farlo è Mind Reset" | scheda §3 |
| Opzioni e criteri | cinque opzioni, i cinque criteri, una proposta di Gianluca bocciata ("il 95/5 è la frase più bruciata della categoria"), tre giri sulla versione di Matteo. La tabella dei criteri non è in `examples/`: giudichi il copy sulle regole, non sul confronto | caso studio p. 1 |
| La svolta di metodo | "stavamo producendo opzioni in astratto invece di partire dal materiale del frontman": sblocca un briefing a Gianluca | caso studio p. 1 |
| Test competitor (20/9) | il vecchio meccanismo "sessione + 21 giorni" **falliva con RTT** (i 21 giorni di Marisa Peer sono dopo). Aggiungendo i **21 giorni prima** passa su tutti e cinque: RTT, Barbieri, SHA/Chenot, Roberto Re, ipnotisti | scheda §3, regola C3 |
| Meccanismo | **21 + 1 + 21**: 21 giorni prima (nessuno ti prepara) + la sessione + 21 giorni dopo (il cambiamento si fissa fuori dalla stanza). LKBD per fase: 1. nessuno ti prepara · 2. non è qualcosa che ti fanno, conta solo la voce · 3. il cambiamento si fissa fuori | scheda §3 |
| Metafore | palazzo buio per le Fasi 1 e 2, camera oscura per la Fase 3 (25/9); iceberg 5/95 come grafica del domino | scheda §3 |
| Obiezione nascosta | "è solo un audio?" → privazione sensoriale in "Conta solo la voce"; ripresa una volta sola nel prezzo ("la voce c'è, la mia ora no") | scheda §3 |
| Domino breve e lungo | congelati il 23/9 ("TIENI QUESTA COME VERSIONE UFFICIALE"), testo in §3. Il 95/5 è dentro per scelta di Matteo, con override | scheda §3, §9, §12 |
| Stack | mappatura 1.000 · 21 giorni di preparazione 5.000 · Sessione di Trasformazione 5.000 · box senza valore ("non te la metto in euro") · 21 giorni di fissaggio 5.000 · WhatsApp 43 giorni 1.000 · **totale 17.000 €** | scheda §2 |
| Prezzo | **2.450 € + IVA** (2.989 € finiti, sotto il tetto Klarna). 2.500 + IVA sforava | scheda §2, caso studio p. 0 |
| Ancore | **10.000 €** il percorso dal vivo, "su selezione" (🟡: il catalogo dice 4.500-5.500, conflitto aperto §13 n. 10) · **3.500 €** il reset di una settimana | scheda §2 |
| Giustificazione del prezzo basso | "la voce c'è, la mia ora no" (B12) | scheda §3, manuale §7 blocco 4 §4.3 |
| Cose superate | stack da 17.500 € con "sessione con Gianluca 5.000 €" e 42 giorni | scheda §2 |

Rapporto valore/prezzo del team: 17.000 / 2.450 ≈ 6,9 (dentro il 5-10 di B5).

### Errori tipici attesi, con la domanda da fare

| Errore | Regola | Domanda |
|---|---|---|
| Domino che parte dal meccanismo, non dal problema di chi guarda | C4 | "Chi guarda, nella prima riga, sente parlare del suo problema o del tuo prodotto?" |
| Prodotto nominato a metà del domino lungo | C8 | "Dove compare Mind Reset nella tua versione lunga? E dove lo vuole C8?" |
| Domino su "capire", "prendere consapevolezza", "decidere" | C2, poi E2 ⛔ | "La storia di Gianluca, alla svolta, cosa fa? Il tuo domino dice che quella cosa funziona?" |
| Test competitor a memoria, senza fonti, o senza guardare quando cadono i 21 giorni di RTT | C3 | "RTT ha dei giorni dopo la seduta? E prima? Dove l'hai letto?" |
| Il 95/5 presentato come fatto, senza verifica | A1 ⛔, A5 | "Da dove viene il 95%? Cosa scrivi se non lo trovi?" (Se il copy lo evita o lo marca `[IPOTESI]`, **ha ragione per le regole**: il team l'ha tenuto con un override) |
| Domino mainstream ("il cambiamento parte dall'inconscio") senza la differenza del meccanismo | C6, C11 | "Un ipnotista potrebbe dire la stessa frase?" |
| Valori a ore: "un'ora di coach vale 1.000 €", "la sessione vale 5.000 € perché è un'ora di Gianluca" | **B4 ⛔** | "Cosa ottiene chi fa la mappatura? Il valore è di quello o del tempo del coach?" (manuale §7 blocco 4 §4.3) |
| Sessione presentata "con Gianluca" o "dal vivo" | vincolo del cliente in scheda §9, A1 | "La sessione è registrata. Cosa capisce chi legge 'con Gianluca'?" |
| Prezzo sopra il tetto delle rate (es. 2.500 + IVA) | B6 | "Quanto fa il tuo prezzo finito? E il tetto Klarna?" |
| Ancora da 10.000 € senza dire del catalogo a 4.500-5.500, o un'ancora senza fonte | A9, B5, A1 ⛔ | "Hai due prezzi per la stessa cosa. Quale scegli, da quale fonte, e dove lo scrivi?" |
| Rapporto valore/prezzo fuori da 5-10 senza motivo | B5 | "Quante volte il prezzo è il tuo totale?" |
| Un componente che non toglie nessun ostacolo (riempitivo), o promesse che il materiale non contiene ("supporto 24/7") | B2, A1 ⛔ | "Quale ostacolo nominato uccide questo componente? Dove hai letto 24/7?" |
| Parole vietate nel domino o nello stack ("in una sola sessione", "guarire", "elimina le convinzioni limitanti") | L8 | "Hai ripassato la lista del materiale, §6?" |
| Box con un valore in euro | non è un errore | "Che ostacolo uccide la box? Perché il team non le ha dato un valore?" |

**Come ne parli:** come in palestra. Al massimo tre punti, il più grave per primo, una domanda e la regola per ciascuno. Poi chiedi al copy di leggere la riga del team e dire con quale regola regge la sua scelta o quella del team. Non dare ragione al team per principio: dove il copy ha una scelta più aderente alle regole (per esempio sul 95/5), diglielo.

## 5 · Quando la chiave va rigenerata

Il webinar Mind Reset non è definitivo. Quando arriva il deck finale, segui la procedura in fondo a `L3-caso-reale/README.md`: nuovo export, nuovo `/webinar-audit` con la scheda, nuova tabella in questo file (§1, con la verifica riga per riga come sopra), nuove ⛔, nuova base, soglia al 58% della base arrotondato per eccesso. Rifai anche il §0 se la scheda nuova riassume di nuovo l'audit.
