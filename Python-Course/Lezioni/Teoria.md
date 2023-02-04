---
title: Teoria
updated: 2023-02-04 10:51:31Z
created: 2023-02-03 11:28:51Z
tags:
  - python
---

03/02/2023
# Introduzione
- Docente: Alessio Bechini
- Prende le presenze (ma solo per statistica non ai fini del titolo)
* * *

## Compilation vs Interpretation

Compilation: trasformazione del programma di alto livello in un linguaggio di basso livello ovvero in istruzioni che la CPU è in grado di eseguire tramite l'utilizzo di compilatori. Per CPU diverse la compilazione deve essere diversa. Se voglio cambiare qualcosa a livello di codice devo ricompilare tutto.

<span style="color: #83d17f">Pro</span>: prestazioni elevate
<span style="color: #ff7f7f">Contro</span> bassa flessibilità di utilizzo a supporto della compilazione

Interpretation: Per colmare questo gap si è pensato di sviluppare un programma in grado di leggere un programma scritto in alto livello ed eseguirlo in termini di istruzioni da dare alla CPU. L'esecuzione del programma stesso sfrutta un intermedio ovvero l'interprete. Le prestazioni saranno ovviamente più basse.

<span style="color: #83d17f">Pro</span>: debugging più semplice e flessibilità maggiore
<span style="color: #ff7f7f">Contro</span>: prestazioni più basse


![dfe5ab257c0df1bd656f81cc3c8f6f65.png](../_resources/dfe5ab257c0df1bd656f81cc3c8f6f65.png)

All'interno dell'interprete posso avere un codice sorgente ma viene analizzato comando per comando ed eseguito comando per comando. Anche in questo caso devo tenere traccia di simboli usati nel programma (ad esempio le variabili). La differenza fondamentale sta nell'utilizzo della tabella dei simboli perchè viene utilizzata una volta soltanto ai fini della generazione del codice nel caso compilato mentre nel caso interpretato dovrà contenere anche tutte le informazioni per supportare l'esecuzione del programma e quindi è a carico dell'ultimo modulo (Executor) ad esempio andrà a leggere dalla tabella dei simboli in quale punto del programma ci troviamo quindi i valori memorizzati fino a quel punto e avrà anche un aggiornamento del contenuto della tabella dei simboli. Inoltre le strutture dati a supporto del programma stesso possono essere molteplici.

Si è pensato di migliorare la situazione e prendere il meglio dei due. Un possibile modo di migliorare il tutto è ottenere una soluzione ibrida in cui l'interprete esegue comandi la cui complessità è intermedia tra i comandi del linguaggio di alto livello e il codice macchina. Avrà bisogno della sua tabella dei simboli che leggerà ed andrà poi a scrivere ed aggiornare. Per la sua esecuzione dovrà avere il codice intermedio che rappresenta il programma espresso non più in linguaggio di alto livello ma in liguaggio intermedio (bytecode). Per ottenerlo posso usare un approccio a compilazione che mi restituisce il bytecode che va in ingresso a un interprete che sarà un po più veloce. L'esecutore è un programma che dovrà essere fatto girare su delle CPU che possono essere di vario tipo. Ma con OS e hardware diversi posso sviluppare un esecutore che sia in grado di avere in input sempre lo stesso codice intermedio. Quindi ci permette di evitare lo svantaggio dell'approccio compilativo che era specifico per ogni CPU.

![b5c785884eacb407cdf5097751da0dd0.png](../_resources/b5c785884eacb407cdf5097751da0dd0.png)

Comunque abbiamo uno step di compilazione ed uno di esecuzione. Ci sono vari modi con cui questi step possono essere portati avanti. Alcuni linguaggi adottano un organizzazione di un tipo altri di altro tipo. JAVA adotta un approccio di questo genere. L'executor è la java virtual machine JVM. L'insieme di questi blocchi fa parte di javac, compilare del bytecode.

