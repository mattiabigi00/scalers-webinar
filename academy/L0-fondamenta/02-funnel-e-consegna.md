# L0.2 · Dove sta il webinar nel funnel, e come si consegna

> **Cos'è:** il percorso del lead dall'ad alla call di chiusura, il punto esatto in cui entra il webinar e la frase con cui il venditore lo consegna. **Durata:** 20-30 minuti. **Prerequisiti:** L0.1.
> **Regole:** N5 ⛔, G21 · **Manuale:** §2, §2.1, §2.2

---

## 1. Il funnel standard dei clienti DFY

Vale per servizi high ticket: minimo 1.000 €, tendenzialmente da 3.000 € in su (manuale §2).

```
   ADV Meta (≈90% del traffico: Facebook + Instagram)
        ↓
   VSL page  →  landing con video sales letter
        ↓
   CTA = survey di candidatura (form con domande qualificanti)
        ↓
   LEAD generato
        ↓
   DISCOVERY CALL del venditore
   → verifica requisiti, budget, problema
   → crea urgenza: trasforma un interesse in priorità assoluta
        ↓
   FINE CALL: il venditore manda il webinar E fissa già la call successiva
        ↓
   Il lead guarda il webinar
        ↓
   CALL DI CHIUSURA (lead già "venduto", manca solo la transazione)
```

*(schema citato dal manuale §2)*

| Tappa | Cosa succede | Cosa c'entra con te |
|---|---|---|
| Ad Meta | circa il 90% del traffico | l'ad è il webinar compresso in 4 righe (L0.1, manuale §9.2) |
| VSL | la CTA porta alla survey | la VSL è il webinar compresso in ~3 minuti |
| Survey | domande qualificanti, nasce il lead | — |
| Discovery | il venditore verifica requisiti, budget, problema e crea urgenza | il webinar arriva **dopo** questa call |
| **Webinar** | **la vendita senza la transazione** | tutto quello che fai nei moduli L1 |
| Call di chiusura | lead già "venduto", manca solo la transazione | il lead arriva con il domino in testa e il prezzo già sentito |

Nota la posizione. Chi guarda il webinar ha compilato una candidatura e ha già parlato con un venditore. Non è traffico freddo: è una persona a cui un venditore ha appena detto "guarda questo, poi ci sentiamo".

## 2. Il passaggio critico: la consegna

Il webinar non si manda come "materiale". Si consegna come **favore scarso**. La formula che usiamo in chiusura di discovery:

> *"Guarda, da quello che ci siamo detti, quello che facciamo può aiutarti esattamente su [risultato X]. Abbiamo troppe richieste, non posso spiegarti tutto dalla A alla Z — proprio per questo ci tengo a darti a titolo gratuito una videolezione direttamente di [esperto], dove spiega esattamente quello che ti serve. Te la mando, quando riesci a guardartela ci sentiamo."* (manuale §2.1)

Tre cose succedono in quella frase (manuale §2.1):

| # | Cosa succede | Dove lo vedi nella frase |
|---|---|---|
| 1 | il webinar diventa un **regalo personalizzato** | "da quello che ci siamo detti… esattamente quello che ti serve" |
| 2 | la **scarsità è dichiarata** senza vantarsene | "abbiamo troppe richieste" |
| 3 | la call successiva si fissa **prima** che il lead riattacchi | "quando riesci a guardartela ci sentiamo" + appuntamento a calendario |

## 3. La regola: N5 ⛔

> **N5 ⛔ Mai mandare il webinar senza la call successiva già fissata.** Si consegna come favore scarso (manuale §2.1).

In parole semplici: il webinar porta il lead fino alla porta della transazione. Se dall'altra parte della porta non c'è già un appuntamento, la vendita resta a metà. È una delle sette regole che il manuale non tocca mai (§11) e una delle dodici ⛔: non si deroga.

Chi la applica è il venditore, non il copy. Ma **tu la scrivi dentro il webinar**, perché la CTA la presuppone.

