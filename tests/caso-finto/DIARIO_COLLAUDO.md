# DIARIO DEL COLLAUDO · plugin scalers-webinar · caso finto "Ritmo Sicuro"

> **Cosa:** collaudo end-to-end della pipeline, da `/webinar-nuovo "Ritmo Sicuro"` a `/webinar-avanti auto` fino al deck (passaggio 5), su un cliente dichiaratamente inventato (Fabrizio Nardelli).
> **Quando:** 2026-09-30. **Senior:** Rocco, simulato: ogni decisione 🧑 è scritta in `WEBINAR/DECISIONI_RICHIESTE.md` e registrata in scheda §12 con chi = "Rocco (simulato · collaudo)".
> **Letti:** comandi `webinar-nuovo`, `webinar-avanti`; skill `webinar-pipeline`, `-stack`, `-intake`, `-big-domino`, `-epiphany-bridge`, `-tre-segreti`, `-script`, `-slide`; agente `prospect-scettico`; `references/` (CANCELLI intero, REGOLE intero, MANUALE §1-2, §4-8, §10-11, BLUEPRINT §0-6, FORMATO_DECK intero), `templates/`, `REVISIONE.md`, `examples/mind-reset/` (scheda e deck, come esempio). **Non letti** (come da consegna): `cliente/NOTE_COLLAUDO_trappole.md`, `tests/regressione-mind-reset/`, `tests/palestra/`, `academy/*/chiav*`.
> **Esito in breve:** cancelli 0-5 chiusi nel registro; deck testo di 110 slide (~5.700 parole), lint senza ⛔ né alte, H3 = 0 violazioni sulla build locale, andata e ritorno senza perdite su titoli e corpi. 33 punti in cui le istruzioni si inceppano, elencati in fondo con la correzione proposta.

---

## `/webinar-nuovo "Ritmo Sicuro"`

**Fatto.** Cartella `tests/caso-finto/WEBINAR/` già esistente e vuota; nessuna scheda precedente. Copiato il template in `SCHEDA_WEBINAR_RITMOSICURO.md`, compilati solo cliente, prodotto, frontman, §1 e data; senior Rocco nella prima riga del registro. Creato `DOMANDE_CLIENTE_RITMOSICURO.md` vuoto. Nessuna KB del cliente (niente `CLAUDE.md`, `voce.md`, `numeri-baseline.md`): §1 punta alle sezioni dell'intake. Intake copiato in `WEBINAR/INTAKE_RITMOSICURO_risposte.md` (identico all'originale, verificato con `cmp`).
**Script:** `stato_scheda.py` → passaggio 0, "nessuna voce ❌" (falso negativo, J3).
**Inceppamenti:** J1, J2, J3, J5.

## Passaggio 0 · Offerta pronta

**Fatto.** Offerta chiusa in scheda §2 (nome, fasi, durata, impegno, prezzo, IVA, rate, ancore, garanzia, CTA, bonus, regalo, scarsità, stack con benefici). Decisione D0 simulata (prezzo 1.990 € + IVA, stack 13.000 €, garanzia «Rifai con me», CTA call già fissata). Glossario §9 con i nomi (B13). Richiesta prove (messaggio D) e messaggio M5 sulla scarsità in `INTAKE_RITMOSICURO_richiesta.md`.
**⛔ rifiutate (non decisioni):** "restano 5 posti" chiesto dal cliente (B10).
**Uscita:**
- ✅ 🤖 §2 senza ❌ (script: nessuna ❌; le 🟡 sono ammesse)
- ✅ ogni valore con frase-beneficio (B4)
- ✅ ancore vere con fonte (Palco Vero 3.400 € al passato, lezioni 70 €/h, mental coach 120 €)
- ✅ 🤖 valore/prezzo 6,5 (script: "13.000 / 1.990 = 6.5 volte · ok")
- ✅ prezzo finito 2.427,80 € sotto il tetto Klarna (2.490 + IVA = 3.037,80 € lo sforava: scartato)
- ✅ scarsità vera con motivo (24 posti, 12 gennaio 2027)
- ➖ durata promessa = durata reale: verificabile solo sulla durata della scaletta (8 settimane); la promessa si scrive dopo (J8)
- ✅ un nome solo, glossario §9
- ✅ richiesta prove partita e in §13
- ✅ riga "Cancello 0 chiuso"
**Inceppamenti:** J6, J7, J8, J9.

