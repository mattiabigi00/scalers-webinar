# L1.1 · I quattro blocchi

> **Cos'è:** la struttura macro di ogni webinar Scalers: quattro blocchi, sempre quelli, qualunque sia la durata. **Durata:** ~45 minuti. **Prerequisiti:** L0.1-L0.3.
> **Regole:** G1, G2, G24 (con G23 e G12 negli esempi) · **Manuale:** §7, §9.1, §10 ("Cosa serve davvero per partire", "Numeri di riferimento")

---

## La regola in breve

Ogni webinar è fatto di **quattro blocchi** (manuale §7):

| # | Blocco | Cosa fa |
|---|---|---|
| 1 | Introduzione | costruisci **rapport** |
| 2 | Epiphany Bridge + Big Domino | installi **la** credenza |
| 3 | Tre segreti (o tre step) | demolisci le **tre obiezioni** |
| 4 | Stack | la vendita vera e propria |

I blocchi 1-3 sono la parte "educativa". Non vuol dire accademica: *"Significa che rompiamo credenze vecchie e ne installiamo di nuove. Lo facciamo con le storie."* Da qui le due regole di base: **G1** il webinar è emotivo, non didattico; **G2** ogni argomento razionale che può diventare una storia deve diventare una storia.

**G24** dice che il framework serve a te, non il contrario: varianti d'ordine ammesse (social proof anticipata, step dentro lo stack, manuale §9.1) **se la logica regge**. I quattro blocchi però ci sono sempre.

**Numeri di riferimento** (manuale §7 e §10): ~120 slide di media · ~10.000 parole di slide ≈ 75 minuti (a circa 140 parole al minuto) · durate testate da 20 minuti a 4 ore, fino a tre serate. *"Ma 120 slide sono sempre e solo quei quattro blocchi."*

E la frase da ricordare quando parti con un cliente nuovo (manuale §10): *"L'intro e lo stack sono sempre uguali come struttura. Le cose da trovare ogni volta sono tre: il Big Domino, le tre credenze limitanti, le storie che le trasmettono. Tutto il resto è ripetibile."*

## Esempio buono

**Il deck di Alex Grassi, blocco per blocco** (`references/BLUEPRINT_SLIDE_WEBINAR.md` §1, mappa macro, citata):

| # | Blocco | Slide | N. | Parole tot. | Media parole/slide |
|---|---|---|---|---|---|
| 1 | Intro / rapport (fino al Chi sono) | 1–11 | 11 | 654 | 59 (mediana 28) |
| 2 | Epiphany Bridge → Big Domino | 12–34 | 23 | 2.167 | 94 (mediana 112) |
| 3 | Tre step | 35–69 | 35 | 3.686 | 105 (mediana 109) |
| 4 | Stack + chiusura | 70–114 | 45 | 3.790 | 84 (mediana 86) |
| | **Totale** | | **114** | **10.297** | **90** |

Guarda le proporzioni: l'intro è corta e leggera; lo stack da solo è quasi il 40% delle slide. Il blueprint: *"~10.300 parole a ~140 parole/minuto fanno ~75 minuti, cioè la durata del webinar."*

