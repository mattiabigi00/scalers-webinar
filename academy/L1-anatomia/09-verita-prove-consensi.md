# L1.9 · Verità, prove, consensi

> **Cos'è:** il confine che non si passa: cosa è vero, cosa è ipotesi, cosa manca e come si segna; le prove, le liberatorie dei clienti e il consenso dei terzi. **Durata:** ~45 minuti. **Prerequisiti:** L1.2, L1.4, L1.5.
> **Regole:** A1-A9 con **A1 ⛔ A2 ⛔ A3 ⛔**, L1-L12 con **L2 ⛔** e **L4 ⛔**, I6-I8 · **Manuale:** §4.5, §11

---

## La regola in breve

> *"Convinciamo solo di cose vere. Usiamo la parola 'convincere' perché è effettivamente quello che facciamo — ma se convinciamo di qualcosa che non è vero siamo scammer, e noi non siamo scammer. Questa non è una nota etica di contorno: è un vincolo di progettazione."* (manuale §4.5)

**Le cinque ⛔ di questo modulo:**

| Codice | Regola | In parole semplici |
|---|---|---|
| **A1 ⛔** | Si convince solo di cose vere | domino, numeri, storie: se non sono veri, non si usano |
| **A2 ⛔** | Mai inventare la biografia del frontman | *"È l'unica cosa che fa crollare tutto il resto."* Ogni beat della storia ha una fonte |
| **A3 ⛔** | Mai storie di clienti inventate in un webinar che va in onda | se manca una storia: caso logico o kinda-like bridge (F9), non un'invenzione |
| **L2 ⛔** | Nome e volto di un cliente solo con liberatoria scritta | senza liberatoria, anonimo |
| **L4 ⛔** | Consenso dei terzi (ospiti, medici, personaggi) prima di usare frase, nome e foto in un contesto di vendita | le frasi da sottotitoli automatici si riascoltano sull'audio prima di andare in slide |

**Le altre A**, in una riga: ogni numero si verifica sulla fonte primaria (A4) · ciò che è inferenza si marca `[IPOTESI]` (A5) · tutti gli asset dicono lo stesso numero (A6) · durata promessa = durata reale (A7) · niente numeri di efficacia non misurati, lo fa meglio la garanzia (A8) · i conflitti di dati si risolvono prima di scrivere la slide (A9).

**Le altre L**, in una riga: la raccolta delle prove parte il giorno 0 (L1) · testimonianze di un servizio equivalente, dichiarate per quello che sono (L3) · medici: la frase è un'opinione sulla persona, mai un parere sul prodotto (L5) · personaggi famosi = incontri, non clienti (L6) · materiale visivo non alterato (L7) · parole vietate del cliente = default, override registrato (L8) · lessico sanitario (L9) · la prova documentale batte la prova sociale (L10) · il deck condiviso con link è pubblico (L11) · si sfocano i dati personali, mai la prova (L12).

**Come si segna quello che non sai** (`references/CANCELLI.md`, "Segnaposto"):

| Segnaposto | Quando | Chi lo chiude |
|---|---|---|
| `[DA CLIENTE: cosa serve]` | numero, risultato, data, nome, testimonianza o dettaglio biografico che **non è nella scheda o nei materiali del cliente** | il cliente, tramite `DOMANDE_CLIENTE_<P>.md` |
| `[PROOF: cosa]` | una prova visiva prevista ma non ancora arrivata (L1) | il cliente |
| `[IPOTESI: …]` | un'inferenza dichiarata, da validare (A5) | il senior o il cliente |
| `[INVENTATO]` | **il plugin non lo usa mai.** Le regole lo ammettono in bozza (A3); se lo trovi in un file, è un errore da chiudere prima dell'onda | — |

*"Claude non riempie mai un segnaposto con un'ipotesi."* E neanche tu.

## Esempio buono

**Prove e liberatorie tracciate in scheda** (`examples/mind-reset/SCHEDA_WEBINAR_MIND_RESET.md` §7, due righe):

| Prova | Tipo | Dove | Liberatoria | Stato |
|---|---|---|---|---|
| Muro di testimonianze ("centinaia") | screenshot, messaggi, email | r13w | ❌ | ❌ |
| Foto delle sessioni | foto | r08 | ✅ consenso dichiarato 25/9 | 🟡 |

**Testimonianze di un servizio equivalente, dichiarate** (L3). Scheda §7: *"Testimonianze del coaching dal vivo **usabili** (Matteo 23/9: 'è lo stesso prodotto'), presentate come 'persone che hanno fatto questo lavoro con me'."*

**Medici come supporto alla persona** (L5). Deck v6, slide 22 · s021f: *"I miei anni di studio e di lavoro sono stati supportati da medici e psicologi come:"*. E la nota di q_vernetti: *"Le parole del medico riguardano Gianluca, non il prodotto: non presentarle come parere clinico su Mind Reset."*

