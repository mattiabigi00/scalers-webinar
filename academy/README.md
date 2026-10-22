# Webinar Academy · Scalers

> **Cos'è:** la scuola interna che porta un copywriter a costruire da solo il webinar di vendita di un cliente con il metodo Scalers. Qui trovi il principio, i livelli, come si usa e l'indice di tutti i file.
> **Durata:** due settimane di formazione (10 giorni lavorativi, circa 2 ore al giorno), poi la certificazione (5 giorni lavorativi).
> **Prerequisiti:** nessuno. Si comincia da questo file, poi si segue `onboarding-2-settimane.md` giorno per giorno.

---

## Il principio: una fonte sola

L'Academy insegna **quello che il plugin esegue, dalla stessa fonte**. Le regole vivono in `references/REGOLE_WEBINAR.md`, il metodo in `references/MANUALE_WEBINAR_SCALERS.md`, la pipeline come la esegue il plugin in `references/CANCELLI.md`. I moduli non le riscrivono: citano il codice (es. `E2 ⛔`) e il punto del manuale (es. "manuale §6.4"), spiegano in due righe e ti rimandano al testo. Se una regola cambia, cambia là e l'Academy la segue.

**Il tutor è il plugin in modalità formazione** (skill `webinar-tutor`). Stesse regole, stessi file, stessi esempi. La differenza è una sola: quando lavora un webinar cliente il plugin scrive; quando ti allena, **non scrive al posto tuo**. Ti fa domande, ti indica la regola, ti fa trovare l'errore da solo.

In caso di conflitto tra le fonti vale la gerarchia di `CANCELLI.md`: **REGOLE > MANUALE > skill > BLUEPRINT > caso studio**. Le contraddizioni note sono in `REVISIONE.md` alla radice del repo: il tutor te le segnala, non le nasconde.

## Per chi è

Per i copywriter junior e mid appena entrati in Scalers: lavorano da remoto, scrivono bene, **non conoscono ancora il metodo webinar**. Non serve aver mai fatto un webinar. Serve:
- circa due ore al giorno, tutti i giorni, per due settimane;
- lavorare per iscritto: ogni consegna è un file in `ACADEMY_<nome>/`;
- accettare le domande al posto delle risposte. È il modo più lento di farti vedere un errore, e l'unico che funziona.

## I livelli

| Livello | Obiettivo | Durata | File | Si passa quando… |
|---|---|---|---|---|
| **L0 · Fondamenta** | Capire perché esiste il webinar (revenue per venditore/ora), dove sta nel funnel, come si consegna, perché one-to-many cambia tutto | ~1h30 · giorno 1 | `L0-fondamenta/` (3 moduli) | domande di verifica ed esercizi flash dei 3 moduli fatti, senza arrivare all'aiuto 3 del tutor |
| **L1 · Anatomia** | Conoscere ogni pezzo del webinar con le sue regole: quattro blocchi, Big Domino, meccanismo, Epiphany Bridge, credenze, intro, stack, slide, verità, scheda | ~9 ore · giorni 2-5 | `L1-anatomia/` (10 moduli) + Expert Secrets | domande di verifica ed esercizi flash dei 10 moduli fatti; al massimo 2 moduli da rileggere |
| **L2 · Palestra** | Fare, su clienti inventati: domino, storia, credenze, stack, prime slide. Il tutor corregge con domande e rubriche | ~10 ore · giorni 5-9 | `L2-palestra/` (3 nicchie, 5 esercizi ciascuna) | ogni esercizio a 70/100 e nessuna ⛔ aperta (`L2-palestra/README.md`); nel tracciato: nicchia 1 completa e nicchia 2 E1-E3 |
| **L3 · Caso reale** | Lavorare sul webinar vero Mind Reset: il tuo domino e il tuo stack sul materiale del cliente, poi la caccia agli errori sul deck v6 | ~4 ore · giorni 9-10 | `L3-caso-reale/` | compito 1 consegnato e confrontato; compito 2 con almeno 15 correzioni su 26, tutte le ⛔, al massimo 5 falsi positivi |
| **Certificazione** | Un webinar completo, da solo, su un cliente inventato nuovo: dalla scheda al deck testo | 5 giorni lavorativi, 10-12 ore · giorni 11-15, poi valutazione | `certificazione/` | zero ⛔ nell'audit indipendente, rubrica ≥ 80/100, nessun blocco sotto il 60% dei suoi punti, difesa del domino superata, firma del senior |