Python adotta un approccio di questo genere con alcune differenze rispetto a JAVA in quanto la generazione del codice intermedio è fatta partire dall'interprete ovvero la generazione del codice intermedio viene fatta al momento senza che il programmatore provveda alla compilazione del programma. È il sistema stesso che si occupa di tutto del processo.
Abbiamo una tabella dei simboli sia sulla destra che sulla sinistra.

## Python è un...
Linguaggio di scripting: il loro scopo è quello di controllare le applicazioni.

i linguaggi di programmazione invece hanno come scopo lo sviluppo di vere e proprie applicazioni.

Gli script in genere sono interpretati in altri casi invece vengono compilati su rappresentazioni intermedie o bytecode. E poi il bytecode a sua volta viene interpretato.

## IDE
L'ide che verrà utilizzato durante il corso è [Spyder](https://www.spyder-ide.org/).

Una distribuzione è un insieme di strumenti che comprendono sia il linguaggio stesso sia un insieme di altri tool.
Inoltre verranno visti i Jupiter Notebooks (data analysis) che sono lo strumento in cui il linguaggio viene più frequentemente usato. All'interno della distribuzione Anaconda è possibile gestire le librerie da installare e se vi è la necessità di usare linguaggi e librerie in ambienti diversi è possibile usare ambienti diversi con versioni e librerie differenti del linguaggio.

Le versioni di python a cui il corso fa riferimento sono superiori alla **3.0**. L'ultima versione precedente alla 3.0 è la **2.7**.
***
***
04/02/2023

Per far partire l'interfaccia grafica di gestione del sistema Anaconda Navigator lanciare il comando `anaconda-navigator` da terminale e selezionare Spyder:
![fdb5c968571a97b8e5c2a354ca5fc1ec.png](../_resources/fdb5c968571a97b8e5c2a354ca5fc1ec.png)

Conda è l'applicazione a linea di comando, mentre Anaconda è l'interfaccia grafica.

![dd434d1c4303673b9b7621d163c36117.png](../_resources/dd434d1c4303673b9b7621d163c36117.png)
Un environment è un ecosistema Python in cui decidere quale versione usare e quali librerie utilizzare. Spostarsi da un ambiente all'altro significa cambiare tutte le configurazioni quindi richiede un pò di tempo. Per creare un nuovo environment c'è il pulsante "Create":
![ad9b812dc51e43bc106d9c1a47f41b7b.png](../_resources/ad9b812dc51e43bc106d9c1a47f41b7b.png)

Sulla destra, relativamente all'ambiente, sono i vari pacchetti che sono presenti nell'ambiente stesso ovvero le diverse librerie. C'è il nome, la descrizione e la versione. Questi sono stati scaricati e installati in automatico da alcune repository online, che nel gergo di Anaconda Navigator si chiamano "Channels":
![fe10e8a69d3f9f87399661d8574b47b3.png](../_resources/fe10e8a69d3f9f87399661d8574b47b3.png)

Dato che vengono mantenute anche le versioni dei pacchetti è possibile vedere la versione installata e vedere sulla repo se ci sono versioni più recenti e quindi vedere se si può caricare la versione più aggiornata.

La "Home" cambia a seconda dell'ambiente selezionato:
![ab32d2f1297eab0a273f09d2251a80a3.png](../_resources/ab32d2f1297eab0a273f09d2251a80a3.png)

Lanciando "Spyder" è possibile notare che c'è una parte dedicata all'editing dei programmi, inoltre è presenta una console in basso a destra che è diversa dalla console di sistema, si chiama IPython e ci indica anche la versione di Python usata dalla console.

La zona in alto a destra "Help" permette di accedere a una descrizione dei vari comandi in modo automatico:
![cb5f44aeee22e738254109f30331a3ec.png](../_resources/cb5f44aeee22e738254109f30331a3ec.png)