**Terzi tracciati con consenso e audio** (L4 ⛔). Scheda §8 (una riga): *"Gurudev Sri Sri Ravi Shankar · «Tu hai un grande compito da svolgere» · dopo 'La voce' (q_gurudev) · ❌ (tramite Art of Living) · ❌"*. Consenso e audio riascoltato hanno una colonna ciascuno.

**Il numero di efficacia tolto** (A8). Nota di r13: *"Tolto il WhatsApp (va solo nello stack) e il 1000%."* Al suo posto lavora la garanzia, che è verificabile.

**La durata vera** (A7). 21 + 1 + 21 = 43 giorni, *"non 42"* (A7); l'audit trova *"43 giorni ovunque, nessun 42 nel testo visibile"*.

**Il cliente protetto anche nelle FAQ.** Slide 122 · s147: *"E il tuo nome non lo usiamo mai, da nessuna parte, senza il tuo consenso scritto."*

## Esempio sbagliato e perché

**1 · Le storie di Marco, Davide e Paolo** (caso studio, passaggio 3): *"li abbiamo integrati con parti inventate marcate `[INVENTATO]`, e Paolo era inventato da cima a fondo. Il 25/9 Matteo le ha tolte tutte."* **A3 ⛔.** E la scheda §6: *"Le storie di Marco, Davide e Paolo sono state tolte il 25/9 (Paolo era inventato, gli altri avevano benefici inventati). Non vanno citate da nessuna parte (regola F13)."*

**2 · Le citazioni prese dai sottotitoli automatici** (L4 ⛔). Nota di q_gurudev: *"The Mind Live #12, 24:39–24:56 (dai sottotitoli automatici YouTube). NUOVA 30/9. Prima di pubblicare: riascoltare l'audio e chiedere il consenso all'ospite."* Audit, riga 30 (⛔): *"Consensi dei terzi ❌ e audio non riascoltato per tutte e 6 le citazioni; Vernetti e Maniscalco senza ok; foto con Amadeus, Bonolis, Roberto Carlos. Pubblicato con l'ok di Matteo (L11), ma **prima della registrazione vanno chiuse tutte**."* Chi non dà il consenso esce dal deck.

**3 · Il famoso che sembra un cliente** (L6). Slide 21 · s021e: la foto *"Con Roberto Carlos"* sta sopra *"Con me lavorano imprenditori, manager, attori e atleti di livello mondiale…"*. Audit, riga 10 (alta): *"sembra un cliente. La scheda lo registra come incontro."* Stesso problema per Bonolis nella slide TV (riga 8).

**4 · La promessa di prove che non ci sono** (L1, L2 ⛔). Slide 73-74 · r13, r13w: *"E a dimostrarlo ci sono centinaia di testimonianze."* e poi *"Screenshot di messaggi, recensioni e testimonianze, tanti, uno accanto all'altro, a muro. Inserire qui."* Audit, riga 19: *"Riempire con prove vere e liberatorie; se non arrivano, togliere 'centinaia' e 'stai per vedere'."*

**5 · La biografia da verificare** (A2 ⛔, E12). Scheda §5: *"verificare 'diciassette' vs 'sette'"*; audit, riga 15: anni di studio che non tornano (*"oltre vent'anni"*, *"più di quindici anni"*, *"15 anni di studio"*). Non si sceglie noi il numero "più probabile": si chiede al frontman.

**6 · Il testo che non combacia con le prove** (A4, I6). Caso studio, passaggio 6: *"Il testo del 'Chi sono' non combaciava con le foto (Canale 5 contro Rai 2, 5 libri contro 7)."* Regola I6: *"Il testo si allinea alle prove disponibili, non il contrario."* E la scheda §4 ha una riga ⛔ di cose da non dire mai: *"'I Maghi della Mente' come programma TV (è un gruppo online) · 'La prova del mentalist' finché non c'è il fotogramma con un solo logo"* (L7).

**7 · Il conflitto di dati lasciato aperto** (A9). L'ancora del percorso dal vivo: 10.000 € in call del 9/9, 4.500-5.500 € nel catalogo della KB (scheda §2, 🟡; aperto n. 10). Si sceglie un valore, si scrive in scheda con la fonte, e il conflitto nella KB va chiuso.

> **Attenzione:** A1 è ⛔, ma il 95/5 del domino di Mind Reset è segnato nel deck come *"dato non dimostrato"* e tenuto con un override di Matteo; `CANCELLI.md` (passaggio 1) prevede un *"override registrato"* per un dato discutibile nel domino. Le due cose non stanno insieme: le ⛔ non si derogano. Nei tuoi webinar: dato non verificato = `[IPOTESI: …]` e decisione del senior prima di scrivere. Vedi anche L1.2. Conflitto registrato in `REVISIONE.md` alla radice del repo.

## Gli errori tipici

