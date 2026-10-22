# Certificazione · Webinar Academy

> **Cos'è:** la prova finale dell'Academy. Costruisci da solo un webinar completo su un cliente inventato, dalla scheda al deck testo; poi un audit indipendente, la rubrica, la difesa del domino e la firma del senior.
> **Durata:** 5 giorni lavorativi, circa 10-12 ore (giorni 11-15 del tracciato), più la valutazione entro 2 giorni lavorativi dalla consegna.
> **Prerequisiti:** L3 chiuso e la riga di ok del senior nel registro `ACADEMY_<nome>/registro.md`.

---

> **FINZIONE DICHIARATA** · materiale inventato per l'allenamento. Non usare fuori dall'Academy.
> Il cliente della prova (`brief-certificazione.md`) è inventato. Il webinar che produci non va a nessun cliente.

## Cos'è e cosa dimostra

Dimostri di saper portare un webinar dal materiale grezzo del cliente al deck testo **rispettando le regole senza nessuno che te le ricordi**. È la stessa pipeline che fai con i clienti veri (`references/CANCELLI.md`, passaggi 0-5), con una differenza: le decisioni umane che di solito prende il senior, qui le prendi tu, e le motivi per iscritto.

Dopo la certificazione lavori i webinar dei clienti in autonomia; le decisioni umane dei cancelli tornano al senior.

## Quando

Dopo L3, con l'ok del senior scritto nel registro. Si avvia con:

`/webinar-certifica <nome> avvia`

Il tutor ti consegna `brief-certificazione.md`, queste regole e la data di consegna (fine del quinto giorno lavorativo). Da quel momento il tutor non aiuta.

## Cosa consegni

Tutto in `ACADEMY_<nome>/CERTIFICAZIONE/WEBINAR/`, con i nomi di `CANCELLI.md` ("Convenzioni dei file"). `<P>` è il nome del prodotto che scegli, maiuscolo e senza spazi.

| File | Cosa contiene | Passaggio |
|---|---|---|
| `SCHEDA_WEBINAR_<P>.md` | la scheda compilata dal modello `templates/TEMPLATE_SCHEDA_WEBINAR.md`, con il registro §12 completo: ogni cancello chiuso, ogni decisione umana con il suo perché | 0-5 |
| `DOMINO_<P>_opzioni.md` | 90% del mercato, forma grezza, opzioni con i 5 criteri, test competitor, mucca viola, stress test, raccomandazione | 1 |
| `ARCHITETTURA_<P>.md` | la tabella dei blocchi con i minuti, più tesi, impegno attivo, promesse, solo-stack, obiezioni vinte | 3 |
| `SCRIPT_<P>_v2.md` | lo script finale (tieni in cartella anche `SCRIPT_<P>_v1.md` e `CONFRONTO_<P>.md`: la rubrica li guarda) | 4 |
| `DECK_<P>_testo.md` | il deck nel formato di `references/FORMATO_DECK.md` | 5 |
| `DOMANDE_CLIENTE_<P>.md` | ogni `[DA CLIENTE]` e ogni verifica aperta, con il blocco o la slide in cui serve | sempre |

Non serve pubblicare l'artifact Slides né fare la grafica: la prova finisce al deck testo (passaggio 5, giro 1).

**La scheda deve seguire il modello.** `lint_deck.py` e `stato_scheda.py` la leggono per sezioni: se la struttura cambia, il controllo meccanico non funziona e la voce 6.2 della rubrica non si può verificare.

## Le regole della prova