## 4. Come si vede nel copy

La CTA principale del webinar è **la call già fissata** con "uno dei miei consulenti", senza nome in slide; opzionale un link per chi ha già deciso (G21).

Nel caso Mind Reset (deck v6, slide 124 · s149):

> *"Hai già una chiamata fissata con uno dei miei consulenti. È lì che decidiamo insieme se Mind Reset è la cosa giusta per te. Su questo video non ti chiedo nessun pagamento."*

E subito dopo la CTA secondaria (slide 125 · s150): *"Se invece la tua risposta ce l'hai già, e a volte succede, a chi ha già provato tutto il resto, non serve aspettare la chiamata. Sotto il video trovi il link per iscriverti e prenotare subito la mappatura."*

L'audit del 30/9 lo registra tra le cose pulite: *"Consulente: 'uno dei miei consulenti', nessun nome né `{NOME CONSULENTE}`. La call è già fissata (N5 ⛔ ok)."* (`examples/mind-reset/AUDIT_DECK_V6_2026-09-30.md`, "Cosa è pulito")

## 5. Cosa non facciamo ancora

Il manuale lo dice chiaro (§2.2): funnel per livelli di consapevolezza più bassi, per esempio, non li facciamo ancora. *"Sono gap noti, non errori di ignoranza."* Se in una lettura trovi un modello diverso, non è un errore del nostro: è una scelta di oggi.

## 6. Nel plugin

- **N5 ⛔** blocca i cancelli **7 · Audit** e **8 · Recita e messa in onda** (`references/CANCELLI.md`).
- L'agente `auditor` la controlla (controllo 18, "Consegna": *la CTA presuppone una call già fissata*).
- La checklist pre-volo della skill `webinar-pipeline` chiede che i venditori abbiano lo script di consegna con la regola N5. `CANCELLI.md` (passaggio 8) lo chiama `templates/CONSEGNA_WEBINAR.md`: al 30/9 il file non è ancora nel repo, quindi per ora lo script di consegna si prende dal manuale §2.1.

---

## Domande di verifica

**1. Un venditore ti dice: "Il lead era di fretta, gli ho mandato il link del webinar e lo richiamo la settimana prossima." Cosa non va?**

<details><summary>Risposta attesa</summary>

Viola N5 ⛔: il webinar non si manda senza la call successiva già fissata. La call si fissa prima che il lead riattacchi (manuale §2.1). "Lo richiamo" non è un appuntamento a calendario.
</details>

**2. Perché nella formula di consegna c'è "abbiamo troppe richieste"?**

<details><summary>Risposta attesa</summary>

Perché è la scarsità dichiarata senza vantarsene (manuale §2.1): trasforma il webinar in un favore, non in materiale. Ed è vera: è il motivo per cui il venditore non può spiegare tutto da A a Z (manuale §1).
</details>

**3. Nella slide finale del tuo webinar scrivi "Prenota ora la tua call con Marta". Cosa correggi?**

<details><summary>Risposta attesa</summary>

Due cose. La call è già fissata, quindi la CTA la presuppone ("hai già una chiamata fissata…"), non la chiede (N5 ⛔, G21). E il nome del consulente non si scrive in slide: "uno dei miei consulenti" (G21).
</details>

## Esercizio flash (5-10 minuti)

*Esempio costruito, inventato per l'esercizio: non usarlo fuori dall'Academy.*

"Agrilume" è un servizio di consulenza per agriturismi che vogliono riempire la bassa stagione. Il frontman si chiama Dario Pelvi. Il risultato che il lead ha detto in discovery: "voglio almeno metà delle camere piene tra novembre e febbraio".

Adatta la formula di consegna del manuale §2.1 a questo caso, come la direbbe il venditore a fine discovery. Poi sottolinea le tre parti: il regalo personalizzato, la scarsità dichiarata, la call fissata. Controlla di non aver promesso niente che il venditore non possa mantenere.