## Passaggio 1 · Big Domino

**Fatto.** `DOMINO_RITMOSICURO_opzioni.md`: mercato, LKBD, 4 opzioni in forma grezza, 5 criteri, test competitor sui 5 concorrenti dell'intake (passa solo A, grazie a "uno scalino alla volta"), mucca viola, verità, raccomandazione. **Stress test:** eseguito nel ruolo dell'agente `prospect-scettico` (non c'era modo di lanciarlo come agente separato, J12), con i soli tre input previsti; esito e correzione (scalini nominati subito dopo la tesi) nel file §9. D1 simulata: opzione A congelata in scheda §3 (breve e lunga, meccanismo "gli otto scalini", metafora della scala, D6 "da uno schermo?").
**Uscita:** tutte ✅ (forma grezza, 3-5 opzioni, test competitor, mucca viola, versioni breve e lunga, prodotto solo nella riga finale, nome del meccanismo e una metafora, D6, domino vero senza dati, stress test, §3 verbatim, riga "Cancello 1 chiuso · versione ufficiale").
**Inceppamenti:** J12.

## Passaggio 2 · Materiale del cliente

**Fatto.** Scheda §4 (promessa, nemici, sospetto, foglio, credenziali con prova e stato), §5 (dieci beat, ognuno con la fonte nell'intake; E2 ✅, E4 ✅, E5 ✅, E10 la fase "snob per paura"), 5 verifiche cronologiche, §6 (10 obiezioni reali raggruppate), §7 (12 prove con stato della liberatoria), §8 (5 terzi), §9 (parole vietate). Tre messaggi al cliente (storia mancante, liberatoria di Simonetta, verifiche E12), 20 righe nuove in `DOMANDE_CLIENTE`. D2 simulata: credenza esterna con kinda-like bridge + fatti veri del frontman + prodotto.
**⛔ rifiutate:** storia "verosimile" per la credenza esterna (A3); nome e volto di Simonetta con solo consenso a voce (L2): storia anonima, video bloccato.
**Uscita:** ✅ beat con fonte · ✅ E2 · ✅ E4 · ✅ prodotto fuori dalla storia, testimonianze fuori · ✅ cronologia controllata, verifiche in §5 e nelle domande · ✅ obiezioni raggruppate · ✅ una storia vera per veicolo (Giorgio) e interna (anonima), decisione D2 per l'esterna · ✅ 🤖 liberatorie con stato (script: 3 prove senza liberatoria ✅, tutte segnalate) · ✅ terzi con stato (5 ❌ che bloccano l'onda) · ✅ parole vietate in §9 · ✅ riga "Cancello 2 chiuso".
**Inceppamenti:** J10, J11, J13, J14, J15.

## Passaggio 3 · Architettura

**Fatto.** D3 simulata: architettura A, ordine classico (camera → veicolo, ascoltatori → interna, live → esterna), "tre fasi". `ARCHITETTURA_RITMOSICURO.md`: 45 righe di tabella con minuti, tesi 5 volte, foglio con 3 ritorni, promesse piantate, solo-stack, obiezioni vinte e dove. Scheda §10 e §11.
**Uscita:** tutte ✅. Stima iniziale ~70 minuti, poi rivista (vedi passaggio 4).
**Inceppamenti:** J16.

## Passaggio 4 · Script

**Fatto.** `SCRIPT_RITMOSICURO_v1.md` (~4.800 parole) → `CONFRONTO_RITMOSICURO.md` (14 buchi contro Grassi e Mind Reset, 5 elementi del blueprint deliberatamente non adottati con il motivo) → `SCRIPT_RITMOSICURO_v2.md` (~5.700 parole, buchi marcati {B1}-{B14}). Il confronto ha trovato anche tre punti in cui la v1 aggiungeva cose non dette dal cliente ("quest'anno", "si prova la canzone", "solo per chi abitava vicino"): tolti. Durata rivista a ~40 minuti di testo (+30-40% digressioni): allungare oltre avrebbe voluto dire riempitivo (registrato in §12).
**Uscita:** ✅ frasi congelate verbatim (breve 4 volte, lunga tutte le frasi, promessa: verificato con uno snippet sui moduli del plugin, non con uno script dedicato, J17) · ✅ nessun `[INVENTATO]`, ogni `[DA CLIENTE]`/`[PROOF]` in DOMANDE/§7 · ✅ confronto · ✅ v2 · ✅ D5 esempi dalla scaletta · ✅ F12 · ✅ riga "Cancello 4 chiuso · chiuso in automatico" (chi = plugin: nessuna decisione 🧑).
**Inceppamenti:** J17, J18.

## Passaggio 5 · Slide copy (giro 1)

**Fatto.** `DECK_RITMOSICURO_testo.md`: 110 slide in 4 blocchi, 5.258 parole di corpo + 429 di titoli; intro nell'ordine G3-G11; rallentatore di 9 slide; 4 statement identiche della tesi; 5 stack slide identiche salvo le aggiunte (4.000 → 7.500 → 13.000, poi + prezzo, poi + garanzia). Regia, fonti e verifiche nelle note.
**Script lanciati:**
- `lint_deck.py … --out LINT_RITMOSICURO.md`: prima passata ⛔ 0 · alta 0 · 1 "da verificare" (falso positivo, J19). Dopo le correzioni (asterischi del corsivo, segnaposto resi visibili): **⛔ 0 · alta 0 · bassa 0 · da verificare 1 · 17 slide con segnaposto**. Exit 0.
- `build_deck.py … --out WEBINAR/deck` → 110 file + `deck.json`, 4 sezioni. Controllo a parte: ogni slide ha 1 `<h2>` e al più 1 `<p>` (le 9 statement ne hanno 0).
- `export_deck.py WEBINAR/deck --check-h3`: **0 violazioni H3**. Andata e ritorno (`deck/DECK_RITMOSICURO_export_ritorno.md`): 110/110 slide, **titoli e corpi identici**, blocchi identici; perse come righe proprie le 25 `[immagini:]` (finiscono nelle note) e i 10 `[layout:]` (J29). Il lint sull'export dà lo stesso esito.
- `stato_scheda.py` a ogni cancello: letture coerenti col registro; ultimo stato: passaggio 6, cancelli 0-5 chiusi, 14 aperti in §13.
**Non fatto (come da consegna):** pubblicazione dell'artifact Slides (la fa la sessione principale); quindi H3 **non** verificato sull'artifact pubblicato. Audit `/webinar-audit` non lanciato (fuori dai passaggi 0-5; la modalità automatica lo prevede subito dopo il 5).
**Uscita:** ✅ 🤖 lint senza ⛔, nessuna slide oltre 220 parole (max 123) · ✅ 🤖 un `<h2>` e al più un `<p>`; ❌ `--check-h3` sull'artifact **pubblicato** (fatto sulla build locale) · ✅ 🤖 stack identiche, somme giuste · ✅ 🤖 nessuna voce "non si dice" a schermo (l'unico avviso è un falso positivo) · ✅ regia nelle note · ❌ rework del senior (non esiste nel collaudo: D5) · ✅ riga "Cancello 5 chiuso" con le due voci non verificate dichiarate.
**Avvisi aperti sul deck:** H2 densità: 47 slide su 110 sotto le 40 parole (il blueprint ne vuole circa un quarto: pesano il rallentatore, le statement, i segnaposto delle prove, le mappe); il deck è più corto dei riferimenti (~5.700 parole contro ~7.400 di Mind Reset e ~10.300 di Grassi) perché il materiale vero del cliente regge questa lunghezza. G11 indebolita: il nome del cantante resta fuori finché non c'è il consenso (L4).
**Inceppamenti:** J19-J33.