La directory qui indicata è la directory di lavoro per l'esecuzione dei programmi:
![e11b7638903a8ad872eed322994c56fc.png](../_resources/e11b7638903a8ad872eed322994c56fc.png)

A volte si hanno problemi per l'accesso al file per via programmatica proprio per mis-configurazioni della directory di lavoro. Di default la directory di lavoro coincide con la directory in cui si trova il file `.py`.
***
## Esecuzione di programmi Python
È possibile inserire una sequenza di comandi in un file con estensione `.py`. Se voglio eseguire l'interno programma, l'esecuzione del programma corrisponde a chiamare l'interprete e passandogli il file `.py`. Per rendere l'esecuzione del file più semplice in sistemi UNIX, devo fare in modo che se io decido di usare quel file come se fosse un eseguibile, deve essere richiamato in automatico l'interprete, ma l'OS a priori non può sapere dove si trova quello specifico interprete, quindi usiamo l'hash bang che il sistema operativo userà per capire dove si trova l'interprete:
![f66681d23726ca0c7bba35e5c087a5dc.png](../_resources/f66681d23726ca0c7bba35e5c087a5dc.png)
e da questo momento in poi è possibile usare lo script come se fosse un qualsiasi comando del sistema operativo.
***
## Storia
Esistono 2 differenti versioni con differenze strutturali molto importanti.
![ff2528b8dbd7b18206ae96302ef5e181.png](../_resources/ff2528b8dbd7b18206ae96302ef5e181.png)

Dal 2008 Python 2 e Python 3 hanno iniziato a seguire binari molto differenti:
- La gestione degli interi
- La sintassi di stampa a video `print`
- Iteratori, generatori, views
- è possibile convertire uno script python2 in uno script python3 tramite il tool `2to3`.


## Visione strutturale di Python

### Handled entities (HE)

Qualsiasi HE può essere un oggetto, un nome o un namespace:
![28862312fbdcd39cfeddf1d08d3c24bf.png](../_resources/28862312fbdcd39cfeddf1d08d3c24bf.png)

La gestione delle varie funzionalità di python si basa sull'organizzazione di questo semplice schema.
- 📂 **Oggetti**: blocchi di base il cui scopo è quello di contenere dei dati (*ObjectX* e *ObjectY* sono degli oggetti di esempio). I moduli, le funzioni, sono oggetti python. Quindi l'oggetto python è il blocco fondamentale della struttura di python. Per poterli referenziare e identificare in modo univoco posso associare un nome. Ogni oggetto ha
	- **identità**: è la locazione di memoria in cui è salvato l'oggetto in memoria RAM
	- **tipo**: definisce tutti i possibili valori che un oggetto può assumere e tutte le operazioni che possono essere svolte sull'oggetto stesso. Per conoscerne il tipo esiste il comando `type()`
	- **valore**: corrisponde a ciò che è scritto nell'oggetto. Nell'esempio in basso sarebbe 127 o 42.
		- **mutable**: possono essere modificati sul posto *in place*, ovvero senza mutare l'identità dell'oggetto, cioè il suo indirizzo in RAM
		- **immutable**: NON possono essere modificati, ovvero il valore dell'oggetto non può cambiare
		
	Supponiamo di voler creare un oggetto contenente un valore intero, se voglio che venga inserito in memoria e che un certo nome (es. ciro) lo riferisca il comando da dare è il seguente: `ciro = 127`. Il sistema prende la rappresentazione "127", ne ricava il valore corrispondente, crea un oggetto in memoria la cui rappresentazione intera è 127 e lo salva in memoria. Crea poi un nome che si chiama <span style="color: #007dff">ciro</span>, grazie all'uguale, per referenziare l'oggetto. In quale posizione in memoria è stato collocato? Esiste il comando `id()` che mi restituisce la locazione di memoria dove è stato collocato l'oggetto "ciro".
	![11f383533c100319fa2e0a20b572c781.png](../_resources/11f383533c100319fa2e0a20b572c781.png)
