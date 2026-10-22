# CANCELLI — la pipeline webinar come la esegue il plugin

> **Cos'è:** per ogni passaggio della pipeline (manuale §10): cosa entra, cosa esce, quando si esce, cosa blocca e chi decide. È il file che leggono `webinar-pipeline`, `/webinar-stato`, `/webinar-avanti`, il tutor e l'Academy.
> **Cosa non è:** non riscrive il metodo né le regole. Il testo delle regole vive solo in `REGOLE_WEBINAR.md`; qui si citano i codici. Se una regola cambia, si cambia là.
> **Gerarchia delle fonti** (in caso di conflitto): `REGOLE_WEBINAR.md` > `MANUALE_WEBINAR_SCALERS.md` > skill > `BLUEPRINT_SLIDE_WEBINAR.md` > caso studio. I conflitti noti sono elencati in `REVISIONE.md` alla radice del repo: il plugin li segnala, non li risolve.

---

## Come si leggono i cancelli

- **⛔ bloccante** = una regola ⛔ di `REGOLE_WEBINAR.md`. Se è violata, il cancello non si chiude. Nessun override: le ⛔ non si derogano.
- **Avviso** = regola non ⛔. Si segnala; il senior può fare un override, che si scrive nel registro della scheda (§12) con data e motivo.
- **Uscita** = checklist verificabile. Ogni voce si controlla sulla scheda o sui file, non a sensazione. Le voci marcate 🤖 le controlla uno script (`scripts/`), le altre Claude o il senior.
- **Decisione umana** = il punto in cui il plugin si ferma e chiede. Tutto il resto lo porta avanti da solo in modalità automatica.

## Ruoli

| Ruolo | Chi | Cosa fa |
|---|---|---|
| **Copywriter** | chi lavora il webinar | lancia i comandi, risponde alle domande del plugin, scrive quando è in formazione |
| **Senior** | il copywriter senior del webinar (oggi: Rocco) | chiude i cancelli con una decisione umana, approva, firma la certificazione. Il suo nome va nella scheda al primo cancello |
| **Matteo** | owner del metodo | escalation: il senior lo coinvolge solo se vuole o se una decisione esce dal metodo (es. un override su una parola vietata dal cliente) |

**Chi firma la chiusura:** se il cancello ha una decisione 🧑, chi = il **senior** (anche in modalità automatica: il plugin registra la sua risposta); se non ne ha ed è chiuso in automatico, chi = `plugin`.

Ogni chiusura di cancello è una riga nel **registro decisioni della scheda (§12)** nel formato:

`| AAAA-MM-GG | Cancello N chiuso · <nome passaggio> · <nota> | <chi> | <file o slide> |`

`scripts/stato_scheda.py` legge queste righe per sapere a che passaggio sei. Niente riga = cancello aperto.

## Modalità

- **Guidata** (default quando il copy è in formazione o lo chiede): si ferma a ogni cancello per l'approvazione del senior, come dice il manuale §10.
- **Automatica** (`/webinar-avanti auto`): con l'intake compilato, porta il webinar fino al deck. Chiude da sola i cancelli la cui uscita è tutta verificata (riga di registro: "chiuso in automatico, criteri verificati", chi = `plugin`), e si ferma **solo** sulle decisioni umane segnate 🧑 qui sotto: scelta del Big Domino, offerta (prezzo e stack), prove mancanti, approvazioni che la scheda non può verificare. Il senior rilegge i cancelli chiusi in automatico con `/webinar-stato`.

## Convenzioni dei file (cartella del cliente)

Tutto vive in `<cartella cliente>/WEBINAR/` (regola M8). `<P>` = nome del prodotto in maiuscolo, senza spazi.