**Nota:** alle 20:58 la scheda è diventata di sola lettura (`-r--r--r--`) dopo la mia ultima scrittura: non l'ho modificata oltre. Il contenuto finale è completo (§0, §12, §13, §14 aggiornate).

---

## Trappole del materiale del cliente che il collaudo ha trovato (senza leggere le note)

| # | Cosa | Regola | Cosa ha fatto il plugin |
|---|---|---|---|
| 1 | "Nel webinar metterei che restano 5 posti" | B10 ⛔ | rifiutato, messaggio M5, scarsità vera (24 posti, 12/1/2027) |
| 2 | "Scrivetene una voi, verosimile" (storia 3) | A3 ⛔ | rifiutato, messaggio M5, D2 kinda-like bridge, storia vera richiesta |
| 3 | Simonetta: "firmata no… usatelo pure con nome e foto" | L2 ⛔ | storia anonima, video bloccato, liberatoria richiesta |
| 4 | 2.490 € + IVA = 3.037,80 € | B6 | scartato |
| 5 | "Agosto 1996, diciannove anni" ma nato nel 1974 | E12 | età tolta dallo script, verifica al cliente |
| 6 | "Solo studio per un sacco di anni" ma tour con Salvi nel 1998 | E12, A1 | `[DA CLIENTE]` visibile |
| 7 | Tour "dell'estate" 2004 ma "dal 2005 al 2009" | E12 | `[DA CLIENTE]` visibile |
| 8 | 300 allievi (§8) contro più di 450 (§5) | A9, A4 | `[DA CLIENTE]`, fuori dal domino |
| 9 | "Circa 40 dischi, forse 38" | A4 | `[DA CLIENTE]` |
| 10 | "Mezz'ora al giorno" (FAQ del cliente) contro 30-40 minuti (scaletta) | A9, A6 | vale la scaletta |
| 11 | Rai 1 senza fotogramma | I6 | `[PROOF]`, nota "senza prova la slide si toglie" |
| 12 | Liberatoria delle Serate firmata "per il locale" | L2 | uso in vendita da verificare |
| 13 | Testimonianze di Palco Vero senza liberatoria, servizio diverso | L2, L3 | solo anonime e dichiarate come percorso dal vivo |
| 14 | Mirko Salvi: "non gli ho chiesto niente" | L4 ⛔, L6 | non nominato nel deck; consenso richiesto |
| 15 | Frasi di moglie, batterista, capobanda | L4 | usate senza nomi, consenso chiesto (J15) |
| 16 | CTA "call di 20 minuti con Marta" + iscrizione diretta | G21, N5 ⛔ | nessun nome in slide, call già fissata, link secondario |
| 17 | Parole vietate (ansia, terapia, talento, sfondare…) e i concorrenti che dicono "ansia da palco" | L8, L9 | mai a schermo; il lint non segnala niente |
| 18 | «Il minuto prima» è sia il regalo sia un pezzo della settimana 4 | G14, B4 | fuori dal conteggio dello stack |
| 19 | Palco Vero come ancora: praticato, ma non più dal 2024 | A1, B5 | "costava", al passato |
| 20 | Bonus "entro 72 ore dal webinar, max 10": in un webinar registrato non si sa da quando contano | B10 ⛔, B11 | 🟡 con `[DA CLIENTE]` visibile |
| 21 | Serate a giugno, ma l'edizione parte il 12 gennaio 2027 | A6 | data della Serata chiesta, non detta |
| 22 | "Il locale che si trova da solo" per chi è lontano | D5 | FAQ con verifica aperta |
| 23 | Recensioni "della scuola": quale scheda? | A4 | domanda |

