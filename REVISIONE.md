# REVISIONE · cosa controllare prima della v1.0 definitiva

> **Per chi:** chi rivede il plugin (Matteo Arnaboldi) e chi decide (Matteo).
> **Regola seguita nella costruzione:** le fonti (`references/` e `templates/`) sono **copiate identiche**, senza nessuna correzione. Dove si contraddicono, il plugin applica la gerarchia **REGOLE > MANUALE > skill > BLUEPRINT > caso studio** e lo dice. Tutto quello che va deciso è qui, numerato, con la proposta. Niente è stato risolto in silenzio.
> **Come si usa:** per ogni punto scrivi a fianco ✅ (ok la proposta), ✏️ (cambia così: …) o ❌ (lascia com'è). Poi le modifiche si fanno **nella fonte** (una volta sola) e il plugin le eredita.

---

## A · Contraddizioni tra le fonti

| # | Dove | Il conflitto | Cosa fa il plugin oggi | Proposta |
|---|---|---|---|---|
| A1 | `MANUALE` §11 vs `REGOLE` | Il manuale elenca "le sette che non si toccano mai": ci sono G1, G2, G18 (che nelle REGOLE **non** sono ⛔) e mancano B10, E2, F12, H3, L2, L4, M2 (che **sono** ⛔) | Valgono le 12 ⛔ delle REGOLE: A1 A2 A3 B4 B10 E2 F12 H3 L2 L4 M2 N5 | Riscrivere il §11 del manuale con le 12 ⛔, oppure marcare ⛔ anche G1, G2, G18 nelle REGOLE |
| A2 | `BLUEPRINT` §0 e §6 (e il brief del plugin) vs `REGOLE` B10, B11 | "Intro 1-11 e stack 70-114 da copiare identici", ma S72 ("ultima volta", "ultimi 50 posti"), S101/S103/S114 ("-90%", "solo 50 posti") violano B10 ⛔, e la "ciliegina" bonus prima del prezzo (S92-94) va contro B11 | Fedeltà totale su struttura, layout e densità; quelle slide non si copiano | Nel blueprint, cambiare "fedeltà totale" in "fedeltà di struttura" e marcare S72, S92-94, S101, S103, S114 come "da non copiare" (oggi è solo nel §5 e nel punto 12 della checklist) |
| A3 | `BLUEPRINT` S1-S11 vs `REGOLE` G3-G11 (e skill originale `webinar-scalers`) | Due intro "canoniche": l'ordine di Alex e l'ordine del rework di Matteo su Mind Reset (promessa → nemici → te lo prometto → domino con grafica → sogno → foglio → chi sono) | Intro canonica = G3-G11 (ordine Mind Reset). Il blueprint resta riferimento per densità e layout | Aggiornare il blueprint §0 e §4 blocco 1 con l'ordine G3-G11 |
| A4 | `BLUEPRINT` S102 vs `REGOLE` G18 | Le alternative di mercato: dopo il prezzo in Alex, prima del prezzo in G18 | Segue G18 | Allineare il blueprint |
| A5 | `GUIDA_STACK` Parte 1 e Parte 3 vs `REGOLE` | La checklist prescrive: urgenza "ultima volta / offerta scandalosa" (B10 ⛔), "% di sconto esplicita", valori "costruiti che sommano pulito" e "stiamo bassissimi" (A1 ⛔, B4 ⛔, B5), rapporto ≥ 10:1 (B5 dice 5-10), bonus a sorpresa prima del prezzo (B11). L'avvertenza in testa copre solo scarsità e sconto | Da GUIDA_STACK si prende la teoria; dove diverge vincono le REGOLE (scritto nella skill `webinar-stack`) | Riscrivere la Parte 3 (checklist, formule, schema-tipo, errori) con le regole Scalers. È la fonte più debole del sistema |
| A6 | `GUIDA_STACK` vs `BLUEPRINT` | Ripetizioni della stack slide di Alex: 6 (GUIDA, che però elenca 7 numeri di slide) contro 8 (BLUEPRINT) | Nessun impatto: il plugin chiede "dopo ogni macroarea" (G17) | Allineare il numero |
| A7 | Quattro strutture dell'Epiphany Bridge | Intake: 4 pezzi · E3: 8 beat · manuale §6.2: 10 tappe dell'eroe · scheda §5: 10 righe | Canonici i beat di E3 / scheda §5; i 4 pezzi dell'intake = formato di raccolta; il §6.2 = teoria | Scriverlo esplicitamente in E3 e nel manuale §6 |
| A8 | `MANUALE` §3.5 vs `REGOLE` F2 | Due architetture delle credenze: (A) una credenza per fase, (B) LKBD in ogni step + muro finale. In (B) la credenza esterna non ha posto | Decisione 🧑 al passaggio 3; in entrambe la credenza esterna va coperta | Aggiungere al §3.5 dove va la credenza esterna nella variante B |
| A9 | Scheda Mind Reset §0 / audit, domanda 1 | "Scheda > deck > script" e insieme "dove script e deck divergono, vale il deck": sulle frasi congelate non si sa chi vince | Il deck non corregge mai la scheda in silenzio: o la modifica è nel registro §12, o è un errore del deck | Scriverlo in M2 |
| A10 | `MANUALE` §10 vs brief del plugin | Il manuale chiede l'approvazione di Matteo tra ogni passaggio; il brief vuole "quasi automatico" con stop solo su domino, prezzo/stack, prove mancanti | Due modalità: guidata (approvazione a ogni cancello) e automatica (`/webinar-avanti auto`, criteri verificati di `CANCELLI.md`, stop solo sulle decisioni 🧑). L'approvatore è il **senior**, Matteo è escalation | Confermare. Aggiornare il §10 del manuale (chi approva: il senior) |
| A11 | Pipeline: passaggio 1 prima del 2 | Il caso studio dice che il domino "in astratto" va fuori strada senza il materiale del frontman, ed E2 si verifica solo con la storia in mano | Ordine del manuale invariato; la skill `webinar-big-domino` chiede il briefing (messaggio A) e le sezioni 1, 2, 4 dell'intake prima delle opzioni se il materiale manca | Valutare di anticipare nel manuale la richiesta delle sezioni 1-2 dell'intake al passaggio 0 |
| A12 | `REGOLE` A1 ⛔ vs override sul 95/5 | A1 non si deroga, ma la scheda Mind Reset registra un override sul 95/5 ("dato non dimostrato" nelle note del deck); `CANCELLI.md` al passaggio 1 ammette "override registrato" per un dato discutibile nel domino | Il plugin segnala il dato discutibile come `[IPOTESI]` (A5) e chiede la decisione | Decidere: un dato non dimostrato in un domino è ammesso con override (allora A1 va precisata) o no |
| A13 | `REGOLE` A3 vs plugin | A3 ammette `[INVENTATO]` in bozza; il brief del plugin vuole "niente invenzioni a livello di sistema" | Il plugin non usa mai `[INVENTATO]`: usa `[DA CLIENTE: …]`, `[PROOF: …]`, `[IPOTESI: …]`. Il lint segnala `[INVENTATO]` come ⛔ | Confermare e allineare A3 |
| A14 | `MANUALE` §4.1-4.2 vs scheda Mind Reset §3 | Il manuale riporta un domino breve e lungo di Gianluca diversi da quelli congelati (es. "…della mente conscia di qualcosa, mentre il 95% — la tua mente inconscia —"; "sicuro o insicuro" vs "confident") | Le frasi congelate si prendono solo dalla scheda | Allineare il manuale alla versione congelata, o dichiarare che nel manuale c'è una versione di lavoro |
| A15 | `MANUALE` §7 (4.4) | Esempio di price drop "€2.500 + IVA", mentre il prezzo congelato è 2.450 + IVA proprio per B6 | — | Allineare l'esempio |
| A16 | `REGOLE` N4 vs H1/H2 | "Molte slide quasi vuote" contro "slide dense che contengono lo script" (nel deck v6, 49 slide su 127 sono sotto le 40 parole) | Segue H1/H2 per la densità, con ~un quarto di slide leggere | Precisare N4 (vale per il ritmo del live, non per il deck registrato?) |
| A17 | Audit v6, domanda 7 vs scheda Mind Reset §3 | L'audit dice che la scheda vuole il palazzo in tutte e tre le fasi; la scheda attuale e il manuale §9.1 dicono camera oscura per la fase 3 | — | La scheda è stata aggiornata dopo l'audit: nessuna azione, ma la domanda 7 è superata |
| A18 | Skill originale `webinar-audit` vs audit v6 | La skill fissa "massimo 8 domande"; l'audit v6 ne ha 9 | L'agente `auditor` tiene il massimo di 8 | Nessuna, o alzare a 10 |
| A19 | `REGOLE` D5 vs caso studio | Lo stesso esempio tolto per D5 ha due nomi: "lettera al padre" (REGOLE) e "la stanza del rapporto con tuo padre" (caso studio) | — | Un nome solo |
| A20 | `REGOLE` G17 vs skill `webinar-stack` | G17: "la macroarea più forte per ultima"; nel caso Mind Reset lo stack segue l'ordine del percorso (nota della slide s129: "ed è giusto così") | Ammesso l'ordine del percorso se si dice | Precisare G17 |
| A21 | Numeri minori | Parole del deck v6: ~7.400 (scheda §0) contro ~7.860 (audit); il conteggio dello script `deckfmt` dà 7.430 · La testata dell'audit dice "⛔ 3" ma la riga 19 cita L2 ⛔ con gravità "alta" · Il blocco 5 del deck si chiama ancora "Per chi è…" dopo che il "per chi è" è stato tolto · La nota di s147 conserva la FLAG "non te lo vendiamo va allineato" dopo la correzione | — | Pulizia quando arriva il deck definitivo |

### Emersi dal collaudo end-to-end (`tests/caso-finto/DIARIO_COLLAUDO.md`)

| # | Dove | Il problema | Proposta |
|---|---|---|---|
| A22 | `TEMPLATE_SCHEDA_WEBINAR.md` riga 4 | Percorsi `01_SCALERS/CLIENTI/…` e `06_OPERATIONS/WEBINAR/…` che nel plugin non esistono | "`<cartella cliente>/WEBINAR/SCHEDA_WEBINAR_<P>.md` · modello in `templates/`" |
| A23 | `TEMPLATE_SCHEDA_WEBINAR.md` §2 | Una sola riga "Bonus" e due ancore: con più alternative o un bonus con condizioni si comprime tutto in una cella. Manca anche una riga per il senior e per i cancelli | Righe "Ancora 3", "Condizioni del bonus", "Senior del webinar" |
| A24 | `INTAKE_WEBINAR_CLIENTE.md` messaggio D | Chiede sempre "Due decisioni tue: [regalo] · [bonus]", anche quando sono già nell'intake | "(solo se non sono già nell'intake)" |
| A25 | `REGOLE` L4 | Non dice se familiari e persone private citate nella storia del frontman (moglie, amico, capobanda) sono "terzi" che richiedono consenso | Precisare: citati senza nome e senza foto non serve consenso; con nome o foto sì |
| A26 | `REGOLE` B10, A6 | In un webinar **registrato** una scarsità datata ("parte il 12 gennaio") diventa falsa dopo la data | In B10: "nei webinar registrati la slide della scarsità si aggiorna a ogni edizione, o dice 'prossima partenza' e rimanda al calendario" |
| A27 | `REGOLE` G11 vs L4 | G11 vuole credenziali con nomi propri; se il nome richiede un consenso che non c'è, non è detto cosa prevale | In G11: "un nome proprio che richiede consenso entra solo con il consenso (L4 prevale)" |