| File | Nasce al passaggio | Cosa contiene |
|---|---|---|
| `SCHEDA_WEBINAR_<P>.md` | 0 | copia compilata di `templates/TEMPLATE_SCHEDA_WEBINAR.md`. **Fonte unica di verità (M2 ⛔)** |
| `INTAKE_<P>_richiesta.md` / `INTAKE_<P>_risposte.md` | 0 e 2 | cosa si è chiesto al cliente; cosa ha risposto, **copiato identico** dal materiale del cliente (testo, mai audio: M4). Se l'intake arriva già completo al passaggio 0, si salva subito e il passaggio 2 diventa solo il controllo |
| `DOMINO_<P>_opzioni.md` | 1 | forma grezza, opzioni, 5 criteri, test competitor, mucca viola |
| `ARCHITETTURA_<P>.md` | 3 | tabella dei blocchi con minuti, credenza → fase → prova |
| `SCRIPT_<P>_v1.md`, `CONFRONTO_<P>.md`, `SCRIPT_<P>_v2.md` | 4 | script, tabella dei buchi, script corretto |
| `DECK_<P>_testo.md` | 5 | il deck in formato testo (`FORMATO_DECK.md`). È da qui che si costruisce l'artifact Slides |
| `deck/project/…` | 5 | i file dell'artifact Slides generati da `scripts/build_deck.py` |
| `AUDIT_<P>_<AAAA-MM-GG>.md` | 7 | tabella delle correzioni, stesso formato di `examples/mind-reset/AUDIT_DECK_V6_2026-09-30.md` |
| `DOMANDE_CLIENTE_<P>.md` | sempre | ogni `[DA CLIENTE]` aperto, con la slide o il blocco in cui serve. Si svuota man mano |

**Stato di liberatorie e consensi** (scheda §7 e §8): ✅ firmata/dato · ❌ mancante · — non serve (prova anonima, senza nome né volto). Una storia vera senza liberatoria si usa **anonima** (L2 ⛔).

## Segnaposto (niente invenzioni, a livello di sistema)

| Segnaposto | Quando | Chi lo chiude |
|---|---|---|
| `[DA CLIENTE: cosa serve]` | qualsiasi numero, risultato, data, nome, testimonianza o dettaglio biografico che **non è nella scheda o nei materiali del cliente** | il cliente, tramite `DOMANDE_CLIENTE_<P>.md` |
| `[PROOF: cosa]` | una prova visiva o video prevista ma non ancora arrivata (L1) | il cliente |
| `[INVENTATO]` | **il plugin non lo usa mai.** Le regole lo ammettono in bozza (A3), ma qui si preferisce `[DA CLIENTE]` o un caso logico (F9). Se lo trovi in un file, è un errore da chiudere prima dell'onda | — |

Claude non riempie mai un segnaposto con un'ipotesi. Un'ipotesi dichiarata si scrive `[IPOTESI: …]` (A5) e va validata.

---

## 0 · OFFERTA PRONTA

