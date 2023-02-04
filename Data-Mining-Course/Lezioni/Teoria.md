---
title: Teoria
updated: 2023-02-04 13:00:01Z
created: 2023-02-04 11:01:04Z
---

04/02/2023
## Introduzione
- Docente: Francesco Marcelloni
- Mail: francesco.marcelloni@ing.unipi.it
- Useremo dei data set aventi righe con valori
- L'esame di maggio consisterà in data set, un paio, di cui bisogna applicare alcune tecniche di data mining e raccontare il risultato ottenuto
* * *

## Data mining e machine learning
![0110367f305308e6f5a000eb03be8c3e.png](../_resources/0110367f305308e6f5a000eb03be8c3e.png)
Si tratta della pratica per ricercare in grandi moli di dati dei pattern utili, ovvero conoscenza. Se però individuiamo la traduzione effettiva dall'inglese, *mining* si intende l'estrazione mineraria, quindi significa *estrazione di dati*. Ma questa traduzione non corrisponde alla definizione. Noi i dati li abbiamo già quindi ci interessa estrarre dei pattern o conoscenza dai dati che possono essere in grande mole e che possono descritti da un numero elevato di caratteristiche e in modo diverso.
Questo termine quindi dal punto di vista inglese non corrisponde con quello che tutti indendono per data mining. Nomi alternativi come Knowledge discovery sarebbero più indicati, ma oramai Data mining è entrato nel linguaggio comune. Il data mining è davvero rilevante oggi perchè avendo tanti dati diventa difficile analizzarli. 

Il machine learning (ML) è invece la capacità di un computer di apprendere dall'esperienza, insegnando al computer a risolvere dei problemi usando dati precedenti o passati. Spesso in data mining si usano delle tecniche del ML (classification, clustering, regression, etc...).
![40f55158b31b20a17d9b361e1cce13d8.png](../_resources/40f55158b31b20a17d9b361e1cce13d8.png)

Le cinque più grandi compagnie di High-tech in questa figura mostrano che esse hanno un valore da un punto di vista economico confrontabile con altre 282 aziende:
![c8f4d59a22c7cadc9613fcc66e7d4cdd.png](../_resources/c8f4d59a22c7cadc9613fcc66e7d4cdd.png)

Alphabet, Amazon e Facebook sono 3 aziende che si occupano dell'elaborazione e raccolta di dati. Da questo spaccato si capisce quanto il dato sia importante dal punto di vista economico.

## Malware detection
Nell'ambito della cybersecurity, il data mining può essere utile per fare <span style="color: #7f7fff">MALWARE DETECTION</span> ad esempio. Quindi usiamo dei dati etichettati in precedenza perchè associati a specifici attacchi per poterli previnire.
- **Anomaly detection**: avendo modellato il comportamento normale, possiamo riconoscere attacchi di vario tipo in quanto abbiamo modellato con i dati il comportamento normale, quello lecito
- **Misuse detection:** nel secondo caso invece abbiamo addestrato il sistema a riconoscere solo gli attacchi forniti in input, nuovi attacchi potrebbero non essere riconosciuti.

***

## Data sets

Tipicamente quello che un ingegnere si trova a fare in questo settore è ragionare su algoritmi disponibili in librerie, provare a risolvere il problema e poi confrontare i risultati ottenuti e trovare l'algoritmo migliore.

Il punto di partenza però prima di parlare di algoritmi sono i dati. Gli oggetti dati, le istanze o campioni sono sinonimi per descrivere un entità, ad esempio per un database di vendite, un oggetto può essere un prodotto da vendere o un cliente. Se parliamo di cybersecurity, un oggetto può essere un traffico in rete. Gli oggetti sono descritti da attributi, questi possono essere di vario tipo e servono a definire l'oggetto stesso. Se volessimo fare un paragone con la memorizzazione all'interno della base di dati, potremmo dire che righe corrispondono agli oggetti e le colonne agli attributi.

Gli attributi sono delle caratteristiche che servono a rappresentare l'oggetto stesso.
Esempio: per un cliente gli attributi possono essere l'ID, il nome, la partita iva, etc...

Gli attributi sono contraddistinti dai loro tipi. Noi vedremo il tipo nominale, binario e numerico.
![627adb9930da87cb3bdc32700de567b3.png](../_resources/627adb9930da87cb3bdc32700de567b3.png)