## B · Scelte di progettazione del plugin (non sono nelle fonti: da approvare)

| # | Scelta | Perché |
|---|---|---|
| B1 | **`references/CANCELLI.md`**: un file nuovo con, per ogni passaggio, input, output, uscita verificabile, ⛔ che bloccano, decisione umana. Cita i codici delle regole, non le riscrive | Tre passaggi del manuale (1, 3, 5) uscivano solo con "Matteo approva", il 6 con "controllo a schermo": servivano criteri verificabili per la modalità automatica e per il tutor |
| B2 | **Chi decide**: il **senior** del webinar (oggi Rocco) chiude i cancelli e firma la certificazione; Matteo è escalation | Indicazione di Matteo ("in teoria deve fare tutto il senior se riesce") |
| B3 | **Stato = registro**: ogni cancello chiuso è una riga "Cancello N chiuso" nel registro §12 della scheda; `stato_scheda.py` la legge | Il template della scheda non ha un campo per i cancelli e non va modificato; il registro esiste già |
| B4 | **Deck = artifact Slides**, con il deck in formato testo (`references/FORMATO_DECK.md`, lo stesso dell'export v6) come fonte. `build_deck.py` genera le slide con **un solo `<h2>` e un solo `<p>`** (H3 ⛔ garantita per costruzione); `export_deck.py` riporta l'artifact in testo e verifica H3 sull'HTML | Indicazione di Matteo (Slides); H3 non si può verificare sul testo. Collaudato: andata e ritorno su 127 slide senza perdite |
| B5 | **Auditor indipendente** riceve export del deck + **scheda** + REGOLE + regole di parola del cliente. Il brief diceva "solo deck e REGOLE" | Senza la scheda metà dei controlli (nomi, numeri, frasi congelate, promesse piantate) non si possono fare. La scheda è una specifica, non produzione: l'indipendenza resta |
| B6 | **Lint meccanico** (`lint_deck.py`) prima dell'auditor | Ripetibile e gratuito; lascia all'auditor solo il giudizio |
| B7 | **`DOMANDE_CLIENTE_<P>.md`**: ogni `[DA CLIENTE]` diventa una riga di checklist con il blocco in cui serve | "Niente invenzioni a livello di sistema": la lista domande è il posto dove vanno i buchi |
| B8 | **`templates/CONSEGNA_WEBINAR.md`**: la formula del manuale §2.1 per i venditori, con la checklist N5 ⛔ | Il passaggio 8 non aveva uno strumento |
| B9 | **Nomi dei file** nella cartella `WEBINAR/` del cliente (tabella in `CANCELLI.md`) | Servono per lo stato automatico e per l'auditor |
| B10 | **Academy**: soglie proposte da noi. Esercizio palestra: 70/100 e nessuna ⛔. L3: 15 correzioni su 26 (il deck in `examples/` ha già 4 delle 30 correzioni applicate), tutte e 3 le ⛔, massimo 5 falsi positivi. Certificazione: zero ⛔ dall'auditor, rubrica ≥ 80/100, nessun blocco sotto il 60%, difesa del domino superata, firma del senior | Da confermare o cambiare |
| B11 | **Certificazione**: oltre all'auditor, il tutor confronta la scheda del copy con il brief (un dato inventato scritto in scheda come fatto l'auditor non lo vede) | Chiusura di un buco dell'indipendenza |
| B12 | **Onboarding**: le durate di moduli ed esercizi portano a ~24 ore; il tracciato di 10 giorni sta a ~2-2h30 al giorno. Alternativa: tre settimane sotto le 2 ore | Il brief chiedeva 1-2 ore al giorno |
| B13 | **Passaggio a L3**: nicchia 1 completa + nicchia 2 almeno E1-E3; la nicchia 3 è di rinforzo su indicazione del senior | Allineato tra `onboarding-2-settimane.md` e `L2-palestra/README.md` |
| B14 | Gli esercizi della palestra si chiamano E1-E5, come i codici delle regole E1-E5 | Da rinominare (es. "Es.1") se crea confusione |