**Il deck Mind Reset v6, sugli stessi quattro blocchi** (`examples/mind-reset/Webinar_Mind_Reset_Deck_v6_testo.md`, 127 slide; parole di corpo contate sull'export, titoli esclusi):

| Blocco | Slide (posizione) | Da … a … | N. | Parole di corpo |
|---|---|---|---|---|
| 1 · Intro | 1-23 | promessa (s004) → "Ma non è sempre stato così." (s021g) | 23 | ~1.040 |
| 2 · Epiphany Bridge + Big Domino | 24-57 | "A diciassette anni" (s022) → domino (s052-s053) → "Me lo dicono tutti" (s055) | 34 | ~2.310 |
| 3 · Tre fasi (una credenza per fase) | 58-89 | obiezione 1 (r01) → storia dei due fratelli (r22) | 32 | ~1.740 |
| 4 · Vendita | 90-127 | Domandina (s115) → stack → prezzo → garanzia → due strade → FAQ → regalo → CTA (s152) | 38 | ~2.340 |

Le proporzioni sono diverse da Grassi (la storia di Gianluca è più lunga, lo stack più corto), ma i blocchi sono gli stessi quattro. È G24 applicata bene: la struttura non cambia, cambiano le lunghezze.

## Esempio sbagliato e perché

**La v1 dello script di Mind Reset** (`examples/mind-reset/CASO_STUDIO_WEBINAR_MIND_RESET.md`, passaggio 4):

> *"Script v1 da 8.600 parole. Poi il confronto con la trascrizione di un webinar vero di Alex Grassi: 19 buchi. I cinque grossi: mancava il finale, nessun impegno attivo di chi guarda, la tesi detta una volta sola, prove tutte alla fine, niente trial close né FAQ."*

Cosa era successo: i quattro blocchi c'erano "di nome", ma dentro mancavano i pezzi che li fanno funzionare.

| Buco | Blocco | Regola |
|---|---|---|
| mancava il finale | 4 | G18, G21 (sequenza del prezzo, CTA) |
| nessun impegno attivo | 1 (e ritorno nel 4) | G9 |
| tesi detta una volta sola | 2 (e ripresa nel 3-4) | C10 |
| prove tutte alla fine | 3 | G12 |
| niente trial close né FAQ | 4 | G16, G20 |

La lezione è la regola **G23**: lo script v1 si confronta con un webinar reale che converte **prima** di passare alle slide. Nel caso Mind Reset la v3 ha chiuso i buchi: *"chi guarda scrive il suo blocco su un foglio al minuto 7 e lo ritrova nel prezzo, nella garanzia e nella CTA; la tesi torna quattro volte; le prove arrivano dopo ogni fase."*

## Gli errori tipici

- **Riprogettare la struttura a ogni cliente.** Intro e stack sono sempre uguali come struttura (manuale §10): il lavoro vero è domino, credenze, storie.
- **Un blocco 3 "didattico":** spiegare il metodo invece di rompere credenze. Viola G1.
- **Confondere G24 con "posso togliere un blocco".** Le varianti d'ordine sono ammesse; un blocco che manca no.
- **Scrivere tutto e poi contare.** Le proporzioni si decidono nell'architettura (passaggio 3), con i minuti stimati per blocco.
- **Saltare il confronto con un webinar vero** (G23): è lì che escono i buchi di struttura.

## Nel plugin

- **Skill:** `webinar-script` scrive l'architettura (`ARCHITETTURA_<P>.md`: tabella dei blocchi con minuti, a circa 140 parole/minuto) e poi lo script v1 → `CONFRONTO_<P>.md` → v2.
- **Cancelli:** **3 · Architettura** (uscita: "tabella dei blocchi con minuti stimati", "dove torna la tesi", "prove dopo ogni fase", "impegno attivo e dove torna") e **4 · Script** (uscita: "confronto fatto: tabella dei buchi con il blocco in cui ciascuno si chiude").
- **Controlli automatici:** nessuno script conta i blocchi. `scripts/lint_deck.py` segnala le slide oltre ~220 parole (H2); `scripts/stato_scheda.py` ti dice a che passaggio sei leggendo il registro della scheda.
- **Tutor:** `/webinar-palestra` per gli esercizi; il tutor ti fa domande, non ti dà la struttura.

---

## Domande di verifica

**1. Un cliente ha un prodotto semplice e vuole un webinar di 25 minuti. Quanti blocchi ha?**

<details><summary>Risposta attesa</summary>

Quattro. Il framework si comprime (manuale §9.2) e la durata cambia la lunghezza dei blocchi, non il loro numero: *"120 slide sono sempre e solo quei quattro blocchi"* (manuale §7).
</details>

**2. Nel deck di Grassi lo stack occupa 45 slide su 114. Nel tuo primo deck lo stack ne ha 8. È per forza un problema?**

<details><summary>Risposta attesa</summary>

Non per forza: G24 ammette lunghezze e ordini diversi se la logica regge (Mind Reset ha 38 slide di vendita). Ma va controllato che dentro ci sia tutta la sequenza del prezzo (G18: totale, "naturalmente no", quanto vale per te, alternative, giustificazione, prezzo, garanzia, due strade, FAQ, regalo, CTA). Con 8 slide è probabile che manchino pezzi, come nella v1 di Mind Reset.
</details>

**3. Quali sono le tre cose da trovare ogni volta, e perché solo tre?**

<details><summary>Risposta attesa</summary>

Il Big Domino, le tre credenze limitanti, le storie che le trasmettono (manuale §10). Solo tre perché intro e stack sono sempre uguali come struttura: si riusano.
</details>

## Esercizio flash (5-10 minuti)

*Esempio costruito, inventato per l'esercizio: non usarlo fuori dall'Academy.*

Hai i pezzi, in disordine, di un webinar per un corso di pianoforte per adulti principianti. Assegna ogni pezzo a uno dei quattro blocchi, poi indica quali due pezzi **non** devono esserci e con quale regola li togli.

1. "Ciao, sono Lia, benvenuti a questa diretta!"
2. Il valore totale del percorso e il prezzo
3. La storia di Lia che a 40 anni non riusciva a leggere uno spartito
4. "Non è colpa tua se ci hai già provato con le app"
5. Tre persone sopra i 50 anni che hanno suonato il primo brano in un mese
6. Lo schema delle tre fasi del percorso, ripetuto tra una fase e l'altra
7. "L'unico modo per suonare da adulto è [domino]"
8. Una pausa a schermo nero "per prendere un caffè"
9. La garanzia
10. "Sì, ma io non ho orecchio"
11. La promessa: come suonare il tuo primo brano entro … senza …
12. Le domande frequenti