Cercheremo anche di capire la somiglianza tra oggetti sulla base di attributi, perchè gli algoritmi useranno qualche calcolo di somiglianza tra oggetti e dobbiamo capire come esprimere la somiglianza quando gli oggetti hanno attributi di tipo differente.

Il tipo:
- **nominale**: si contraddistingue dal fatto che i possibili valori sono delle etichette, dei nomi e non c'è un ordinamento. Es. i capelli possono grigi, gialli, rossi. Non avendo un ordinamento non posso neanche dire che rosso sia più vicino a biondo o grigio. Questo è un problema perchè quando dobbiamo definire la distanza tra oggetti dobbiamo sapere che non c'è un ordinamento. Calcoliamo la distanza tra due oggetti nominali 

![6070aed2f9c22cca5f03b4ef9edad7ec.png](../_resources/6070aed2f9c22cca5f03b4ef9edad7ec.png)

`m`: è il numero di valori uguali tra due oggetti, `p` è il numero totale di variabili

La distanza viene calcolata andando a vedere quanti sono gli attributi nominali che descrivono i due oggetti che hanno lo stesso valore. Questa è l'unica cosa che possiamo fare per calcolare la distanza tra oggetti con valori nominali, non essendoci un ordinamento, quindi l'unica cosa valutabile è vedere se quell'attributo ha lo stesso valore in entrambi gli oggetti. Supponendo di avere `p` attributi, se `p` attributi hanno gli stessi valori tra i 2 oggetti, la distanza tra i 2 oggetti è nulla. Se nessun attributo è uguale, la distanza tra i due oggetti è massima.

Un tipo di attributo nominale molto particolare è l'attributo binario in quanto come gli attributi nominali ha 2 possibili valori, true/false, 0/1 è particolare perchè ha solo 2 valori. Possiamo avere due tipi di attributo binario:
- simmetrico: i due possibili valori sono ugualmente importanti o in altri termini si presentano con la stessa probabilità ad esempio il genere
- asimmetrico: i risultati non sono ugualmente importanti, uno dei due valori si presenta con un alta probabilità rispetto all'altro. Nei test medici, ad esempio, la positività è più bassa rispetto alla negatività

Per convenzione si assegna 1 al risultato più importante che però non è detto che sia quello più probabile.
![f751f54f4e69d86385e847c681507190.png](../_resources/f751f54f4e69d86385e847c681507190.png)

È necessario fare distinzione tra simmetrico e asimmetrico, perchè se dobbiamo calcolare la distanza tra i due oggetti i e j definiti attraverso attributi binari. Per capire come è calcolata la distanza bisogna fare riferimento alla tabella: rappresenta l'oggetto i e l'oggetto j e ogni cella rappresenta quanti attributi binari hanno valore 1 per l'oggetto i e lo stesso valore 1 per l'oggetto j. q rappresenta il numero di attributi binari con valore 1 in entrambi gli oggetti. s sono gli attributi in cui l'oggetto i ha valore 1 e l'oggetto j  ha valore 0. t attributi in cui entrambi hanno valore 0.
La somma al denominatore corrisponde al numero totale di attributi rappresentato da p, al numeratore abbiamo il numero di attributi per cui il valore per i e per j sono differenti. infatti r corrisponde a i con valore 1 e j 0 mentre s viceversa. r+s è il numero di attributi in cui i e j hanno valori differenti. Se r+s sono uguali a 0 significa che i e j vanno a coincidere. 

Dove vediamo questa differenza tra attributi binari simmetrici e asimmetrici? Nella formula la differenza non c'è.
Cosa succede se gli attributi sono binari asimmetrici?
![e5b84c320a0696829fb5d50810cde402.png](../_resources/e5b84c320a0696829fb5d50810cde402.png)
nel caso di attributo binario asy, il valore che assegniamo con 1 è quello più importante ma con meno probabilità, quindi 1 ha una probabilità bassa di apparire, 0 alta. Dato che 0 appare molto di più, ci aspettiamo sia per i che per j che appaia 0 molte più volte, quindi t sia elevato. Otteniamo nel calcolo che t è elevato quindi la distanza apparità sempre molto bassa. Questo è il motivo per cui con attributi binari asy non consideriamo t, questo ci consente di avere una distanza elevata quando ci sta una differenza effettiva tra i e j non prendendo in considerazione il numero t che è tipicamente elevato con attributi asimmetrici binari.