---

## Dove le istruzioni del plugin si inceppano (e la correzione proposta)

Gravità: **A** = blocca o falsa la pipeline · **M** = porta a un errore probabile · **B** = attrito o imprecisione.

| # | Dove (file:riga) | Problema | Gr. | Correzione proposta |
|---|---|---|---|---|
| J1 | `commands/webinar-nuovo.md:3` e punto 1 | `argument-hint: <cliente> <prodotto>`, ma il comando si lancia con il solo prodotto ("Ritmo Sicuro"): nessuna istruzione per ricavare il cliente | B | punto 1: "se l'argomento ha solo il prodotto, prendi il cliente dall'intake o dalla cartella; se non è univoco, chiedi" |
| J2 | `templates/TEMPLATE_SCHEDA_WEBINAR.md:4` | percorsi `01_SCALERS/CLIENTI/…` e `06_OPERATIONS/WEBINAR/TEMPLATE_…` che nel plugin non esistono | B | "`<cartella cliente>/WEBINAR/SCHEDA_WEBINAR_<P>.md` · modello: `templates/TEMPLATE_SCHEDA_WEBINAR.md`" |
| J3 | `scripts/stato_scheda.py:67-73` + template `:65` | su una scheda appena aperta dice "nessuna voce ❌" (le celle vuote non contano) e conta come ❌ e 🟡 la riga guida del template "(✅ / 🟡 / ❌ · data)" | A | in `aperti()`: contare come aperte le righe della tabella §2 con la colonna Stato vuota; escludere le righe che contengono "(✅ / 🟡 / ❌" |
| J4 | `scripts/stato_scheda.py:71` | conta ogni riga con il glifo ❌ in qualunque sezione, anche nel registro §12 ("§2 senza ❌") | M | leggere solo la colonna Stato/Consenso/Liberatoria; saltare §12 e §14 |
| J5 | `skills/webinar-intake/SKILL.md` §"Passaggio 0" e `references/CANCELLI.md:68` | la pipeline presume: prove chieste al passaggio 0, Parte 1 al passaggio 2. Se l'intake torna già completo (questo caso) non si sa cosa scrivere in `INTAKE_<P>_richiesta.md`, né se il messaggio A serve | M | aggiungere: "se la Parte 1 è già tornata: niente messaggio A; `INTAKE_<P>_richiesta.md` raccoglie solo le richieste di completamento (D, M5, E12) con la data" |
| J6 | `references/CANCELLI.md:33` e ogni cancello | chi firma la riga di chiusura quando il cancello ha una decisione 🧑: la modalità automatica dice chi = plugin, il cancello 1 dice chi = senior, gli altri non dicono niente | M | regola unica in "Modalità": "cancello con decisione 🧑: chi = senior (dopo la sua risposta); senza 🧑: chi = plugin" |
| J7 | `references/CANCELLI.md:81` | "la durata promessa = la durata reale" è nell'uscita del passaggio 0, ma la promessa si scrive in §4 al passaggio 2-3 | B | al passaggio 0: "la durata in §2 coincide con la scaletta"; spostare A7 sulla promessa al cancello 3 |
| J8 | `templates/TEMPLATE_SCHEDA_WEBINAR.md` §2 | una sola riga "Bonus" e due ancore: con due alternative di mercato e un bonus con condizioni si comprime tutto in una cella | B | righe "Ancora 3" e "Condizioni del bonus" facoltative |
| J9 | `templates/INTAKE_WEBINAR_CLIENTE.md:178` | il messaggio D chiede sempre "Due decisioni tue: [regalo] · [bonus]", anche quando sono già nell'intake §3 e §7 | B | "(solo se non sono già nell'intake; altrimenti chiedi le conferme aperte)" |
| J10 | `scripts/stato_scheda.py:127` + template §7 | una prova è "senza liberatoria" se la cella non ha ✅ né "—": la convenzione del trattino (= non serve, anonima) non è scritta da nessuna parte; "anonima, non serve" viene contata come mancante | M | nel template §7, sotto la tabella: "Liberatoria: ✅ firmata · ❌ manca · — non serve (prova anonima o pubblica)" |
| J11 | `references/CANCELLI.md` passaggio 2, Input | "Parte 1 inviata" e "risposte in `INTAKE_<P>_risposte.md`": nessuna istruzione su dove sta l'originale del cliente né se va copiato o collegato | B | "copia il file del cliente in `WEBINAR/INTAKE_<P>_risposte.md` senza modificarlo; se arriva un'altra versione, nuova data in testa" |
| J12 | `skills/webinar-big-domino/SKILL.md` §"Stress test" | "Lancia l'agente prospect-scettico": nessuna alternativa se l'ambiente non permette sotto-agenti | M | "se non puoi lanciarlo, simulalo in un blocco separato che legge solo i tre input (avatar, obiezioni, frase) e dichiaralo nel file" |
| J13 | `skills/webinar-intake/SKILL.md` §"🧑 Prove mancanti" | una storia vera senza liberatoria (Simonetta) non è una "prova mancante" ma nemmeno una prova piena: il caso non è previsto | M | "storia vera senza liberatoria: si usa anonima (niente nome, volto, città, video) e non serve la decisione 🧑; il video resta bloccato fino alla liberatoria" |
| J14 | `references/REGOLE_WEBINAR.md` L4 + template §8 | non è detto se i familiari e le persone private citate nella storia del frontman (moglie, amico, capobanda) sono "terzi" che richiedono consenso; L4 parla di "ospiti, medici, personaggi" | M | decisione di Matteo da scrivere in L4: es. "persone private nella storia del frontman: senza nome e senza foto; frase citata con consenso chiesto, non bloccante" |
| J15 | `references/CANCELLI.md` passaggio 2 | l'uscita chiede lo stato del consenso dei terzi ma non cosa fare nel testo finché è ❌ (nominarli o no) | B | "finché il consenso è ❌: nel deck senza nome né foto; se il nome è essenziale, `[DA CLIENTE: consenso di …]` visibile" |
| J16 | `skills/webinar-script/SKILL.md` §3 e `references/REGOLE_WEBINAR.md` H1 | l'architettura stima i minuti prima di scrivere e H1/manuale presumono ~10.000 parole; nessuna regola dice cosa fare se il materiale vero ne regge meno (qui ~5.700): il rischio è gonfiare con riempitivo | M | in H1: "la lunghezza segue il materiale vero; mai riempitivo per arrivare a 10.000 parole"; al cancello 4: "parole della v2 / 140 = minuti; se lo scarto con l'architettura supera il 20%, aggiorna §0 e registra" |
| J17 | `references/CANCELLI.md` passaggio 4 (voci 🤖) e `skills/webinar-script/SKILL.md` | le voci 🤖 del cancello 4 (frasi congelate, segnaposto) non hanno uno script: `lint_deck.py` legge solo il formato `### n · id · titolo`, e il formato dello script consigliato dalla skill (`## Blocco n`, `[SLIDE: …]`) non lo è | M | un'opzione `lint_deck.py --script` che legge tutto il testo, oppure scrivere lo script con intestazioni `### n · id · titolo` |
| J18 | `skills/webinar-script/SKILL.md` §Confronto | il confronto G23 non chiede di controllare la lunghezza (parole/minuti) contro il riferimento: qui era il buco più grande | B | aggiungere "lunghezza per blocco contro il riferimento" all'elenco dei controlli |
| J19 | `scripts/lint_deck.py:129` | glossario confrontato senza distinguere maiuscole: «Palco Vero» (nome del vecchio percorso, in "non si dice") segnala 11 slide che dicono "un palco vero" | M | se il termine comincia con una maiuscola, confronto sensibile alle maiuscole |
| J20 | `scripts/lint_deck.py`, parole vietate (radice `base[:-2]`) | "sfondare" diventa `sfond\w*` e prende "sfondo"; "paziente" prenderebbe "pazienza": falsi positivi probabili | B | radice solo per parole ≥ 9 lettere, oppure lista di eccezioni |
| J21 | `references/FORMATO_DECK.md:28` · `scripts/build_deck.py` `inline()` · `references/BLUEPRINT_SLIDE_WEBINAR.md:63` | il blueprint vuole citazioni e dialoghi in corsivo, ma il formato ha solo `**…**` e `==…==`: scrivendo `*"…"*` gli asterischi vanno a schermo e il lint non se ne accorge | M | supportare `*…*` → `<i>` in `build_deck.py` e `<i>` → `*` in `export_deck.py`, e documentarlo; oppure vietarlo in FORMATO_DECK e farlo segnalare al lint |
| J22 | `scripts/deckfmt.py` (`LAYOUT_RE … if m and not body`) + `FORMATO_DECK.md:46` | `[layout: x]` funziona solo come prima riga sotto `###`; messo dopo il corpo diventa testo a schermo, senza avviso | M | il lint segnala ogni riga `[layout:` dentro il corpo (H10) |
| J23 | `FORMATO_DECK.md` §1 · `lint_deck.py` `VAL_RE`/`TOT_RE` | la sintassi delle stack slide non è documentata; il lint riconosce solo "(valore 1.500 €)" e "Valore totale: 13.000 €". La notazione del blueprint ("(valore €X)", "Valore totale €18'500") **salta in silenzio** il controllo delle somme e delle ripetizioni (verificato) | A | documentare la sintassi in FORMATO_DECK e accettare l'euro prima e dopo il numero nelle due regex |
| J24 | `FORMATO_DECK.md` §4 · `skills/webinar-slide/SKILL.md:23` · `CANCELLI.md:192` | "un solo `<p>` per slide": le statement non ne hanno nessuno | B | "al più un `<p>`" |
| J25 | `scripts/lint_deck.py` | nessun controllo sulla quota di slide leggere (~1/4, H2) né sulla densità minima: 47 slide su 110 sotto le 40 parole passano senza avviso | B | avviso se la quota di slide sotto 40 parole supera il 35% o se la mediana delle dense è sotto 90 |
| J26 | `commands/webinar-avanti.md:11` vs `CANCELLI.md` (ordine 5 → 6 → 7) vs `scripts/stato_scheda.py:31` | l'automatica dice "dopo il 5 lancia /webinar-audit"; CANCELLI e lo script mettono la grafica (6) prima dell'audit (7) e la "prossima azione" del 6 non cita né la pubblicazione né l'audit | M | allineare: dopo il 5 → pubblicazione giro 1 → audit → rework del senior → 6; aggiornare `PROSSIMA[6]` |
| J27 | `CANCELLI.md:192, 196` vs `commands/webinar-avanti.md:11` | il cancello 5 contiene voci impossibili in automatica ("--check-h3 sull'artifact pubblicato", "rework del senior fatto"), mentre l'automatica deve arrivare al "deck giro 1 pubblicato": non si sa se il 5 si chiude prima o dopo il rework, né chi lo chiude | A | dividere: **5a** deck testo + build + lint + H3 locale (automatico) · **5b** pubblicato + `--check-h3` sull'artifact + rework del senior (🧑, chi = senior) |
| J28 | `CANCELLI.md` passaggio 5, riga ⛔ | L4/L11 (terzi senza consenso in un deck condiviso con link) sono solo al cancello 6, ma anche l'artifact del giro 1 si condivide con un link | M | aggiungere al 5: "prima di pubblicare con link: terzi in §8 senza consenso fuori dal testo visibile o ok esplicito (L11)" |
| J29 | `scripts/export_deck.py:143` · `scripts/build_deck.py:55-61` | andata e ritorno: `[immagini:]` torna dentro le note ("IMMAGINI PER LA GRAFICA: …") e `[layout:]` si perde; dopo il primo rework del senior il file testo perde entrambe | M | `build_deck.py` scrive `data-layout` sulla `<section>` e le immagini in un attributo; `export_deck.py` li rilegge e ricostruisce le due righe |
| J30 | `scripts/stato_scheda.py:36, 146` vs `lint_deck.py` | due conteggi dei segnaposto diversi sullo stesso deck (22 contro 17): lo stato conta anche le note | B | lo stato usa `deckfmt` e conta solo il testo visibile, come il lint |
| J31 | `REGOLE_WEBINAR.md` B10 / A6 | webinar **registrato** con una scarsità datata ("parte il 12 gennaio 2027"): nessuna regola su come si tiene vera nel tempo | M | in B10: "nei webinar registrati la slide della data e dei posti si aggiorna a ogni edizione; è una voce del pre-volo (messaggio E)" |
| J32 | `skills/webinar-stack/SKILL.md` passo 3 | il regalo per chi resta fino alla fine può essere anche un componente dello stack (qui «Il minuto prima»): non si sa se va valorizzato | B | "se il regalo è anche un componente: nello stack senza valore, dichiarato come il regalo di oggi" |
| J33 | `REGOLE_WEBINAR.md` G11 vs L4 | G11 vuole "credenziali con nomi propri"; quando il nome proprio richiede un consenso che non c'è (il cantante), non è detto cosa prevale | B | in G11: "un nome proprio che richiede consenso (L4) entra solo con il consenso; fino ad allora la credenziale si dice senza nome" |

## Cosa resta per la sessione principale

1. Pubblicare l'artifact Slides dal contenuto di `WEBINAR/deck/project/` (titolo "Webinar Ritmo Sicuro — v1 copy"), poi rileggerlo e rilanciare `export_deck.py --check-h3` sui file letti.
2. Attenzione L11 prima di condividere il link: nel deck ci sono frasi di terzi senza consenso (moglie, batterista, capobanda), senza nomi.
3. `/webinar-audit` sul deck (passaggio 7, previsto dalla modalità automatica dopo il 5).
4. Confrontare questo diario con `cliente/NOTE_COLLAUDO_trappole.md`.