**Attenzione:** `L2-palestra/README.md` chiede per L3 la nicchia 1 più una seconda nicchia completa, e la terza prima della certificazione; il tracciato di due settimane porta a L3 con nicchia 1 e nicchia 2 E1-E3. Vale la riga del senior nel registro (conflitto registrato in REVISIONE.md alla radice del repo).

**Dopo la certificazione sei autonomo sui webinar dei clienti.** Apri tu il webinar (`/webinar-nuovo`), lo porti avanti (`/webinar-avanti`), controlli lo stato (`/webinar-stato`), lanci l'audit (`/webinar-audit`). Le decisioni umane dei cancelli (offerta, scelta del domino, prove mancanti, architettura, approvazioni) **le chiude il senior** del webinar (oggi Rocco: `CANCELLI.md`, "Ruoli"); Matteo è l'escalation. Autonomo vuol dire che il lavoro lo porti tu, non che decidi da solo.

## Come si usa

**Con il tutor, ogni giorno.** Lancia `/webinar-palestra <nome>` (facoltativo: il punto, es. `L2 nicchia-1 es-3`). Il tutor:
1. cerca o crea il tuo registro `ACADEMY_<nome>/registro.md` (livello, moduli fatti, esercizi con punteggio, dove ti sei bloccato, prossimo passo);
2. ti dice in una riga dove sei e cosa fai adesso;
3. lavora **una cosa per volta**, in quattro modalità: spiega (L0-L1), allena (L2), guida il caso reale (L3), conduce la certificazione.

**Come ti corregge in palestra.** Al massimo tre problemi per consegna, il più grave per primo (una ⛔ è sempre la prima). Per ognuno una domanda e il codice della regola. Non riscrive, non ti dà la versione giusta, nemmeno "per esempio". Se chiedi la risposta sale di un livello di aiuto: (1) una domanda più stretta · (2) la regola intera e il paragrafo del manuale · (3) un esempio da un altro caso (Grassi o Mind Reset), mai dalla nicchia dell'esercizio. Il punteggio con la rubrica arriva solo quando dici "consegno" (o dopo tre giri).

**Per la certificazione:** `/webinar-certifica <nome> avvia` (ti consegna brief, regole e tempi) e, alla consegna, `/webinar-certifica <nome> valuta`. Tutto in `certificazione/README.md`.

**Gli strumenti che userai da L3 in poi:** i comandi `/webinar-audit`, `/webinar-nuovo`, `/webinar-avanti`, `/webinar-stato`, `/webinar-decidi`, `/webinar-cliente`; gli agenti `auditor` (il revisore indipendente) e `prospect-scettico` (il pubblico che attacca il tuo domino); le skill di pipeline `webinar-pipeline`, `webinar-intake`, `webinar-big-domino`, `webinar-epiphany-bridge`, `webinar-tre-segreti`, `webinar-stack`, `webinar-script`, `webinar-slide`, `webinar-audit`.

**Le 12 regole che non si derogano** (le ⛔ di `REGOLE_WEBINAR.md`): `A1` `A2` `A3` `B4` `B10` `E2` `F12` `H3` `L2` `L4` `M2` `N5`. Un esercizio con una ⛔ violata non passa, qualunque sia il resto. Il tutor non promuove nessuno con una ⛔ aperta.

## La regola della finzione dichiarata

I casi della palestra e della certificazione sono **inventati**, e ogni file lo dice in testa con questo box:

> **FINZIONE DICHIARATA** · materiale inventato per l'allenamento. Non usare fuori dall'Academy.

- Nomi di persone e di brand inventati, non esistenti e non famosi.
- Mai le nicchie dei clienti reali di Scalers (e-commerce, investimenti, crescita personale e inconscio, formazione immobiliare, auto).
- I dati finti della palestra e della certificazione **non entrano mai** nel webinar di un cliente, neanche come esempio.

**Il caso Mind Reset (L3) invece è vero.** Sono dati di un cliente (Gianluca Liguori): restano dentro Scalers, non si copiano altrove e non si mandano fuori.

## Le chiavi del tutor

I file `chiavi-tutor.md` (palestra) e `chiave-tutor.md` (L3 e certificazione) sono **solo per il tutor e il senior**. Il tutor non li mostra, non li cita e non li parafrasa. Tu non li apri: se lo fai, l'esercizio non vale e va scritto nel registro. Lavori da remoto e nessuno ti controlla la cartella: è una regola sulla fiducia, come quella di non inventare un dato.

## Indice di tutti i file