- **ordinali**: da un punto di vista dell'attributo i possibili valori sono delle etichette ma la differenza sta nel fatto che si tratta di valori ordinabili, ovvero l'ordine è significativo. Es: l'attributo size con valori small, medium, large. Nella nostra mente sappiamo che piccolo è più vicino a medio di quanto non lo sia rispetto a grande. Quando calcoliamo la distanza tra 2 oggetti che sono definiti attraverso attributi ordinali dobbiamo considerare l'ordinamento.
![2b4c68af7e338cce61dbfcda75ad0906.png](../_resources/2b4c68af7e338cce61dbfcda75ad0906.png)

Andando a trasformare i valori testuali in valori numerici e trasformando il calcolo della distanza. Associamo ad ogni possibile valore ordinale un numero crescente, partendo da quello più basso. Nel caso della slide, associamo 1 a small, 2 a medium e 3 a large. Questo ci realizza la intuizione di prima, sappiamo che small è più vicino a medium rispetto a large, noi diamo questa idea perchè 1 è più vicino a 2 che a 3. Prendiamo il nostro valore asssociato con small medium e large.
Trasformare small signfica prendere il valore mappato quindi 1 - 1/ 3 - 1 ==> 0, medium era mappato con 2 quindi: 2 - 1/ 3-1 ==> 0.5, large invece 3 -1 / 3- 1 ==> 1.

A cosa serve normalizzare⁉️
Si normalizza per far variare i valori nello stesso range e far pesare i valori all'interno della distanza euclidea nello stesso modo.

Abbiamo mantenuto l'ordinamento ma trasformando le etichette in numeri. Il vantaggio è che l'attributo ordinale nominale è un attributo numerico. Questo ci porta a dire che se noi avessimo degli oggetti descritti da attributi ordinali, dopo la trasformazione abbiamo attributi numerici, e possiamo calcolarne la distanza, ad esempio la distanza euclidea.

- **quantità**
	- intervalli: nel primo caso abbiamo gli attributi che sono misurati su una scala di unità con lo stesso intervallo ma che hanno un anomalia non avendo uno 0. Le temperature in °C considera delle unità che hanno la stessa dimensione, quello che non abbiamo è che lo 0°C non è un vero 0 perchè sappiamo che non esiste un vero 0°C, fatto sta che una divisione tra temperature espresse in gradi celsius non ha significato. La temperatura in gradi K ha uno 0 e ha senso fare un rapporto tra temperature. I gradi K da questo punto di vista sono dei razionali.
	- razionali: lunghezze, quantità monetarie

Le cose si complicano se un oggetto può essere descritto da diversi tipi di attributi. Per calcolare la distanza tra 2 oggetti è calcolare la distanza per ciascun attributo, e poi fare una media pesata con il peso che corrisponde al numero di attributi di quel tipo.


I dati li vedremo come singolo oggetto con un certo numero di attributi. Quando approcciamo un problema di data mining è cercare di capire meglio come sono distribuiti i dati, per capire cosa possiamo aspettarci. Per visualizzare un dato non è facile, perchè se un dato è rappresentano da tante dimensioni non possiamo darne una rappresentazione visuale, a meno di non visualizzare  come i valori sono distribuiti attributo per attributo. Per far questo abbiamo il Box Plot.

## Box plot
Consente di capire come i valori sono distribuiti per uno specifico attributo. Si tratta di una rappresentazione grafica basata su una scatolina:
![f9a6b316636d75cb6844e7ac696f74e2.png](../_resources/f9a6b316636d75cb6844e7ac696f74e2.png)

che rappresenta 5 valori statistici. Il q1 e q3 sono il primo e il terzo quartile. Il quartile è il valore che individua il 25% dei valori con valore inferiore a quello del quartile. Ci sono il 25% di punti dell'attributo che stiamo considerando che cadono al di sotto di 51. Il terzo quartile corrisponde a 86 significa che ci sono l'75% dei punti al di sotto di quel valore.

Presi tutti i valori corrispondendi all'attributo, ordinati, noi andiamo dal valore minimo al massimo. Ci trasmette un idea molto grossolana di come sono distribuiti i valori all'interno dell'attributo. Se vediamo il blox pot, il 50% dei valori tra i due quartili, sono tra 51 e 86. Poi abbiamo un 25% dei valori che varia tra 51 e 19 e un 25% tra 86 e 100.