- **Riempire un buco con un numero "plausibile"** invece di `[DA CLIENTE: …]` (A1 ⛔, A4).
- **Rendere più bella una testimonianza vera** con benefici inventati (A3 ⛔: è quello che è successo con Marco e Davide).
- **Mettere nome e volto di un cliente** senza liberatoria scritta (L2 ⛔).
- **Citare un ospite di un podcast** dai sottotitoli, senza riascoltare e senza consenso (L4 ⛔).
- **Medici nel muro delle testimonianze**, o citati come se approvassero il prodotto (L5, I8).
- **Chiedere le prove alla fine.** *"Le prove si chiedono il primo giorno. Altrimenti si scrive con i segnaposto e si finisce a inventare."* (caso studio, "Le cinque cose da ricordare").

## Nel plugin

- **Skill:** `webinar-intake` manda la richiesta delle prove **al passaggio 0** (messaggio tipo D, `/webinar-cliente D`) e registra lo stato delle liberatorie (scheda §7) e dei consensi (scheda §8). `webinar-epiphany-bridge` monta solo beat con una fonte (A2 ⛔).
- **Cancelli:** A1 ⛔ blocca 0, 1, 4, 7 · A2 ⛔ blocca 2, 4, 7 · A3 ⛔ blocca 3, 4, 7, 8 · L2 ⛔ e L4 ⛔ bloccano 2, 6, 7, 8. Decisione 🧑 al cancello 2: per ogni credenza senza prova, (a) avanti con `[PROOF]`, (b) caso logico o kinda-like bridge, (c) aspettare il cliente. Al cancello 6: pubblicare con terzi non verificati solo con ok esplicito (L11).
- **Controlli automatici:** `scripts/lint_deck.py` conta tutti i segnaposto e segnala come ⛔ ogni `[INVENTATO]` (A3); segnala gli importi in euro che non sono in scheda (A4 · A6). Cancello 8: 🤖 *"zero `[PROOF]`, `[DA CLIENTE]`, `[INVENTATO]` nel deck"*. `scripts/stato_scheda.py` elenca le voci ❌ di §7 e §8. Il cancello 2 marca 🤖 anche *"ogni prova in §7 ha lo stato della liberatoria"*, ma oggi nessuno script lo verifica voce per voce: si controlla sulla scheda.
- **Agente:** `auditor`, controlli 10 ("Verità"), 12 ("Segnaposto"), 13 ("Terzi e prove").

---

## Domande di verifica

**1. Il frontman in call dice "ho aiutato circa tremila persone". Nella KB c'è scritto 2.100. Cosa scrivi nella slide?**

<details><summary>Risposta attesa</summary>

Niente dei due finché il conflitto non è risolto (A9): si segnala al senior, si sceglie un valore con la sua fonte, lo si scrive in scheda e solo dopo va in slide. Nel frattempo `[DA CLIENTE: numero di persone aiutate, fonte]` (A4).
</details>

**2. Hai una bella frase di uno psicologo ospite del podcast del cliente, trascritta dai sottotitoli automatici. Cosa manca prima di metterla in slide?**

<details><summary>Risposta attesa</summary>

Il riascolto dell'audio e il consenso dell'ospite a usare frase, nome e foto in un contesto di vendita (L4 ⛔). E va presentata come opinione sulla persona, non come parere sul prodotto (L5), in una scheda sua, non nel muro delle testimonianze (I7, I8).
</details>

**3. Manca una storia per la credenza esterna e il webinar va registrato tra tre giorni. Il cliente propone: "Scrivete voi una storia verosimile, tanto è anonima." Cosa rispondi?**

<details><summary>Risposta attesa</summary>

No: A3 ⛔, mai storie di clienti inventate in un webinar che va in onda, anonime o no. Le opzioni sono un caso logico (una storia pubblica attribuita correttamente, raccontata per intero, F9-F10) o un kinda-like bridge. La scelta è del senior (cancello 2).
</details>

## Esercizio flash (5-10 minuti)

*Esempio costruito, inventato per l'esercizio: non usarlo fuori dall'Academy.*

Bozza di una slide di "Lievita". La scheda contiene: 30 giorni di durata; 312 iscritti alla prima edizione (fonte: gestionale); nessuna liberatoria raccolta; nessun consenso di terzi.

> *"Oltre 500 persone hanno già sfornato il loro primo pane con Lievita, con un tasso di successo del 97%. Come Giulia Marchetti di Bergamo, che dopo due settimane portava il pane in ufficio (guarda la sua foto qui sotto). Lo chef Arturo Benzi, ospite del nostro podcast, ha detto: 'È il metodo più serio che abbia visto'. In soli 25 giorni anche tu avrai il tuo pane perfetto."*

Per ogni affermazione decidi: resta così / diventa `[DA CLIENTE: …]` / diventa `[PROOF: …]` / diventa `[IPOTESI: …]` / si toglie. Scrivi accanto il codice della regola. Poi elenca cosa manca (liberatorie, consensi, verifiche) prima che la slide possa andare in onda.