Se supponiamo che ciro abbia questo nome all'anagrafe ma tutti dalla nascita lo chiamano "nino", nino è un alias di ciro, quindi il nome nino punterà sempre allo stesso oggetto puntato da ciro:
![0fd9637de6a3e627a0cdbe0f965a33c9.png](../_resources/0fd9637de6a3e627a0cdbe0f965a33c9.png)
L'operatore `is` prende l'identità dei due argomenti e ne valuta l'uguaglianza:
![c3c691e358cc4bb4b8f2f50516480bfe.png](../_resources/c3c691e358cc4bb4b8f2f50516480bfe.png)


- 🔤 **Nome**: è una stringa di lettere che identifica uno o più oggetti. Nell'esempio <span style="color: #ff7f7f">name1</span> ha un binding con l'oggetto <span style="color: #7f7f7f">objectX</span>. Il <span style="color: #ff7f7f">name2</span> e <span style="color: #ff7f7f">name3</span> sono **alias** per lo stesso oggetto <span style="color: #7f7f7f">objectY</span>. È importante che un oggetto sia referenziato da un nome, perchè altrimenti quell'oggetto sarà totalmente inutile e non sarà utilizzabile da nessuno. Infatti il sistema Python quando vede oggetti senza alcun binding con un nome, se ne sbarazza, quindi li cancella dalla RAM. Il sistema che si occupa di fare questo è il <span style="color: #ffc86c">garbage collector</span>. Un modo per gestire i nomi è di raccoglierli all'interno di insiemi detti namespace.



- 🗃️ **Namespace**: il raggruppamento di nomi ha la stessa funzionalità delle tabelle dei simboli accennate nella lezione precedente. In genere non si usa un solo namespace per l'esecuzione di un programma, ma più di uno. È possibile che namespace diversi debbano essere ricercati dall'interprete per ricercare i bindings durante l'esecuzione del programma. Se volessi rimuovere un nome dal namespace posso farlo tramite il comando `del nome`  : 
![8fe2d2469f56ea586330f1630026122e.png](../_resources/8fe2d2469f56ea586330f1630026122e.png)

Un oggetto può essere messo in relazione con alcuni attributi che appartengono ad essi. Per supportarla a livello di sistema, ho un namespace principale con il nome <span style="color: #ff7f7f">foo</span> e gli altri due oggetti che devono essere suoi attributi (<span style="color: #ff7f7f">bar</span> e <span style="color: #ff7f7f">bar2</span>), quindi è necessario creare un namespace per il singolo oggetto "foo":
![dbae0e7e468c4346d379280d3cbe1f6a.png](../_resources/dbae0e7e468c4346d379280d3cbe1f6a.png)

Una funzione può essere un attributo di un oggetto, e verrà chiamata metodo dell'oggetto.

Quando vengono chiamate delle funzioni o dei metodi si crea un *namespace temporaneo* a supporto dell'esecuzione della funzione stessa. Esiste un comando per conoscere gli attributi, ovvero i nomi presenti nel namespace associato all'oggetto riferito dal nome foo: `dir(foo)`.
![179bb769ffca5381f479610e252e4dd6.png](../_resources/179bb769ffca5381f479610e252e4dd6.png)

Alcuni oggetti hanno la funzione di chiamata *"function-call operation"*. Esistono diversi oggetti python che appartengono a questa categoria, che quando vengono chiamati creano un oggetto con il valore passato come argomento della chiamata:
- funzioni
- tipi built-in: int, list, tuple
- metodi

```python 
int(78)
Out[22]: 78
```
Con questo comando l'oggetto è stato creato in memoria ma è stato subito dato in pasto al garbage collector che lo ha rimosso immediatamente. Non potendolo referenziare non posso neanche sapere dove si trova in RAM.

```python
id(int(78))
Out[23]: 139872530858768
```
In questo caso invece l'identità l'ho avuta ma adesso non ho più la possibilità di andare a recuperare l'oggetto.  