1. **Il tutor non aiuta.** Niente domande socratiche, niente correzioni, niente "sei sulla strada giusta". Può solo chiarire cosa dice una regola della prova (questa sezione), non cosa fare.
2. **Puoi usare i comandi di pipeline del plugin:** `/webinar-nuovo`, `/webinar-avanti` (anche `auto`), `/webinar-stato`, `/webinar-decidi`, `/webinar-cliente`, `/webinar-audit`, e le skill che richiamano. Il plugin può scrivere bozze. **Ma ogni decisione umana la prendi tu** (le fermate 🧑 di `CANCELLI.md`: offerta, scelta del domino, prove mancanti, architettura A o B, approvazioni) e la **motivi per iscritto** nel registro della scheda: `| data | decisione | <nome> | dove | ` con il perché nella colonna della decisione. Una decisione senza motivo vale 0 nella sua voce della rubrica.
3. **Tu sei responsabile di tutto quello che consegni**, anche di quello che ha scritto il plugin. "L'ha scritto la skill" non è un motivo.
4. **Niente invenzioni.** Il cliente non risponde durante la prova. Ogni dato che non è nel brief si scrive `[DA CLIENTE: cosa serve]` e va in `DOMANDE_CLIENTE_<P>.md`; ogni prova attesa `[PROOF: cosa]`; ogni inferenza `[IPOTESI: …]`. Mai `[INVENTATO]`, mai un numero plausibile (A1 ⛔, A2 ⛔, A3 ⛔).
5. **Segnaposto ammessi, violazioni no.** Un deck con dei `[PROOF]` aperti è normale (il cliente non ha ancora mandato tutto). Un volto senza liberatoria o un terzo senza consenso in slide non lo è (L2 ⛔, L4 ⛔).
6. **Tempo:** 5 giorni lavorativi. Se non finisci, consegni quello che hai alla scadenza: la rubrica valuta i file che ci sono. Una proroga la dà solo il senior, per scritto, prima della scadenza.
7. **Da solo.** Niente aiuto da colleghi, niente webinar di clienti veri come fonte di dati. `examples/mind-reset/` e il blueprint li puoi usare come riferimento di struttura (G23), come in un webinar vero.
8. **Le chiavi non si aprono** (`certificazione/chiave-tutor.md`). Se succede, la prova non vale.

## La valutazione

Si avvia con `/webinar-certifica <nome> valuta`. Quattro passi, in quest'ordine.

**1 · Controlli indipendenti** (tutor)
- `python3 scripts/lint_deck.py ACADEMY_<nome>/CERTIFICAZIONE/WEBINAR/DECK_<P>_testo.md --scheda ACADEMY_<nome>/CERTIFICAZIONE/WEBINAR/SCHEDA_WEBINAR_<P>.md --out ACADEMY_<nome>/CERTIFICAZIONE/LINT_<P>.md`
- l'agente **`auditor`**, lanciato **solo** con i percorsi di deck testo, scheda del copy, `references/REGOLE_WEBINAR.md` e radice del plugin, più il file da scrivere `ACADEMY_<nome>/CERTIFICAZIONE/AUDIT_<P>_<data>.md`. Niente brief, niente conversazione, niente altri file: l'auditor giudica il risultato, non il percorso.
- il **confronto scheda ↔ brief**, voce per voce (tutor): l'auditor vede solo la scheda, quindi un dato inventato scritto in scheda come fatto non lo può vedere. Le ⛔ trovate qui valgono come quelle dell'auditor.

**2 · La rubrica** (tutor): `certificazione/rubrica.md`, voce per voce, con una riga di motivo e la regola.

**3 · La difesa del domino** (10 minuti)
- Il tutor lancia l'agente **`prospect-scettico`** con l'avatar e le obiezioni della sezione 2.1 e 8 del brief, e con il **tuo** domino breve e lungo come sono in scheda §3.
- Tu leggi la sua risposta e hai **10 minuti** per rispondere per iscritto, obiezione per obiezione: dove il webinar la affronta (blocco, slide, prova) e perché regge. Non si riscrive il domino durante la difesa: se cambia il domino, cambia tutto il webinar (C9).
- **Il senior giudica** se il domino regge: **regge** · **regge con riserva** (una debolezza nominata, che il webinar copre) · **non regge** (un attacco lo fa cadere e il webinar non ha risposta). "Non regge" = difesa non superata.