![9221440eb7a6a140bbed652bbdd0d3e1.png](../_resources/9221440eb7a6a140bbed652bbdd0d3e1.png)
I box plot qui sono rappresentati in modo diverso. Ci sono gli * che sono gli outliers, ovvero valori molto differenti rispetto ai valori tipici del dataset. Sono quei punti che hanno un valore più basso o più basso di 1.5 volte IQR, ovvero la differenza tra il quartile q2 e il quartile q1. Questo blox pot ci consente di avere un idea della distribuzione dei dati ma anche confrontare le differenti distribuzioni. Il secondo box plot ha una distribuzione dei punti molto concentrata mentre il terzo ha una distribuzione molto sparsa. Questa idea mi è data utilizzando solamente 5 valori statistici. In generale si usa per confrontare la distribuzione relativa allo stesso attributo. Se si ha lo stesso range di variazione, si può usare per confrontare anche attributi diversi.



Un altra rappresentazione grafica è l'istogramma ma spesso c'è una confusione con il bar chart. Il valore nell'istogramma è dato non dal valore dell'ordinata ma dall'area. Per ogni intervallo che consideriamo per un attributo, ci dice quanti valori abbiamo in quell intervallo. Tipicamente usiamo l'ordinata della barra corrispondente, ma la frequenza è l'area della barra. Tipicamente usando intervalli della stessa dimensione, è ovvio che considerare l'area o l'ordinata è analogo. Ma dal punto di vista formale, la frequenza di quel valore è associato all'area.
![2f87636ff3dcea7e9b664728a620f843.png](../_resources/2f87636ff3dcea7e9b664728a620f843.png)

Quindi divide il dominio dell'attributo in intervalli (in questo caso della stessa dimensione) e conta i valori nei singoli intervalli.

❓️Tra le 2 rappresentazioni, quale è più espressivo? L'istogramma

Esempio: con una distribuzione bimodale o unimodale
![a4a4374c8243e52541adaf3b575e8746.png](../_resources/a4a4374c8243e52541adaf3b575e8746.png)

questi corrispondono allo stesso boxplot, che rappresentando 5 statistiche è fatto solo su 5 numeri. 

## Scatter Plot
Rappresentazione diversa dalle precedenti perchè consente di confrontare 2 attributi. Usiamo un attributo sulle ascisse e ordinate e rappresentiamo i punti nel piano che si forma. Può essere utile perchè consente di capire in modo semplice se esiste una relazione tra i 2.

![cfa9be1e544a0fe015944ca874cb8624.png](../_resources/cfa9be1e544a0fe015944ca874cb8624.png)

Nel primo scatter plot all'aumentare del valore della x aumenta anche la y, lo scatter plot è molto concentrato all'interno di una linea. Nel secondo è un fenomeno inverso.
Questi 2 scatter plot ci fanno capire che esiste una correlazione tra i 2 attributi, all'aumentare del valore di un attributo aumenta anche l'altro o vicersa, quindi i 2 attributi hanno una quantità informatica simile, ovvero il trend è lo stesso. Se hanno uno stesso trend, due attributi portano uno stesso contenuto. Potremmo pensare di non usarli entrambi dal punto di vista di tecniche di datamining, quindi possiamo decidere di usarne uno solo.

Nel caso dello scatter plot in basso invece è ovviamente differente in quanto non si muove lunga una linea, vi è una correlazione positiva fino a un certo valore della x e poi da quel valore in poi la correlazione diventa negativa. Questa analisi di correlazione attraverso scatter plot può essere utile per farci capire che ci sono coppie di attributi ridondanti. 
La produzione di scatter plot può avvenire per attributi di tipo numerico. 

## Data visualization
Quando i dati sono espressi in modo testuale, essi sono trasformati con delle tecniche in numeri.
![5dbc4aa8df40594058749386261a87b1.png](../_resources/5dbc4aa8df40594058749386261a87b1.png)

Questa visualizzazione permette di capire quali sono le parole più frequentemente usati nel documento stesso. Viene associata una dimensione del font più grande con le paroli più frequenti.

# Data cleaning

