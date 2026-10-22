---
name: webinar-intake
description: Gestisce il materiale del cliente per un webinar Scalers (passaggi 0 e 2): prepara e manda l'intake, chiede le prove dal primo giorno, controlla le risposte, scrive i messaggi al cliente (tipo A-E) e tiene aggiornate le domande aperte. Usala quando il copy dice "mandiamo l'intake a X", "cosa chiediamo al cliente", "il cliente ha risposto", "controlla le risposte del cliente", "scrivi al cliente che la storia non va", "chiedi le prove", "mancano le testimonianze", "prepara il pre-volo".
---

# Webinar Scalers · intake e materiale del cliente

Il webinar è forte quanto il materiale vero che hai. Questa skill lo chiede, lo controlla e lo porta nella scheda. Non scrive mai la risposta al posto del cliente (M4, M5).

`R/` = radice del plugin. Fonte unica: `R/templates/INTAKE_WEBINAR_CLIENTE.md` (Parte 1 da mandare, Parte 2 per noi con i controlli e i messaggi tipo A-E). **Non ricopiarlo né riscriverlo**: si usa così com'è, compilando solo i campi tra parentesi quadre. Regole: aree **A, E, F, L, M** di `R/references/REGOLE_WEBINAR.md`.

## Passaggio 0 · la richiesta delle prove parte subito

Appena la scheda è aperta:
1. Compila il **messaggio tipo D** (Parte 2) con le tre obiezioni (se non le conosci ancora: "chi dubitava del metodo / chi pensava che su di lui non funzionasse / chi pensava che fuori sarebbe rimasto tutto uguale") e mandalo al copy da inoltrare, con la **sezione 4** della Parte 1.
2. Scrivi in scheda §13: "Prove richieste il <data>" · chi · blocca: passaggio 8.
3. Salva quello che hai chiesto in `INTAKE_<P>_richiesta.md`.

**Se l'intake arriva già compilato al passaggio 0:** salvalo subito, identico, in `INTAKE_<P>_risposte.md`, fai partire lo stesso la richiesta delle prove che mancano, e al passaggio 2 fai solo il controllo qui sotto.

## Passaggio 2 · l'intake completo

1. Se il cliente non conosce il metodo: **messaggio tipo A** (briefing) prima dell'intake.
2. Manda la **Parte 1 completa**. Dì al cliente di partire dalle sezioni 1, 2 e 4.
3. Le risposte arrivano **per iscritto o come trascrizione**. Vocali da trascrivere noi: no (M4). Salvale in `INTAKE_<P>_risposte.md`, con la data.

## Il controllo delle risposte

Usa la tabella "Come si controllano le risposte" della Parte 2, sezione per sezione. In più:

| Sezione | Cosa fai con la risposta | Dove va |
|---|---|---|
| 1 · Storia | passa la palla a `webinar-epiphany-bridge` per il controllo E2 ⛔, E4, E5, E12 e il montaggio dei beat | scheda §5 |
| 2.1 · Obiezioni | le elenchi con le parole esatte, le raggruppi nelle tre credenze (veicolo, interna, esterna), scegli la più grande per categoria (F3) | scheda §6 |
| 2.2 · Storie clienti | controlli le 4 condizioni (F4) e se toccano il mondo dell'avatar (F7). Liberatoria sì/no | scheda §6 e §7 |
| 3 · Prodotto | scaletta reale salvata: servirà a verificare ogni esempio (D5) | scheda §1 (percorso del file) |
| 4 · Prove | ogni prova con tipo, dove andrà e **stato della liberatoria** (L2 ⛔) | scheda §7 |
| 5 · Credenziali | ogni credenziale con la sua prova visiva; terzi con consenso e audio riascoltato (I6, L4 ⛔, L5, L6) | scheda §4 e §8 |
| 6 · Foto | elenco, passato e presente | cartella del cliente |
| 7 · Numeri | prezzo, alternative, garanzia, limiti reali. Conflitti con la scheda §2: segnalali al senior (A9) | scheda §2 (solo dopo decisione) |
| 8 · Pubblico e parole | parole vietate e usate, cose da non dire per il settore | scheda §9 (L8, L9) |
| 9 · Asset e meccanica | design system, chi presenta, cosa succede dopo | scheda §1 e §0 |

Ogni dato che manca o che non torna diventa una riga in `DOMANDE_CLIENTE_<P>.md`:
`- [ ] <domanda precisa> · serve in: <blocco> · aperta il <data>`

## I messaggi al cliente

Brevi e concreti: **cosa non va, perché, cosa deve fare la versione giusta**, con un **esempio inventato di un altro settore** che mostri la forma e mai la risposta già scritta (M5). Usa i modelli della Parte 2:
- **A** briefing iniziale (domino, meccanismo, storia, credenze) · **B** la storia non funziona · **C** i pezzi mancanti dell'Epiphany Bridge · **D** le prove · **E** il pre-volo prima di registrare.

Scrivi il messaggio pronto da incollare, poi una riga su cosa aspettarsi. Il plugin non manda niente al cliente da solo: lo manda il copy.

## 🧑 Prove mancanti

Alla fine del passaggio 2, per ogni credenza senza una prova vera prepara per il senior tre opzioni:
(a) andare avanti con `[PROOF: …]` e chiuderle prima dell'onda (L1);
(b) un **caso logico** (una storia pubblica attribuita, raccontata per intero: F9, F10) o un **kinda-like bridge**, con una proposta concreta;
(c) aspettare il cliente, con cosa blocca.
Mai una storia inventata (A3 ⛔). La scelta va nel registro §12.

**Storia vera senza liberatoria** (es. il cliente ha solo un "sì a voce"): non è una prova mancante. Si usa **anonima** (senza nome, volto, dettagli che identificano) e si chiede la liberatoria scritta; se arriva, si aggiunge nome e volto (L2 ⛔). In §7: liberatoria ❌, nota "usata anonima".

## Uscita

La checklist del passaggio 2 in `R/references/CANCELLI.md` (insieme a `webinar-epiphany-bridge`).

## Da non fare

- Trascrivere noi vocali del cliente.
- Scrivere nel messaggio la risposta che vorremmo ("scrivici che…").
- Usare nome e volto di un cliente senza liberatoria.
- Mettere in scheda un dato del cliente in conflitto con un altro senza la scelta del senior.
