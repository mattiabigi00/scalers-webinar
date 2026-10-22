# SCHEDA WEBINAR — FABRIZIO NARDELLI · RITMO SICURO

> **Cos'è:** la fonte unica di verità di questo webinar. Nomi, numeri, frasi congelate, regole del cliente, decisioni. Script e slide si allineano a questa scheda, mai il contrario (regola `M2`).
> **Dove vive:** `01_SCALERS/CLIENTI/<CLIENTE>/…/WEBINAR/SCHEDA_WEBINAR_<PRODOTTO>.md`. Il modello vuoto sta in `06_OPERATIONS/WEBINAR/TEMPLATE_SCHEDA_WEBINAR.md`.
> **Come si usa:** si apre al passaggio 0 della pipeline e si aggiorna a ogni decisione (§12). Prima di scrivere o modificare una slide si controlla qui. La skill `webinar-audit` confronta script e deck con questa scheda.
> **Legenda stato:** ✅ congelato · 🟡 deciso ma da confermare col cliente · ❌ aperto

---

## 0 · STATO

| Voce | Valore |
|---|---|
| Passaggio attuale della pipeline | 6 · Grafica (fermo: prima pubblicazione dell'artifact giro 1, audit `/webinar-audit` e rework del senior; la grafica non è mai automatica) |
| Ultimo aggiornamento | 2026-09-30 (collaudo end-to-end, passaggi 0-5) |
| Script vivo | `SCRIPT_RITMOSICURO_v2.md` · versione v2 (v1 e `CONFRONTO_RITMOSICURO.md` nella stessa cartella) |
| Deck vivo | artifact Slides giro 1: **da pubblicare dalla sessione principale** (non pubblicato nel collaudo) · versione v1 copy · export testo: `DECK_RITMOSICURO_testo.md` · file dell'artifact: `deck/project/` (110 slide) |
| Frontman | Fabrizio Nardelli |
| Durata prevista | ~40 minuti di testo (deck: ~5.700 parole con i titoli, a 140 parole/minuto) · +30-40% con le digressioni (N2): ~55 minuti · 110 slide |
| Posizione nel funnel | dopo la discovery, con la call successiva già fissata (N5 ⛔) · 🟡 chi fa la call: vedi §13 |

## 1 · FONTI DEL CLIENTE

| Per… | File |
|---|---|
| Regole del brand | nessuna KB del cliente (niente `CLAUDE.md`, `voce.md`): parole e divieti da `INTAKE_RITMOSICURO_risposte.md` §8 |
| Numeri | nessun `numeri-baseline.md`: `INTAKE_RITMOSICURO_risposte.md` §5 e §7 (unica fonte primaria) |
| Offerta | `INTAKE_RITMOSICURO_risposte.md` §3 (scaletta reale settimana per settimana) e §7 |
| Prove | `INTAKE_RITMOSICURO_risposte.md` §2.2, §4, §5 · file originali presso il cliente |
| Design system | `INTAKE_RITMOSICURO_risposte.md` §9 (bordeaux #6B1E2E, crema #F4EAD5; font e vettoriale del logo da ricevere) |

## 2 · OFFERTA CONGELATA

| Voce | Valore | Stato | Fonte / decisione |
|---|---|---|---|
| Nome del prodotto | **Ritmo Sicuro** (il percorso dal vivo di prima si chiamava Palco Vero: si nomina solo come percorso passato e come ancora, mai come nome del prodotto) | ✅ | intake §3 · D0 |
| Nomi delle fasi (come si dicono in slide) | **Fase 1 · La camera** (settimane 1-2) · **Fase 2 · Gli ascoltatori** (settimane 3-5) · **Fase 3 · Il live** (settimane 6-8). "Gli scalini" resta la parola del metodo intero (il cliente: "prima del palco ci sono sette scalini… il live finale è lo scalino otto"), non il nome di una fase | ✅ | intake §2.1 obiez. 4 e 10, §3 · D0 · Rocco (simulato) 2026-09-30 |
| Nome della sessione / componente centrale | **la Serata Ritmo Sicuro** (il live finale, settimana 8) | ✅ | intake §3 |
| Durata totale | **8 settimane** | ✅ | intake §3 |
| Impegno richiesto | **30-40 minuti al giorno, cinque giorni su sette** (serve lo strumento, un telefono e una stanza). Se salti un giorno si recupera; il video del venerdì è l'unica cosa non negoziabile | ✅ | intake §3. Conflitto A9: nella risposta all'obiezione 5 il cliente dice "mezz'ora al giorno": vale la scaletta (30-40 minuti) |
| Prezzo | **1.990 € + IVA** (2.427,80 € IVA inclusa, con IVA al 22%) | 🟡 | intake §7 · D0.1 · Rocco (simulato) 2026-09-30 · aliquota IVA da confermare |
| IVA inclusa / esclusa | esclusa in slide ("+ IVA") | 🟡 | intake §7 |
| Rate | tre rate senza interessi con Stripe, oppure Klarna (2.427,80 € finiti: sotto il tetto di 3.000 €, B6) | ✅ | intake §7 |
| Ancora 1 (interna) | **Palco Vero**, il percorso dal vivo in sala prove a Bologna: **3.400 €**, 12 incontri (ultimo gruppo nel 2024: in slide al passato) | ✅ | intake §7 |
| Ancora 2 (alternativa di mercato) | **lezioni private** con Fabrizio a **70 €** l'ora, "ne servirebbero una trentina" (stima del cliente, circa **2.100 €**) · **un mental coach** per il palco a **120 €** a sessione | ✅ | intake §7 e "Concorrenti" (Stage Mind) |
| Garanzia (nome e condizioni) | **«Rifai con me»**: se fai tutto (tutti i video del venerdì e almeno 6 call del martedì su 8) e alla settimana 8 non te la senti di salire alla Serata, rifai l'edizione successiva gratis, con Fabrizio. Niente rimborso. Si promette un impegno, mai "garantito che suoni" (B9) | 🟡 | intake §7 e §8 · D0.4 · nome: Rocco (simulato) · da confermare: l'edizione ripetuta include 1:1 e Serata? |
| CTA principale | la **call già fissata** con "uno dei miei consulenti" (nessun nome in slide, G21) | 🟡 | intake §9 · D0.7 · chi fa la call (Marta o venditori) da confermare |
| CTA secondaria (quick checkout) | link per iscriversi subito | ✅ | intake §9 |
| Bonus | **una sessione 1:1 in più con Fabrizio** (45 minuti, prima dell'inizio, per scegliere insieme la canzone-àncora) a chi si iscrive **entro 72 ore** dal webinar, **massimo 10 persone**. Dopo il prezzo, fuori dallo stack (B11). Ok del frontman: sì | 🟡 | intake §7 · D0.6 · da confermare: da quando si contano le 72 ore, 10 per edizione? |
| Regalo per chi resta fino alla fine | **«Il minuto prima»**, l'audio di 7 minuti (cosa fare nel minuto prima di suonare con le mani, il respiro e lo sguardo). Esiste già (settimana 4) | ✅ | intake §3 |
| Scarsità (vera, con motivo) | **24 posti per edizione**: 2 gruppi da 12, perché i gruppi li segue Fabrizio; la Serata è una sera sola e il locale più di così non ne tiene. **Prossima edizione: 12 gennaio 2027.** A gruppi pieni si passa all'edizione dopo. Niente countdown, niente "ultimi posti" | ✅ | intake §7 · D0.5. ⛔ **Rifiutato** il "restano 5 posti" chiesto dal cliente (B10) |

**Stack**

| Macroarea / fase | Componente | Beneficio (cosa dice la slide) | Valore |
|---|---|---|---|
| Fase 1 · La camera | I video della camera | dal primo giorno smetti di provare la canzone e cominci a provare il palco, a casa tua | 1.500 € |
| | Il video del venerdì, con il feedback scritto entro 48 ore (8 settimane) | ogni settimana qualcuno che conosce la strada guarda come suoni davvero e ti dice cosa ha funzionato | 2.000 € |
| | La prima sessione 1:1 con Fabrizio (settimana 2) | sai esattamente dove ti inceppi e cosa fanno le tue mani in quel punto | 500 € |
| Fase 2 · Gli ascoltatori | I tre scalini con gli ascoltatori | suoni per qualcuno prima di sentirti pronto | 2.000 € |
| | La call del martedì (8 call di gruppo da 90 minuti) | ogni settimana un pubblico vero che dice solo cosa ha funzionato | 1.500 € |
| | «Il minuto prima» | è il regalo di oggi: fuori dal conteggio | — |
| Fase 3 · Il live | La scaletta e la frase ponte, con la seconda sessione 1:1 (settimana 6) | non sali con una canzone, sali con una scaletta | 1.000 € |
| | La prova generale: il tuo house concert (settimana 7) | la prima volta davanti a 5-10 persone la fai a casa tua | 1.000 € |
| | La Serata Ritmo Sicuro (settimana 8) | finisci le 8 settimane su un palco vero, non con un attestato | 3.500 € |
| **Totale** | | | **13.000 €** |
| **Prezzo** | | | **1.990 € + IVA** |

## 3 · BIG DOMINO, MECCANISMO, METAFORA

**Forma grezza (tavolo di lavoro):** L'unico modo per suonare davanti agli altri come suoni quando sei da solo è provare il palco, non la canzone, uno scalino alla volta, dalla tua stanza fino a un palco vero; e l'unico modo per provare il palco così, con qualcuno che guarda ogni tuo scalino e un palco vero alla fine, è con Fabrizio (Ritmo Sicuro).

**Versione breve — congelata** (✅ · 2026-09-30):
> La canzone l'hai provata mille volte, il palco mai: e il palco si prova come una canzone, uno scalino alla volta.

**Versione lunga — congelata, verbatim** (✅ · 2026-09-30):
> Suoni da anni. Quando la casa è vuota, le mani vanno da sole.
> Poi qualcuno dice «dai, suonaci qualcosa», e le mani diventano quelle di un altro.
> Allora hai fatto quello che ti hanno insegnato tutti: più tecnica, più scale, più ore.
> Qualcuno ti ha fatto respirare, qualcuno ti ha detto di immaginare il pubblico in mutande, qualcuno ti ha detto «buttati».
> E non è cambiato niente, perché il problema non è lì.
> La canzone l'hai provata mille volte, il palco mai.
> Il palco non è una dote che hai o non hai: è una cosa che si prova, come una canzone.
> Solo che non si prova tutto in una volta: si prova uno scalino alla volta, dalla tua stanza fino a un palco vero.
> E ogni scalino si fa con le mani che hai, anche fredde.
> Ed è esattamente quello che fa Ritmo Sicuro.

**Test competitor** (regola C3, dettaglio in `DOMINO_RITMOSICURO_opzioni.md` §5):

| Concorrente | Può dire la stessa frase? |
|---|---|
| PalcoFacile (corso online, respirazione e visualizzazione) | No: niente pubblico, niente palco, niente scalini |
| Stage Mind (mental coach, PNL) | No: lavora sui pensieri, il palco non lo fa provare |
| Scuole di musica (saggio una volta l'anno) | No: il saggio è un salto unico, non una scala |
| App (Yousician, Simply Piano) | No: suoni sempre e solo per un telefono |
| Open mic e jam ("buttati") | No: "il palco si impara sul palco" sì, ma senza scalini |

**Nome del meccanismo:** gli otto scalini
**Little Known Big Difference per step:** 1. La camera: tutti provano la canzone finché viene perfetta, rifacendola; noi proviamo il palco, una take sola con la lucina rossa accesa e un errore messo apposta · 2. Gli ascoltatori: tutti aspettano di sentirsi pronti; noi suoniamo per qualcuno prima di sentirci pronti, di spalle, di fronte, con la TV accesa · 3. Il live: tutti dicono «buttati»; noi al palco ci arriviamo dopo sette scalini, e il palco c'è davvero
**Metafora del meccanismo** (una sola, regola D3): la scala, dalla stanza al palco — dove nasce nella storia: le sei settimane "a scalini" del 2003-2004 (blocco 2, piano) — come torna in ogni step: La camera = scalini 1-2, Gli ascoltatori = scalini 3-5, Il live = scalini 6-8; nello stack ogni componente sta sul suo scalino
**Obiezione nascosta del prodotto e dove si disinnesca** (regola D6): "è online: il palco da uno schermo?" → nel meccanismo (blocco 2, subito dopo il domino): i primi sette scalini si fanno dove suoni davvero, a casa tua, e l'ottavo è un palco vero con pubblico vero; il telefono con la lucina rossa non è l'insegnante, è il primo spettatore che non ti lascia rifare

## 4 · PROMESSA E INTRO

| Pezzo | Testo congelato | Stato |
|---|---|---|
| Promessa (slide 1) | Come passare dalla cameretta a un palco vero in 8 settimane e suonare davanti agli altri come suoni da solo, anche se ti tremano le mani e nessuno ti ha mai sentito suonare | ✅ 2026-09-30 · tempo = durata reale (A7) · promette un percorso, non un risultato garantito (B9) |
| Nemici (origine + false soluzioni) | **Origine:** il modo in cui ci hanno insegnato a suonare: tecnica, scale, repertorio, e il palco una volta l'anno, al saggio, dove chi ha paura si imbosca. Nessuno l'ha fatto apposta. **False soluzioni:** chi ti ha fatto respirare e immaginare il pubblico in mutande; chi ti ha detto «buttati» (intake §8 "Da cosa mi dissocio", "Concorrenti" 3 e 5) | ✅ |
| Sospetto confermato | L'hai sempre sospettato: non è una questione di tecnica. Lo sai perché conosci gente che suona peggio di te e sale sul palco ridendo | ✅ |
| Impegno attivo (es. il foglio) | **Il foglio:** chi guarda scrive la canzone che suonerebbe se stasera qualcuno gli dicesse «dai, suonaci qualcosa», e sotto per chi la suonerebbe. Torna: **prezzo** (quanto vale suonarla per quella persona) · **garanzia** (alla settimana 8 rileggi il foglio) · **CTA** (porta il foglio in call: può diventare la tua canzone-àncora) | ✅ |
| Credenziali "chi sono" | 1. chitarrista turnista per quindici anni (1995-2009) · prova: foto dal palco del tour '98 col pass, crediti Discogs · 🟡 da ricevere · 2. `[DA CLIENTE: numero esatto dei dischi, 38 o 40]` dischi · prova: crediti Discogs, copertine · ❌ numero da verificare · 3. tour estivi nelle piazze con Mirko Salvi · prova: foto del palco e dietro le quinte · ❌ consenso di Mirko Salvi (L4) · 4. house band di un programma del sabato sera di Rai 1 · prova: fotogramma che il cliente non ha · ❌ `[PROOF]` · 5. sei anni insegnante alla Scuola Civica di Musica di Ferrara · prova: lettera del direttore · 🟡 da ricevere · 6. `[DA CLIENTE: 300 o più di 450]` allievi seguiti · prova: gestionale + registro di Palco Vero · ❌ conflitto A9 · 7. 4,9 su Google su 120 recensioni · prova: screenshot · 🟡 da ricevere, di quale scheda? | 🟡 |

## 5 · EPIPHANY BRIDGE

Strumento che il domino dichiara **efficace:** provare il palco, uno scalino alla volta. Strumento che dichiara **inutile:** più tecnica, capire (respirazione, libri), buttarsi senza preparazione.

| Beat | Contenuto (in una riga) | Fonte (trascrizione del frontman) | Stato |
|---|---|---|---|
| Backstory con una scena | Agosto 1996, piazza di Senigallia, primo tour vero con Mirko Salvi, 4-5.000 persone. In studio "Nardelli la fa buona alla prima". Settimo pezzo, "Vento di maggio", assolo di sedici battute: si gira verso il pubblico, le mani si gelano, il plettro cade, il tastierista copre con l'organo. Nel furgone il capobanda: "In studio sei un orologio. Sul palco sei un'altra persona." | intake §1.1 (vocale trascritto dal cliente) | ✅ · età da verificare (E12) |
| Desiderio | Dopo quella sera chiede di fare solo studio e si racconta che il palco è per chi vuole farsi vedere: "ero uno snob per paura" (fase rinnegata, E10). Quello che voleva davvero non è detto in modo esplicito | intake §1.1 e §1.4 | 🟡 `[DA CLIENTE: cosa volevi davvero in quegli anni?]` |
| Muro | Tecnica, tecnica e tecnica: 6-7 ore al giorno di scale, due anni di jazz a Bologna, assoli trascritti, un libro sulla respirazione. 2003, matrimonio del cugino in un agriturismo sui colli di Imola, 40 persone che gli volevano bene: non riesce a fare quattro accordi ("la chitarra è scordata", non lo era). In macchina, alla moglie: "Non è la tecnica. Ero il più bravo nella stanza e non ho saputo fare quattro accordi." | intake §1.2 | ✅ |
| Epifania | Inverno 2003-2004, jam all'Osteria del Moro di Bologna. Un batterista di settant'anni: "Tu la canzone l'avrai provata mille volte. Il palco quante volte l'hai provato? Zero. E pretendi di saperlo fare." | intake §1.3 | ✅ |
| Piano: lo strumento trovato | Una canzone sola ("Can't Find My Way Home") e sei settimane in cui non prova la canzone ma il palco, a scalini: una take al giorno con la lucina rossa della videocamera accesa; un errore apposta alla battuta otto; per la moglie di spalle, poi di fronte; per i vicini sul pianerottolo; per tre amici in salotto. È lo strumento del domino (E2 ✅) | intake §1.3 | ✅ |
| Resistenza | Terza settimana, davanti ai tre amici: si blocca alla stessa battuta, mani fredde. "Lascio perdere, è inutile, sono fatto così." La moglie: "Hai sbagliato e sei andato avanti. Al matrimonio ti eri fermato." Si era bloccato, ma non si era fermato | intake §1.3 | ✅ |
| Prima volta che ha funzionato su di lui | Marzo 2004, open mic all'Osteria del Moro: tre pezzi. Al secondo sbaglia un accordo e va avanti. Nessuno se ne accorge. Scena diversa dall'epifania (E4 ✅) | intake §1.3 | ✅ |
| Come se n'è accorto (risultato concreto) | A metà del terzo pezzo si accorge che sta guardando il pubblico: una signora in prima fila canta sottovoce, lui le sorride. Le mani sono calde. "Io, che per otto anni avevo suonato guardando il manico." | intake §1.4 | ✅ |
| Cosa ha costruito · missione | Il giorno dopo richiama il capobanda e torna in tour. Dal 2010 al 2016 insegna alla Scuola Civica di Ferrara: gli allievi adulti hanno tutti il suo problema (benissimo in cameretta, crollano al saggio) e comincia a fargli fare gli scalini. Nel 2016 apre un percorso dal vivo in sala prove a Bologna, dal 2022 lo porta online. Arriva il **metodo**, non il prodotto (E5) | intake §1.4 | ✅ · date da verificare (E12) |
| Cerniera: "ed è proprio per questo che…" | …ed è proprio per questo che te lo dico così: la canzone l'hai provata mille volte, il palco mai: e il palco si prova come una canzone, uno scalino alla volta. | domino breve congelato §3 | ✅ |

**Verifiche cronologiche aperte** (E12, anche in `DOMANDE_CLIENTE_RITMOSICURO.md`):
1. Agosto 1996 "avevo diciannove anni", ma "sono nato a Ferrara nel 1974": a agosto 1996 gli anni sono 21 o 22. Nello script l'età non si dice finché non è verificata.
2. Dopo Senigallia "ho chiesto di fare solo studio… per un sacco di anni", ma le credenziali dicono tour estivi con Salvi anche nel 1998 (e c'è la foto del tour '98).
3. Dopo l'open mic di marzo 2004 "ho chiamato il capobanda… per il tour dell'estate", ma "ho rifatto i tour dal 2005 al 2009": l'estate 2004 c'è stata?
4. "Nel 2003 suonavo da vent'anni" (dal 1983, a 9 anni): da confermare.
5. Il percorso dal vivo è finito nel 2024 ma nel 2022 è partito quello online: per due anni c'erano tutti e due? (serve per "l'ho portato online").

## 6 · LE TRE CREDENZE

Obiezioni reali (intake §2.1) raggruppate (F3): **veicolo** 4, 7, 10 · **interna** 2, 3, 5, 6, 9 · **esterna** 1, 8. La più grande per gruppo è in tabella.

| Credenza | Come la dice il pubblico | Fase / step | Credenza nuova | Prova (storia vera · caso logico · kinda-like bridge) | Stato |
|---|---|---|---|---|---|
| Veicolo | "Un corso online per il palco? Il palco si impara sul palco." (obiez. 4) | Fase 1 · La camera | Il palco si prova anche a casa: il telefono con la lucina rossa è il primo spettatore, e alla fine il palco c'è davvero | **storia vera:** Giorgio, 52 anni, geometra, pianoforte da trent'anni: "il palco si impara sul palco, cosa mi insegni da uno schermo?", webcam sul lampadario per due settimane, crollo alla settimana 3, alla 5 suona per undici persone ridendo dell'errore, Serata di giugno 2024, poi l'assemblea di condominio senza appunti. Liberatoria ✅. F4 ✅ (obiezione detta per prima, parte da più lontano, prova esperienziale, credenza dedotta) · F6 ricaduta ✅ · F7 lavoro ✅ | ✅ |
| Interna | "Io sono fatto così, a me le mani tremano. È fisico." (obiez. 3, con 6 "prima devo migliorare la tecnica") | Fase 2 · Gli ascoltatori | Le mani fredde non spariscono: impari a suonare con le mani fredde | **storia vera, anonima:** un'insegnante di lettere di 47 anni, chitarra dai quindici: "Io sono fatta così, a me le mani tremano da quando ho quindici anni. È fisico"; stava seduta sulle mani; alla settimana 4 (il disturbo) piange: "per me è inutile, lo sapevo"; alla Serata le mani tremano trenta secondi e continua: "Tremavano e suonavano. Non sapevo che si potessero fare le due cose insieme"; a scuola ha fatto il discorso dell'open day. **Senza nome né volto:** manca la liberatoria scritta (L2 ⛔). F4 ✅ · F5 (credenza-conclusione su di sé) ✅ · F6 ✅ · F7 ✅ | ✅ anonima |
| Esterna | "E poi dove suono? Non ho una band, i locali non ti chiamano, non ho occasioni." (obiez. 8, con 1 "io suono per me") | Fase 3 · Il live | Le occasioni non mancano: le hai già avute e hai detto «no, stasera no». Il palco lo costruisci tu: prima il salotto, poi la Serata | **kinda-like bridge** (decisione D2): "c'è mai stata una volta in cui qualcuno ha detto «dai, suonaci qualcosa» e hai detto no?" (parole del cliente, obiez. 1) + un fatto vero del frontman (il matrimonio era un'occasione; dopo l'open mic richiama il capobanda e torna in tour) + il prodotto (settimana 7 l'house concert lo organizzi tu, settimana 8 la Serata). Storia vera di un allievo richiesta al cliente. La storia "verosimile" chiesta dal cliente non si scrive (A3 ⛔) | 🟡 bridge ok · storia vera richiesta |

## 7 · PROVE PER IL WEBINAR

| Prova | Tipo (video, screenshot, documento, clip) | Dove va (blocco/slide) | Liberatoria | Stato |
|---|---|---|---|---|
| Video di Giorgio (2 minuti, .mov originale) | video | fase 1, prova del veicolo | ✅ firmata a ottobre 2024 | 🟡 file da ricevere |
| Messaggio di Giorgio dopo l'assemblea ("ho fatto la mia canzone-àncora con sessanta condòmini") | screenshot | fase 1 | ✅ (stessa persona) | 🟡 screenshot da ricevere |
| Storia di Simonetta raccontata da Fabrizio, senza nome né volto | racconto | fase 2, prova della credenza interna | — anonima, non serve | ✅ |
| Video di Simonetta (1 minuto e mezzo, dopo la Serata di giugno 2025) | video | nessuna finché manca la liberatoria | ❌ solo un consenso a voce: non basta (L2 ⛔) | bloccato |
| Video delle Serate 2023, 2024, 2025 | video | fase 3 e muro finale | 🟡 liberatoria "per le riprese della serata, per il locale": va verificato che copra un video di vendita | `[PROOF]` |
| Recensioni Google (4,9 su 120) | screenshot | chi sono e muro finale | — pubbliche, nomi sfocati (L12) | `[PROOF]` da ricevere |
| Screenshot WhatsApp dal gruppo (circa venti, dopo le Serate) | screenshot | muro della fase 2 | — anonimi, nomi e foto sfocati | `[PROOF]` da ricevere |
| Testimonianze di Palco Vero (una decina di messaggi, due video) | messaggi, video | muro finale, dichiarate come percorso dal vivo (L3) | ❌ nessuna liberatoria: solo i messaggi, anonimi | 🟡 |
| "Il più grande che ho portato alla Serata aveva 63 anni" | dato del frontman | FAQ | — anonimo | ✅ |
| Calendario dell'edizione del 12 gennaio 2027 | screenshot | scarsità, blocco 4 | — | `[PROOF]` da ricevere |
| Audio «Il minuto prima» (7 minuti) e link o QR per consegnarlo | audio | regalo, blocco 4 | — | `[PROOF]` file e link da ricevere |
| Prove delle credenziali: Discogs, foto del tour '98, lettera del direttore della Scuola Civica, fotogramma Rai 1 | documenti, foto | chi sono | — | `[PROOF]` da ricevere · fotogramma Rai: il cliente non ce l'ha |
| Foto del frontman: passato (tour '96, studio anni '90, open mic 2004) e presente (ritratti, Serate, sala prove) | foto | storia e chi sono (giro 2) | — | presso il cliente |

**Segnaposto ancora aperti nel deck** (lint del 2026-09-30, 17): `[PROOF]` intro-teoria, chi-dischi, chi-piazze, chi-tv, eb-prove, f1-giorgio-video, f2-muro, f3-serata, v-calendario, v-muro, v-regalo · `[DA CLIENTE]` chi-dischi, chi-allievi, eb-snob, eb-costruito, eb-storia, v-scelte, v-bonus. Nessun `[INVENTATO]`.

## 8 · TERZI (citazioni, foto con personaggi, esperti)

| Persona | Cosa usiamo | Dove | Consenso | Audio riascoltato | Come si presenta (regole L4-L6) |
|---|---|---|---|---|---|
| Mirko Salvi (cantante, datore di lavoro del frontman) | **oggi nel deck non è nominato** ("un cantante che faceva le piazze d'estate"); con il consenso: nome nelle credenziali e foto dietro le quinte | storia (eb-agosto), chi sono (chi-piazze) | ❌ non chiesto ("non gli ho chiesto niente") | n/a (fonte scritta) | come datore di lavoro, mai come cliente né come testimonial (L6) |
| La moglie del frontman (nome in intake) | una frase ("Hai sbagliato e sei andato avanti. Al matrimonio ti eri fermato"), come "mia moglie", senza nome | storia (resistenza) | ❌ da chiedere | n/a (fonte scritta) | "mia moglie" |
| Il batterista dell'Osteria del Moro (nome di battesimo in intake) | una frase, senza nome | storia (epifania) | ❌ da chiedere, se raggiungibile | n/a | "un batterista di settant'anni" |
| Il capobanda del tour 1996 | una frase, senza nome | storia (backstory) | ❌ da chiedere | n/a | "il capobanda" |
| Il direttore della Scuola Civica di Ferrara | la sua lettera come prova | chi sono (giro 2) | ❌ da chiedere prima di mostrare nome e firma | n/a | prova documentale, non citazione |

Non nominati in slide (nessun consenso necessario): il tastierista Dario, il cugino Stefano, i coach Marta e Ivan (G21: nessun nome del consulente in slide).

## 9 · PAROLE

**Vietate dal cliente:** ansia, attacchi di panico, terapia, blocco psicologico, talento, diventa una rockstar, sfondare, guarire, non avrai più paura, garantito che suoni.
**Vietate da noi:** ultimi posti, curare.
**Override di Matteo** (parola · dove · data · motivo): nessuno.
**Parole del cliente da usare** (intake §8): il palco, suonare per qualcuno, la tremarella, le mani (fredde, calde), la canzone-àncora, gli scalini, andare avanti (quando sbagli), il video del venerdì. Niente promesse sanitarie o psicologiche (L9): Fabrizio non si presenta come psicologo. Il cliente si dissocia da: guru del mindset (respirare, pubblico in mutande), "buttati e basta", talent show.
**Si dice / non si dice** (glossario del webinar):

| Si dice | Non si dice |
|---|---|
| Ritmo Sicuro | Palco Vero (come nome del prodotto: Palco Vero è il percorso dal vivo di prima), il corso (per Ritmo Sicuro) |
| la Serata Ritmo Sicuro | concerto finale, saggio finale |
| il video del venerdì | compito |
| la call del martedì | lezione in diretta |
| la canzone-àncora | brano del corso |
| uno dei miei consulenti | Marta, Ivan (in slide) |

## 10 · PROMESSE PIANTATE → DOVE SI CHIUDONO (regola G14)

| Piantata in | Cosa | Chiusa in |
|---|---|---|
| blocco 1 · la tesi e la scala | "ti faccio vedere gli otto scalini uno per uno" | blocco 3 (le tre fasi) |
| blocco 1 · il foglio | la canzone e la persona per cui la suoneresti | blocco 4: quanto vale per te · garanzia · CTA |
| blocco 1 · cosa porti a casa | il regalo «Il minuto prima» per chi resta fino alla fine | blocco 4: "ricordi il regalo? eccolo" |
| blocco 2 · gli otto scalini | "ti faccio conoscere uno che diceva esattamente così" | blocco 3: Giorgio |
| blocco 2 · gli otto scalini | "me lo dicono tutti: sì, ma…" (tre obiezioni) | blocco 3: fase 1, 2, 3 |

## 11 · COSA COMPARE SOLO NELLO STACK (regola G15)

Le due sessioni 1:1 con Fabrizio · il video del venerdì con il feedback scritto entro 48 ore · la call del martedì (prima dello stack solo "il tuo gruppo", e l'accenno alla "prima call di gruppo" nella storia vera di Giorgio) · la garanzia «Rifai con me» · le rate · il bonus delle 72 ore.

## 12 · REGISTRO DECISIONI

| Data | Decisione | Chi | Dove applicata (script / slide) |
|---|---|---|---|
| 2026-09-30 | Webinar aperto · senior: Rocco (simulato · collaudo) | Rocco (simulato · collaudo) | scheda |
| 2026-09-30 | Modalità automatica (`/webinar-avanti auto`): sostituisce l'approvazione del senior tra i passaggi con i criteri verificati di `CANCELLI.md`; si ferma solo sulle decisioni 🧑 (qui simulate, vedi `DECISIONI_RICHIESTE.md`) | plugin | — |
| 2026-09-30 | D0.1 · Prezzo 1.990 € + IVA. Scartato 2.490 € + IVA: 3.037,80 € finiti sfora il tetto Klarna (B6) | Rocco (simulato · collaudo) | §2 |
| 2026-09-30 | D0.2 · Stack a 3 fasi, valori del beneficio, totale 13.000 € (6,5 volte il prezzo). «Il minuto prima» fuori dal conteggio perché è il regalo | Rocco (simulato · collaudo) | §2 |
| 2026-09-30 | Nomi delle fasi: La camera · Gli ascoltatori · Il live. "Gli scalini" = il metodo intero | Rocco (simulato · collaudo) | §2, §9 |
| 2026-09-30 | D0.4 · Garanzia di continuazione del cliente, nome «Rifai con me» | Rocco (simulato · collaudo) | §2 |
| 2026-09-30 | D0.5 · ⛔ Rifiutata la scarsità finta chiesta dal cliente ("restano 5 posti"): B10 non si deroga. Scarsità vera: 24 posti, 12 gennaio 2027. Messaggio M5 al cliente | plugin (regola ⛔, non decisione) | §2 · `INTAKE_RITMOSICURO_richiesta.md` |
| 2026-09-30 | D0.6 · Bonus 1:1 entro 72 ore, max 10 persone, dopo il prezzo (B11); 🟡 finché non si chiarisce da quando contano le 72 ore | Rocco (simulato · collaudo) | §2 |
| 2026-09-30 | D0.7 · CTA principale = call già fissata con "uno dei miei consulenti" (G21, N5 ⛔); CTA secondaria = link per iscriversi | Rocco (simulato · collaudo) | §2 |
| 2026-09-30 | Richiesta delle prove partita (messaggio tipo D) | plugin | `INTAKE_RITMOSICURO_richiesta.md` |
| 2026-09-30 | Cancello 0 chiuso · Offerta pronta · decisioni 🧑 D0 simulate, criteri verificati (§2 senza voci aperte, B5 6,5 volte, B6 ok, B10 vera) | Rocco (simulato · collaudo) | §2 |
| 2026-09-30 | D1 · Big Domino: scelta l'opzione A. Breve e lunga dichiarate "versione ufficiale" e congelate (C9). Stress test del prospect-scettico fatto: aggiunta la grafica degli otto scalini nominati subito dopo il domino | Rocco (simulato · collaudo) | §3 · `DOMINO_RITMOSICURO_opzioni.md` |
| 2026-09-30 | Cancello 1 chiuso · versione ufficiale · domino A congelato, meccanismo "gli otto scalini", metafora della scala | Rocco (simulato · collaudo) | §3 |
| 2026-09-30 | ⛔ Rifiutata la storia "verosimile" per la credenza esterna chiesta dal cliente (A3). ⛔ Simonetta solo anonima, video bloccato: consenso solo a voce (L2). Messaggi M5 al cliente | plugin (regole ⛔, non decisioni) | §6, §7 · `INTAKE_RITMOSICURO_richiesta.md` |
| 2026-09-30 | D2 · Prove mancanti, credenza esterna: opzione (b) kinda-like bridge + fatto vero del frontman + prodotto; storia vera di un allievo richiesta in parallelo | Rocco (simulato · collaudo) | §6 |
| 2026-09-30 | Verifiche cronologiche e conflitti di dati (età 1996, tour 1998, estate 2004, allievi 300/450, dischi 38/40) mandati al cliente: nello script restano fuori o come `[DA CLIENTE]` | plugin | §4, §5 · `DOMANDE_CLIENTE_RITMOSICURO.md` |
| 2026-09-30 | Cancello 2 chiuso · Materiale del cliente · ogni beat con fonte, E2 ok, liberatorie e consensi con stato, parole vietate copiate, decisione D2 registrata | Rocco (simulato · collaudo) | §4-§9 |
| 2026-09-30 | D3 · Architettura A: una credenza per fase, ordine classico (camera → veicolo, ascoltatori → interna, live → esterna); "tre fasi", non "tre segreti". Intro in ordine G3-G11 (REVISIONE A3) | Rocco (simulato · collaudo) | `ARCHITETTURA_RITMOSICURO.md` · §6 |
| 2026-09-30 | Cancello 3 chiuso · Architettura · tabella dei blocchi (~70 min), tesi 5 volte, foglio in 3 ritorni, §10 e §11 compilate, obiezioni vinte pianificate (F12) | Rocco (simulato · collaudo) | `ARCHITETTURA_RITMOSICURO.md` |
| 2026-09-30 | Durata rivista: l'architettura stimava ~70 minuti; lo script v2, con i buchi del confronto chiusi e solo materiale vero, ha ~5.700 parole (~40-45 minuti di testo). Allungare oltre vorrebbe dire riempitivo (B2, G1) o nuove storie del cliente: si tiene così | plugin | §0 · `ARCHITETTURA_RITMOSICURO.md` |
| 2026-09-30 | Cancello 4 chiuso · Script · chiuso in automatico, criteri verificati (frasi congelate verbatim, nessun `[INVENTATO]`, segnaposto tutti in `DOMANDE_CLIENTE`, confronto G23 con 14 buchi chiusi in v2, esempi dalla scaletta reale, nessuna obiezione vinta riaperta) | plugin | `SCRIPT_RITMOSICURO_v2.md` · `CONFRONTO_RITMOSICURO.md` |
| 2026-09-30 | Deck testo v1 (110 slide, ~5.700 parole). Lint: ⛔ 0 · alta 0 · 1 da verificare (falso positivo del glossario: "palco vero" non è il nome "Palco Vero") · 17 segnaposto. Tolti gli asterischi del corsivo (non supportato da `build_deck.py`) | plugin | `DECK_RITMOSICURO_testo.md` · `LINT_RITMOSICURO.md` |
| 2026-09-30 | `build_deck.py` → `deck/project/` (110 file, un solo `<h2>` e al più un `<p>` per slide). `export_deck.py --check-h3` sulla build locale: 0 violazioni H3; andata e ritorno: titoli e corpi identici su 110 slide; `[immagini:]` e `[layout:]` tornano solo dentro le note | plugin | `deck/` |
| 2026-09-30 | D5 · Rework del senior sul deck: nel collaudo non c'è (nessuna mossa da applicare). Artifact Slides non pubblicato: lo pubblica la sessione principale, poi va rilanciato `export_deck.py --check-h3` sull'artifact pubblicato (M6) | Rocco (simulato · collaudo) | `DECISIONI_RICHIESTE.md` |
| 2026-09-30 | Cancello 5 chiuso · Slide copy (giro 1) · lint senza ⛔, H3 ok sulla build locale, stack identiche e somme giuste, nessuna voce "non si dice" a schermo, regia nelle note. **Non verificati:** H3 sull'artifact pubblicato, rework del senior | Rocco (simulato · collaudo) | `DECK_RITMOSICURO_testo.md` |

## 13 · APERTI — DA DECIDERE O CONFERMARE

| # | Cosa | Chi decide | Blocca |
|---|---|---|---|
| 1 | Prove richieste il 2026-09-30 (messaggio D): video, liberatorie, screenshot, prove delle credenziali | cliente | passaggio 8 |
| 2 | Aliquota IVA (22%?) e prezzo finito 2.427,80 € | cliente | passaggio 8 |
| 3 | Bonus: da quando si contano le 72 ore in un webinar registrato; i 10 posti sono per edizione? | cliente | passaggio 8 (B10 ⛔ se non verificabile) |
| 4 | Garanzia «Rifai con me»: l'edizione ripetuta include le 1:1 e una nuova Serata? | cliente | passaggio 8 |
| 5 | CTA: chi fa la call dopo il webinar (Marta o i venditori) e posizione nel funnel (N5 ⛔) | cliente + senior | passaggio 8 |
| 6 | Liberatoria scritta di Simonetta (finché manca: anonima, video bloccato) | cliente | passaggio 8 (L2 ⛔ solo se si usano nome o volto) |
| 7 | Storia vera di un allievo per la credenza esterna (oggi: kinda-like bridge, D2) | cliente | nulla (rinforzo) |
| 8 | Consensi dei terzi in §8 (Mirko Salvi, moglie, batterista, capobanda, direttore) | cliente | passaggio 8 (L4 ⛔) e pubblicazione con link (L11) |
| 9 | Verifiche cronologiche §5 (età 1996, tour 1998, estate 2004) e conflitti di dati (allievi 300/450, dischi 38/40) | cliente | passaggio 8 (E12, A9) |
| 10 | Liberatoria delle Serate: copre l'uso in un video di vendita? | cliente | passaggio 8 (L2 ⛔) |
| 11 | Pubblicare l'artifact Slides giro 1 da `deck/project/` e rilanciare `export_deck.py --check-h3` sull'artifact pubblicato. Attenzione L11: nel deck ci sono frasi di terzi senza consenso (moglie, batterista, capobanda), senza nomi | sessione principale + senior | passaggio 6 |
| 12 | Rework del senior sul deck giro 1 (manuale §10 passaggio 5) | Rocco | passaggio 6 |
| 13 | Audit indipendente (`/webinar-audit`, agente `auditor`) sul deck: la modalità automatica lo prevede dopo il passaggio 5 | senior | passaggio 7 |
| 14 | 17 segnaposto nel deck (§7): chiudere prima dell'onda (L1) | cliente | passaggio 8 |

## 14 · VERSIONI E FILE

| Versione | Data | Cosa | Dove |
|---|---|---|---|
| intake | 2026-09-30 | risposte del cliente (copia) e richieste partite (messaggi D, M5, E12) | `INTAKE_RITMOSICURO_risposte.md` · `INTAKE_RITMOSICURO_richiesta.md` |
| domino | 2026-09-30 | opzioni, 5 criteri, test competitor, mucca viola, stress test | `DOMINO_RITMOSICURO_opzioni.md` |
| architettura | 2026-09-30 | tabella dei blocchi, tesi, foglio, promesse, obiezioni vinte | `ARCHITETTURA_RITMOSICURO.md` |
| script v1 | 2026-09-30 | prima stesura (~4.800 parole) | `SCRIPT_RITMOSICURO_v1.md` |
| confronto | 2026-09-30 | 14 buchi contro Grassi e Mind Reset | `CONFRONTO_RITMOSICURO.md` |
| script v2 | 2026-09-30 | buchi chiusi (~5.700 parole) | `SCRIPT_RITMOSICURO_v2.md` |
| deck v1 copy | 2026-09-30 | 110 slide, bianco e nero, lint senza ⛔ | `DECK_RITMOSICURO_testo.md` · `LINT_RITMOSICURO.md` · `deck/project/` · ritorno: `deck/DECK_RITMOSICURO_export_ritorno.md` |
| decisioni | 2026-09-30 | D0-D5 simulate per il collaudo | `DECISIONI_RICHIESTE.md` |