| File | Livello | Cosa c'è | Chi lo legge |
|---|---|---|---|
| `README.md` | — | questo indice: principio, livelli, uso, finzione | tutti |
| `metodo-su-un-foglio.md` | — | il metodo intero in una pagina, da tenere aperto | tutti |
| `onboarding-2-settimane.md` | — | il tracciato giorno per giorno, output e controlli | copy, tutor, senior |
| `L0-fondamenta/01-perche-il-webinar.md` | L0 | il vincolo economico: il venditore è l'asset più scarso | copy |
| `L0-fondamenta/02-funnel-e-consegna.md` | L0 | dove sta il webinar nel funnel, come si consegna | copy |
| `L0-fondamenta/03-one-to-many-e-letture.md` | L0 | one-to-many contro one-to-one, le letture obbligate | copy |
| `L1-anatomia/01-quattro-blocchi.md` | L1 | intro, Epiphany Bridge + domino, tre segreti, stack | copy |
| `L1-anatomia/02-big-domino.md` | L1 | la tessera più grossa: forma grezza, 5 criteri, test competitor | copy |
| `L1-anatomia/03-meccanismo-e-metafora.md` | L1 | perché funziona, il nome, una metafora sola | copy |
| `L1-anatomia/04-epiphany-bridge.md` | L1 | la storia che finisce nel domino | copy |
| `L1-anatomia/05-credenze-e-storie.md` | L1 | veicolo, interna, esterna: una credenza, una storia | copy |
| `L1-anatomia/06-intro-e-rapport.md` | L1 | promessa, One Sentence Persuasion, impegno attivo, chi sono | copy |
| `L1-anatomia/07-stack-prezzo-close.md` | L1 | stack a strati, sequenza del prezzo, garanzia, close | copy |
| `L1-anatomia/08-slide-copy.md` | L1 | le slide sono lo script: densità, blocchi di testo, ganci | copy |
| `L1-anatomia/09-verita-prove-consensi.md` | L1 | niente invenzioni, liberatorie, consensi, parole vietate | copy |
| `L1-anatomia/10-scheda-e-processo.md` | L1 | la scheda di progetto, i cancelli, chi decide | copy |
| `L2-palestra/README.md` | L2 | come funziona la palestra, soglie, ordine delle nicchie | copy, tutor |
| `L2-palestra/nicchia-1-public-speaking/brief.md` | L2 | cliente inventato: materiale grezzo | copy |
| `L2-palestra/nicchia-1-public-speaking/esercizi.md` | L2 | consegne e rubriche | copy |
| `L2-palestra/nicchia-1-public-speaking/chiavi-tutor.md` | L2 | trappole e criteri di correzione | **solo tutor e senior** |
| `L2-palestra/nicchia-2-fotografia/brief.md` | L2 | cliente inventato: materiale grezzo | copy |
| `L2-palestra/nicchia-2-fotografia/esercizi.md` | L2 | consegne e rubriche | copy |
| `L2-palestra/nicchia-2-fotografia/chiavi-tutor.md` | L2 | trappole e criteri di correzione | **solo tutor e senior** |
| `L2-palestra/nicchia-3-artigiani-b2b/brief.md` | L2 | cliente inventato: materiale grezzo | copy |
| `L2-palestra/nicchia-3-artigiani-b2b/esercizi.md` | L2 | consegne e rubriche | copy |
| `L2-palestra/nicchia-3-artigiani-b2b/chiavi-tutor.md` | L2 | trappole e criteri di correzione | **solo tutor e senior** |
| `L3-caso-reale/README.md` | L3 | obiettivi, i tre compiti, soglia | copy, tutor |
| `L3-caso-reale/materiale-copy.md` | L3 | il materiale vero di Mind Reset per il compito 1, senza spoiler | copy |
| `L3-caso-reale/chiave-tutor.md` | L3 | le 30 righe dell'audit reale, criteri di conteggio, punti di confronto | **solo tutor e senior** |
| `certificazione/README.md` | Cert. | cosa si consegna, regole della prova, valutazione, verbale | copy, tutor, senior |
| `certificazione/brief-certificazione.md` | Cert. | il cliente inventato della prova: intake completo e offerta grezza | copy |
| `certificazione/rubrica.md` | Cert. | la rubrica su 100 punti, blocco per blocco | copy, tutor, senior |
| `certificazione/chiave-tutor.md` | Cert. | le trappole del brief, i domini accettabili, gli errori che fanno fallire | **solo tutor e senior** |

**Fuori dall'Academy, le fonti che l'Academy cita:** `references/` (manuale, regole, cancelli, formato del deck, blueprint Grassi, guida allo stack), `examples/mind-reset/` (scheda, caso studio, deck v6, audit), `templates/` (scheda e intake), `agents/` e `skills/`.