| | |
|---|---|
| **Skill** | `webinar-stack` (parte offerta) · `webinar-intake` (richiesta prove) |
| **Input** | brief del cliente, numeri, catalogo, KB del cliente se c'è (`CLAUDE.md`, `numeri-baseline.md`, `voce.md`) |
| **Output** | `SCHEDA_WEBINAR_<P>.md` aperta, §0-§2 compilate · `INTAKE_<P>_richiesta.md` con la sezione 4 (prove) già inviata |
| **⛔ bloccanti** | **A1** (ancore e valori veri) · **B4** (valore = beneficio) · **B10** (solo scarsità vera) · **M2** (la scheda esiste ed è l'unica fonte) |
| **Avvisi** | B1 B2 B3 B5 B6 B7 B8 B9 B11 B12 B13 · A6 A7 A9 |
| **🧑 Decisione umana** | **prezzo, IVA, rate, stack con valori, garanzia, scarsità.** Il plugin propone, il senior decide |

**Uscita:**
- [ ] 🤖 nessuna voce della scheda §2 è ❌ (B1)
- [ ] ogni valore dello stack ha una frase-beneficio, non un costo orario (B4 ⛔)
- [ ] ogni ancora è un prezzo praticato davvero o un'alternativa di mercato reale, con la fonte in scheda (B5, A1 ⛔)
- [ ] 🤖 valore totale tra 5 e 10 volte il prezzo, oppure override registrato (B5)
- [ ] prezzo finito sotto il tetto delle rate dichiarato (B6)
- [ ] la scarsità è un vincolo reale con il suo motivo, niente countdown né "ultimi posti" (B10 ⛔)
- [ ] la durata in §2 coincide con la scaletta reale del prodotto (A7; la promessa che la usa si scrive ai passaggi 3-4)
- [ ] un nome solo per prodotto, fasi e componenti, scritto nel glossario §9 (B13)
- [ ] richiesta delle prove partita (intake §4, messaggio tipo D) e segnata in scheda §13 (L1)
- [ ] riga "Cancello 0 chiuso" nel registro §12

## 1 · BIG DOMINO + MECCANISMO + METAFORA

| | |
|---|---|
| **Skill** | `webinar-big-domino` · agente `prospect-scettico` per lo stress test |
| **Input** | scheda §2 · obiezioni reali (intake §2.1 se già arrivato) · materiale del frontman · 4-5 concorrenti diretti |
| **Output** | `DOMINO_<P>_opzioni.md` · scheda §3 compilata e **congelata verbatim** |
| **⛔ bloccanti** | **A1** (il domino è vero) · **M2** |
| **Avvisi** | C1-C11 · D1-D6 · A5 |
| **🧑 Decisione umana** | **scelta del domino tra le opzioni** e dichiarazione di "versione ufficiale" (C9). Il plugin non sceglie |

**Uscita:**
- [ ] forma grezza scritta: "l'unico modo per ottenere X è Y, e l'unico modo per fare Y è con [frontman/prodotto]" (C1)
- [ ] 3-5 opzioni valutate sui 5 criteri, con una raccomandazione motivata (C2)
- [ ] test competitor su 4-5 concorrenti: nessuno può dire la stessa frase (C3)
- [ ] test della mucca viola: né mainstream né crazy (C6)
- [ ] versione breve (una frase) e lunga (diagnosi → tentativi falliti → dove sta il problema → domino → prodotto) (C7)
- [ ] il prodotto compare solo nella riga finale (C8)
- [ ] il meccanismo ha un nome pronunciabile (D2) e una metafora sola (D3)
- [ ] obiezione nascosta del prodotto individuata e disinnescata nel meccanismo (D6)
- [ ] il domino è vero: niente dato non dimostrato presentato come fatto (A1 ⛔, A5). Se un dato è discutibile ma il senior lo tiene, override registrato
- [ ] stress test del `prospect-scettico` fatto sulla versione scelta, risposte annotate
- [ ] domino breve e lungo verbatim in scheda §3 con ✅ e data (C9)
- [ ] riga "Cancello 1 chiuso · versione ufficiale" nel registro §12, chi = senior

## 2 · MATERIALE DEL CLIENTE

| | |
|---|---|
| **Skill** | `webinar-intake` · `webinar-epiphany-bridge` |
| **Input** | `templates/INTAKE_WEBINAR_CLIENTE.md` Parte 1 inviata · risposte del cliente per iscritto |
| **Output** | `INTAKE_<P>_risposte.md` · scheda §4-§9 compilate · `DOMANDE_CLIENTE_<P>.md` aggiornato |
| **⛔ bloccanti** | **A2** (biografia mai inventata) · **E2** (l'eroe si salva con lo strumento del domino) · **L2** (nome e volto solo con liberatoria) · **L4** (consenso dei terzi) · **M2** |
| **Avvisi** | E1 E3-E14 · F3 F4 · I6 · L1 L3 L5-L9 · M4 M5 · A4 A9 |
| **🧑 Decisione umana** | **prove mancanti:** per ogni credenza senza prova il senior sceglie tra (a) andare avanti con `[PROOF]`, (b) caso logico o kinda-like bridge (F9), (c) aspettare il cliente |

**Uscita:**
- [ ] ogni beat dell'Epiphany Bridge in scheda §5 ha una fonte (trascrizione o testo del frontman), nessun beat scritto da noi (A2 ⛔, E3)
- [ ] il "piano" della storia è lo strumento che il domino dichiara efficace (E2 ⛔)
- [ ] epifania e "prima volta che ha funzionato su di lui" sono due scene diverse (E4)
- [ ] il prodotto non compare nella storia (E5); le testimonianze stanno fuori (E6)
- [ ] cronologia controllata; le verifiche aperte sono in §5 e in `DOMANDE_CLIENTE_<P>.md` (E12)
- [ ] obiezioni reali elencate e raggruppate nelle tre credenze (F3)
- [ ] per ogni credenza: una storia vera che passa le 4 condizioni (F4), oppure la decisione umana sulle prove mancanti registrata
- [ ] 🤖 ogni prova in §7 ha lo stato della liberatoria; nessun nome/volto senza liberatoria (L2 ⛔)
- [ ] ogni terzo in §8 ha lo stato del consenso (L4 ⛔: può essere ancora ❌, ma allora compare nella lista di cosa blocca l'onda, e **nel testo resta senza nome né foto** finché il consenso non arriva)
- [ ] parole vietate del cliente copiate in §9 (L8)
- [ ] riga "Cancello 2 chiuso" nel registro §12

## 3 · ARCHITETTURA

| | |
|---|---|
| **Skill** | `webinar-tre-segreti` (credenze e storie) · `webinar-script` (tabella della struttura) |
| **Input** | scheda §2-§9 |
| **Output** | `ARCHITETTURA_<P>.md` · scheda §6, §10, §11 compilate |
| **⛔ bloccanti** | **A3** (niente storie di clienti inventate) · **E2** · **F12** (un'obiezione vinta non si riapre: si pianifica qui) · **M2** |
| **Avvisi** | F1 F2 F5-F11 F13 F14 · G1-G24 · C10 · D3 D4 |
| **🧑 Decisione umana** | **scelta dell'architettura delle credenze:** (A) una credenza per fase, come Mind Reset (F2), oppure (B) Little Known Big Difference in ogni step + muro finale, come Grassi (manuale §3.5). In entrambe la credenza esterna deve avere una prova. Poi approvazione della struttura (in modalità automatica: si chiude da sola se tutte le voci sotto sono verificate) |

**Uscita:**
- [ ] le tre credenze (veicolo, interna, esterna) collegate a fase/step, credenza nuova e prova (F1, F2)
- [ ] ogni prova è una storia vera, un caso logico attribuito o un kinda-like bridge; nessuna storia inventata (A3 ⛔, F9, F10)
- [ ] tabella dei blocchi con minuti stimati (circa 140 parole/minuto)
- [ ] dove torna la tesi (~4-5 volte, identica: C10)
- [ ] prove dopo ogni fase (G12) e mappa ricorrente delle tre fasi (G13)
- [ ] impegno attivo e dove torna: prezzo, garanzia, CTA (G9)
- [ ] promesse piantate e dove si chiudono → scheda §10 (G14)
- [ ] cosa compare solo nello stack → scheda §11 (G15)
- [ ] per ogni obiezione: il punto in cui viene vinta; dopo quel punto non torna, salvo una ripresa con funzione nuova (F12 ⛔)
- [ ] niente slide di servizio (G10); si apre con la promessa (G3)
- [ ] riga "Cancello 3 chiuso" nel registro §12

## 4 · SCRIPT

| | |
|---|---|
| **Skill** | `webinar-script` |
| **Input** | `ARCHITETTURA_<P>.md` · scheda completa · un webinar reale che converte come termine di confronto (G23: trascrizione se c'è; altrimenti `BLUEPRINT_SLIDE_WEBINAR.md` + deck Mind Reset in `examples/`) |
| **Output** | `SCRIPT_<P>_v1.md` → `CONFRONTO_<P>.md` → `SCRIPT_<P>_v2.md` |
| **⛔ bloccanti** | **A1** · **A2** · **A3** · **E2** · **F12** · **M2** (frasi congelate verbatim dalla scheda) |
| **Avvisi** | G1-G24 · E8 E9 E11 E13 E14 · D5 · H4 H5 · A4-A8 |
| **🧑 Decisione umana** | nessuna in modalità automatica, se l'uscita è verificata |

**Uscita:**
- [ ] 🤖 domino breve, domino lungo e promessa compaiono verbatim come in scheda (C9, M2 ⛔) · con `lint_deck.py` se lo script è scritto nel formato del deck (`### n · id · titolo`), altrimenti con una ricerca
- [ ] 🤖 nessun `[INVENTATO]`; ogni `[DA CLIENTE]` e `[PROOF]` è anche in `DOMANDE_CLIENTE_<P>.md` / scheda §7 e §13 (A3 ⛔)
- [ ] confronto fatto: tabella dei buchi con il blocco in cui ciascuno si chiude (G23)
- [ ] v2 scritta con i buchi chiusi
- [ ] gli esempi del prodotto esistono nella scaletta reale, oppure sono `[DA CLIENTE: verificare che esista]` (D5)
- [ ] nessuna obiezione vinta riaperta nei recap, nello stack, nel prezzo o nelle FAQ (F12 ⛔)
- [ ] riga "Cancello 4 chiuso" nel registro §12

## 5 · SLIDE COPY (giro 1: bianco e nero)

Il passaggio ha due tempi: **5a** lo fa il plugin (anche in automatico), **5b** è il rework del senior.

| | |
|---|---|
| **Skill** | `webinar-slide` |
| **Input** | `SCRIPT_<P>_v2.md` · `BLUEPRINT_SLIDE_WEBINAR.md` · scheda |
| **Output** | `DECK_<P>_testo.md` · artifact Slides (giro 1) · link e versione in scheda §0 e §14 |
| **⛔ bloccanti** | **H3** (titolo un blocco, corpo un blocco) · **F12** · **B10** (niente "ultimi posti"/countdown copiati dal deck di Alex) · **L4** (un artifact si condivide con un link: L11) · **M2** |
| **Avvisi** | H1 H2 H4-H11 · G14 G15 · I1 · A6 |
| **🧑 Decisione umana** | 5b: il rework del senior sul deck (si legge la versione live prima di toccare qualsiasi cosa: M6) |

**Uscita 5a** (automatica):
- [ ] 🤖 `lint_deck.py` senza errori ⛔; nessuna slide oltre ~220 parole (H2)
- [ ] 🤖 `build_deck.py` genera un solo `<h2>` e al più un `<p>` per slide (H3 ⛔); `export_deck.py --check-h3` sulla build: zero violazioni
- [ ] 🤖 stack slide ripetute identiche salvo le aggiunte, somme giuste (G17, A6)
- [ ] 🤖 nessuna voce "Non si dice" del glossario §9 nel testo visibile (H8)
- [ ] niente regia, flag o numeri di blueprint a schermo: stanno nelle note (H10)
- [ ] artifact Slides pubblicato (privato), link e versione in scheda; `export_deck.py --check-h3` sull'artifact pubblicato: zero violazioni
- [ ] se nel deck ci sono frasi, nomi o foto di terzi con consenso ❌: il link **non si condivide** fuori dal team finché il senior non dà l'ok esplicito, e le verifiche sono nelle note (L4 ⛔, L11)
- [ ] riga "Cancello 5a chiuso" nel registro §12

In modalità automatica, dopo 5a si lancia un **audit di controllo** sul giro 1 (M9: audit prima di ogni pubblicazione importante) e ci si ferma per 5b. Il cancello 7 formale si chiude dopo la grafica.

**Uscita 5b** (🧑 senior):
- [ ] rework del senior fatto e le sue mosse applicate a tutto il deck (manuale §10 passaggio 5)
- [ ] export testo aggiornato dalla versione live; lint rilanciato
- [ ] riga "Cancello 5 chiuso" nel registro §12, chi = senior

## 6 · GRAFICA (giro 2, su un duplicato)

| | |
|---|---|
| **Skill** | `webinar-slide` |
| **Input** | deck copy approvato · design system del cliente (scheda §1) · foto e prove arrivate |
| **Output** | artifact Slides grafico (duplicato) · export testo aggiornato |
| **⛔ bloccanti** | **H3** (il giro grafico non spezza i blocchi di testo) · **L2** · **L4** (terzi senza consenso in un deck condiviso: ci si ferma, L11) · **M2** |
| **Avvisi** | I1-I12 · L5-L7 L10-L12 |
| **🧑 Decisione umana** | pubblicare con terzi non ancora verificati (L11): solo con ok esplicito |

**Uscita:**
- [ ] 🤖 il copy è identico al deck approvato, slide per slide (`export_deck.py` + diff)
- [ ] 🤖 zero violazioni H3 sull'HTML
- [ ] design system del cliente, non inventato (I2)
- [ ] controllo a schermo di ogni slide toccata: niente testo sotto 24 px, niente foto tagliate male, niente sfondi sotto il testo (I9, I12)
- [ ] autorità separate dalle testimonianze (I8); credenziali con la loro prova visiva (I6)
- [ ] ogni terzo visibile ha consenso ✅ in §8, oppure ok esplicito a pubblicare con la verifica scritta nelle note (L4 ⛔, L11)
- [ ] riga "Cancello 6 chiuso" nel registro §12

## 7 · AUDIT

| | |
|---|---|
| **Skill** | `webinar-audit` · agente `auditor` (indipendente) · `scripts/lint_deck.py` |
| **Input** | **solo** l'export testo del deck (o lo script), la scheda, `REGOLE_WEBINAR.md` e le regole di parola del cliente. **Mai** la conversazione di produzione né le bozze |
| **Output** | `AUDIT_<P>_<data>.md` |
| **⛔ bloccanti** | **tutte**: **A1** **A2** **A3** **B4** **B10** **E2** **F12** **H3** **L2** **L4** **M2** **N5** |
| **Avvisi** | tutte le altre |
| **🧑 Decisione umana** | quali correzioni applicare (l'audit non tocca niente); le domande che l'auditor non può decidere |

**Uscita:**
- [ ] audit completo nel formato di riferimento: testata di 3 righe, tabella in ordine di slide, segnaposto e aperti, domande (massimo 8), cosa è pulito
- [ ] zero ⛔ aperte, oppure ogni ⛔ ha un responsabile e blocca esplicitamente il passaggio 8
- [ ] ogni ❌ della scheda ha un responsabile in §13
- [ ] correzioni approvate applicate sulla versione live, scheda aggiornata (§0, §12, §13, §14)
- [ ] riga "Cancello 7 chiuso" nel registro §12

L'audit si rilancia dopo ogni rework e prima di ogni pubblicazione importante (M9), non solo qui.

## 8 · RECITA E MESSA IN ONDA

| | |
|---|---|
| **Skill** | `webinar-pipeline` (checklist pre-volo) · skill A4a del pacchetto marketing per la meccanica |
| **Input** | deck finale · scheda |
| **Output** | webinar registrato · messaggio di pre-volo al cliente (intake, messaggio tipo E) · script di consegna per i venditori (`templates/CONSEGNA_WEBINAR.md`) |
| **⛔ bloccanti** | **A3** · **L2** · **L4** · **N5** (mai mandare il webinar senza la call successiva già fissata) · **M2** |
| **Avvisi** | N1-N4 · A4 |
| **🧑 Decisione umana** | via libera alla registrazione |

**Uscita:**
- [ ] 🤖 zero `[PROOF]`, `[DA CLIENTE]`, `[INVENTATO]` nel deck (L1, A3 ⛔)
- [ ] tutti i consensi dei terzi ✅ o i terzi tolti (L4 ⛔); tutte le liberatorie ✅ o prove anonime (L2 ⛔)
- [ ] pre-volo inviato al cliente e confermato (messaggio tipo E)
- [ ] ~10 prove recitate, cronometro alla prova generale (+30-40% per le digressioni) (N1, N2)
- [ ] i venditori hanno lo script di consegna e la regola: la call successiva si fissa prima di mandare il link (N5 ⛔)
- [ ] riga "Cancello 8 chiuso · in onda" nel registro §12

---

## Mappa delle ⛔ sui cancelli

| ⛔ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| A1 | ● | ● | | | ● | | | ● | |
| A2 | | | ● | | ● | | | ● | |
| A3 | | | | ● | ● | | | ● | ● |
| B4 | ● | | | | | | | ● | |
| B10 | ● | | | | | ● | | ● | |
| E2 | | | ● | ● | ● | | | ● | |
| F12 | | | | ● | ● | ● | | ● | |
| H3 | | | | | | ● | ● | ● | |
| L2 | | | ● | | | | ● | ● | ● |
| L4 | | | ● | | | | ● | ● | ● |
| M2 | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| N5 | | | | | | | | ● | ● |

`scripts/copertura.py` verifica che questa tabella resti vera: ogni ⛔ di `REGOLE_WEBINAR.md` deve comparire in almeno un cancello di questo file e in almeno un modulo dell'Academy.