I dati grezzi dai quali si parte, possono essere estratti da database, da sensori IoT, che per loro natura sono sporchi, incorretti, a causa di errori umani o del computer o di trasmissione. Quando parliamo di rumore, lo si associa a dati prelevati da sensori, oltre alla misura del parametro che stiamo raccogliendo, ad esempio temperatura o umidità, abbiamo anche una sorta di rumore dato dal dispositivo che stiamo analizzando. Questo rumore va eliminato in quanto ci da un oscillazione di valori che non rappresenta la grandezza che stiamo acquisendo. Ma esiste un rumore anche con dati estratti da database. Rumore dovuto al fatto che per alcuni record i dati sono incompleti, o inseriti male. In alcune situazioni il rumore è creato intenzionalmente, ad esempio se la data di nascita non è inserita viene dato il valore di default 01/01/1901.

![542da915678dc395180e8bfcec2cc4c5.png](../_resources/542da915678dc395180e8bfcec2cc4c5.png)

## Incomplete Data
<span style="color: #ffc86c">Un oggetto incompleto significa che manca qualche valore per qualche attributo</span>.
Supponiamo di voler calcolare la distanza tra 2 oggetti espressi con attributi numerici e supponiamo che per uno di questi non ci sia un valore. Quando calcoliamo la distanza euclidea, da un punto di vista algoritmico non viene valutato se si tratta di un valore inserito li casualmente o meno. Quindi applichiamo degli algoritmi per cui consideriamo che tutti i valori siano validi e presenti, ma potrebbe esserci in memoria in quella cella un valore casuale non compilato intenzionalmente. Se un valore manca dobbiamo fare in modo di eliminare il problema.

- Se ho un oggetto, una tupla, senza un valore, elimino l'oggetto, non lo prendo in considerazione. È ragionevole se gli oggetti con dati mancanti sono in percentuale infinitesima rispetto al numero totale di oggetti.

- Un approccio alternativo è quello di inserirli manualmente. Funziona solo se i dati con valori mancanti sono pochi.

- Un modo potrebbe essere di inserire dove ho un dato mancante una label, ad esempio unknown, che mi segnala che li c'è un valore mancante, dal punto di vista dell'elaborazione non me ne faccio nulla ma almeno lo segnalo esplicitamente.

- La soluzione è prendere il valore mancante, calcolare la media dei valori e sostituire il valore mancante con l'attributo.

- Oppure calcolare la media solo per gli ogggetti appartenenti alla stessa classe e sostituire il valore mancante con questa media fatta sugli oggetti della stessa classe. 

- L'ultimo approccio è sviluppare un sistema che prendendo dei valori vicini al valore mancante, riescono a generare il valore mancante. Questo approccio ovviamente ha i suoi aspetti negativi, in ogni caso quel sistema va generato e non siamo sicuri che i valori generati siano vicini al valore che avrebbe dovuto avere quell'oggetto.

## Rimozione del rumore
Viene chiamata smoothing, ovvero l'idea di lisciare qualcosa. Prende questo segnale che è rumoroso e cerca di lisciarlo portando alla luce solo il segnale e rimuovendo il rumore. Uno degli algoritmi di smoothing è quello rettangolare.
Si prende il campione e si considera una finestra attorno al campione. Ad esempio con una finestra di 3 cmpioni, il campione al centro viene sostituito dalla media dei 3 campioni. Sostiuendolo con la media ho l'effetto di lisciamento perchè considerò la media, quindi considero nella finestra più campioni e quando ne ho uno molto diverso dagli altri, sostituendolo con la media.

![270bfae018568606d4ba7529ce3e0065.png](../_resources/270bfae018568606d4ba7529ce3e0065.png)

La formula considera una finestra con 3 campioni, sostituisco il campione al centro con indice j con la media dei campioni precedenti e successivo.

La dimensione della finestra liscia di più o di meno il campione:

![1a54d02cbd4cde50202f512396db47c0.png](../_resources/1a54d02cbd4cde50202f512396db47c0.png)

Nella finestra con 51 punti il rumore si è ridotto ma la variazione non è più brusca ma graduale e deriva dall'applicazione del filtro, applicato con una finestra molto ampia, ovvero rimuove rumore ma sposta anche i momenti in cui avviene la transizione. Quando applichiamo un filtro di smoothing, con una finestra maggiore riduciamo maggiormente il rumore ma la variazione brusca viene graduata e ritardata.