**4 · Verbale e firma** (tutor e senior): il tutor scrive il verbale con l'esito proposto; **l'esito lo decide e lo firma il senior**.

## La soglia

Tutte e quattro, insieme:
1. **zero ⛔** nell'audit indipendente e nel confronto scheda ↔ brief (esclusa "H3 non verificabile dall'export");
2. **rubrica ≥ 80/100**;
3. **nessun blocco della rubrica sotto il 60% dei suoi punti**;
4. **difesa superata** (regge, o regge con riserva).

Se il copy contesta una ⛔ dell'auditor, decide il senior leggendo la regola in `REGOLE_WEBINAR.md`. La soglia non si tratta.

## L'esito

**Certificato.** Il registro dice "certificato il <data>, senior <nome>". Da lì lavori i webinar dei clienti in autonomia, con il senior che chiude i cancelli.

**Da ripetere**, con cosa rifare:

| Cosa non è passato | Cosa rifai | Tempo |
|---|---|---|
| una o più ⛔ | correggi solo le ⛔ sullo stesso brief; si rilancia l'audit sul deck corretto e si rivalutano le voci della rubrica toccate | 2 giorni lavorativi |
| totale sotto 80 o un blocco sotto il 60% | rifai i pezzi dei blocchi sotto soglia sullo stesso brief; si rivalutano quei blocchi, più l'audit se il deck cambia | 3 giorni lavorativi |
| difesa non superata | il domino non regge: si riparte dal passaggio 1 sullo stesso brief (C9), poi di nuovo tutto fino al deck | 5 giorni lavorativi |
| una seconda prova non superata | decide il senior: ripasso mirato (moduli L1 e palestra sulle regole mancate) e una nuova prova più avanti | a giudizio del senior |

## Il verbale

Il tutor lo scrive in `ACADEMY_<nome>/CERTIFICAZIONE_<AAAA-MM-GG>.md` con questo modello.

```markdown
# CERTIFICAZIONE · <nome del copy> · <AAAA-MM-GG>

> Brief: `certificazione/brief-certificazione.md` · consegna del <data> · valutazione del <data>
> Tutor: webinar-tutor · Senior: <nome>

## Esito proposto dal tutor
<certificato | da ripetere>

## 1 · Controlli indipendenti
- Lint: ⛔ <n> · alta <n> · bassa <n> · segnaposto <n> → `CERTIFICAZIONE/LINT_<P>.md`
- Auditor: ⛔ <n> · alta <n> · bassa <n> → `CERTIFICAZIONE/AUDIT_<P>_<data>.md`
- Confronto scheda ↔ brief: ⛔ <n> · note: <…>
- ⛔ trovate (una riga ciascuna, con regola e slide): <…> / nessuna

## 2 · Rubrica
<il foglio del punteggio di `rubrica.md`, con una riga di motivo per voce>
Totale: <n>/100 · blocchi sotto il 60%: <nessuno | quali>

## 3 · Difesa del domino
- Domino breve difeso: «<verbatim dalla scheda §3>»
- Attacchi più forti del prospect-scettico: <2-3 righe>
- Risposte del copy: <sintesi, o il file allegato>
- Giudizio del senior: <regge | regge con riserva: … | non regge: …>

## 4 · Decisione
| Soglia | Esito |
|---|---|
| zero ⛔ | ✅ / ❌ |
| rubrica ≥ 80 | ✅ / ❌ (<n>) |
| nessun blocco sotto il 60% | ✅ / ❌ |
| difesa superata | ✅ / ❌ |

**Esito:** <certificato | da ripetere>
**Se da ripetere, cosa rifare e entro quando:** <…>
**Punti di forza (max 3):** <…>
**Da tenere d'occhio sui primi webinar veri (max 3):** <…>

Firma del senior: <nome> · <data>
```

Dopo la firma, il tutor aggiorna il registro del copy con l'esito e il link al verbale.