## C · Buchi e limiti noti

- **Nessuna trascrizione di un webinar reale** per il confronto G23: il plugin usa il blueprint Grassi e il deck Mind Reset. Se esiste la trascrizione di Alex, va in `references/`.
- **Il webinar Mind Reset non è definitivo.** `examples/mind-reset/` è la versione del 30/9. Quando arriva il deck finale: sostituire l'export, rilanciare l'audit, rigenerare `academy/L3-caso-reale/chiave-tutor.md` e il test di regressione (`tests/regressione-mind-reset/`).
- **La scheda Mind Reset in `examples/` rivela l'audit** (§13 riga 11, §14 riga "Audit deck v6", §6 frase su Selye): per L3 il tutor deve preparare una copia senza quei pezzi (scritto nella chiave). Il manuale e le regole, che il copy ha già letto, contengono comunque domino e stack di Mind Reset: il compito 1 di L3 giudica il ragionamento, non l'originalità.
- **Skill già installate sull'account** con nomi e trigger simili (`webinar-scalers`, `webinar-slide`, `webinar-audit`, W1, la vecchia `webinar-script` in `RISORSE_CORSO`): non sono state toccate. Con il plugin installato si attivano sulle stesse frasi. Decidere se disattivarle.
- **Le tre copie delle fonti** (Drive, KB di progetto, cartella locale) restano tre: se il repo diventa la fonte, le altre vanno trattate come specchi.
- **Il lint è letterale**: parole vietate e glossario generano candidati da confermare ("medico" in "medico ortopedico"). L'auditor li filtra.
- **Il tetto delle rate per chi ha partita IVA** (B6 parla di 3.000 € "finiti"): in palestra è applicato alla lettera; da confermare per i clienti B2B.

## D · Per la v1.1 (proposte)

1. Riscrivere la Parte 3 di `GUIDA_STACK.md` e il §11 del manuale (A1, A5): sono le due correzioni che valgono di più.
2. Un test di regressione automatico: `lint_deck.py` + auditor sul deck Mind Reset definitivo, confrontato con la chiave, a ogni modifica delle regole.
3. Un secondo caso reale in `examples/` (il prossimo webinar cliente), anonimizzato solo se serve.
4. Integrazione Canva per il giro grafico, se il design system del cliente vive lì.
5. `webinar-vsl` e `webinar-ad`: il framework si comprime (manuale §9.2), la scheda è già pronta a farlo.
