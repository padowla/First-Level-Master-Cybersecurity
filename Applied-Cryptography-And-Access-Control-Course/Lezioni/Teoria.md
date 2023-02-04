## Introduzione
- Docente: Gianluca Dini, Pericle Perazzo
- Mail: gianluca.dini@unipi.it
* * *

Dobbiamo considerare che abbiamo un avversario che vuole attaccare il nostro sistema.
L'avversario cercherà di violare:
1. Confidenzialità
2. Integrità
3. Disponibilità

La crittografia ci permette di proteggere la confidenzialità e l'integrità dei dati.
La disponibilità si protegge in altri modi che non sono metodi crittografici.
Parleremo di crittografia applicata in quanto non progetteremo algoritmi crittografici perchè inerente l'ambito matematico. Noi invece ci chiederemo come usare gli algoritmi per proteggere i dati trasmessi in rete. Ci interessa la parte applicativa. Cos'è un certificato, quali vantaggi mi da una firma digitale, etc...

***

![86c8f5828233b1aeb41f6eef238e509f.png](:/b05b32f7abc74db4ba9d2a48516eca6d)


La storia ci insegna che nella maggior parte dei casi gli algoritmi crittografici "home-made" possono essere facilmente rotti. Usiamo sempre algoritmi standard, ovvero progettati dai migliori crittografi in circolazione e attaccati e analizzati e alla fine di questo processo si è deciso che si trattava di algoritmi sicuri e prestazionali.

La crittografia è importante in quanto nei servizi e apparati che usiamo la troviamo ovunque:
- HTTPS: Web Traffic
- Wireless Traffic: 802.11i WPA2, GSM, Bluetooth
- File cifrati su disco: EFS, TrueCrypt
- Protezione dei media: DVD(CSS) e Blu-ray (AACS)
***

## Cosa significa "Security" ❔
![689128848448f4b03620ecdbbf4d7c16.png](:/cca40e477e2840a9b65317fd2da7c682)
Se abbiamo una dimostrazione matematica per cui un algoritmo è sicuro quell'algoritmo è sicuro matematicamente. Quell'algoritmo è male utilizzabile nella pratica quindi si usa molto poco. Ne vedremo un esempio dopo.

La seconda dice che "rompere quell'algoritmo matematicamente parlando o in termini di tempo è tanto difficile quanto risolvere un problema complesso". Se abbiamo un numero con 100 cifre decimali, fare la fattorizzazione è molto difficile, quindi anche usando i migliori elaboratori ci vogliono migliaia di anni. Se dimostro che rompere quell'algoritmo corrisponde a velocizzare la fattorizzazione, posso stare sicuro. Si tratta del caso della crittogradia asimmetrica.

La terza casistica non ha dietro una dimostrazione matematica ma una prova sperimentale in cui i migliori crittografi ben equipaggiati hanno provato a romperlo ma non ci sono riusciti.

L'ultimo caso parla dello scenario in cui c'è un numero enorme di chiavi di crittografia per cui potrei provarle tutte ma sono talmente tante che ci vorrebbe una quantità di tempo impraticabile. Mettendoci anche un microsecondo ci vuole una quantità di tempo inestimabile. Questa non è neanche una definizione di sicurezza.

Ci sono 4 livelli diversi di sicurezza e ogni algoritmo cerca di coprirne almeno 3. Vedremo anche in quale di questi ogni algoritmo si colloca.

## Cryptography
<span style="color: #00ff7f">È</span>: uno strumento molto utile e le fondamenta per molti meccanismi di sicurezza

<span style="color: #ff7f7f">Non è</span>: la soluzione a tutti i problemi, affidabile se implementata e usata in modo sbagliato e qualcosa da inventare e usare per conto nostro

# Primitive crittografiche

## Cyphers

### Cifrari simmetrici
![733fa3a9585401bd57d6643e5bec8b83.png](:/3890c62355724dccabfe08ce62bd31a1)
Lo scenario di riferimento contiene due interpreti principali (Alice e Bob) che vorranno comunicare tra di loro attraverso una rete di calcolatori. Alice usa il suo laptop per collegarsi al server di Bob. 

L'attaccante cercherà di violare la confidenzialità delle comunicazioni (eavesdropping) e/o alterare l'integrità della comunicazione (tampering). 
- Ad esempio Alice invia la password a Bob e l'attaccante può rubare la password.(eavesdropping)
- Oppure durante una transazione bancaria da Alice a Bob, l'attaccante modifica il destinatario della somma di denaro inviandoli a se stesso.(tampering)

Per lo meno vorremmo che il tampering sia rilevato.

Lo scenario è il medesimo del seguente:
![dc8dd5a2aef7256c296f8b87a2633454.png](:/5d76d30244124102800f329b8219d4b8)

Alice salva un file in un repository e poi lo va a rileggere. Alice parla con se stessa, perchè salvare un file su un disco è come se Alice di oggi parlasse con l'Alice di domani, in quanto il file lo rileggerà nel futuro (domani, o tra un mese). Vogliamo proteggere la modifica del file.
![dcf092908949b44bfcc00c6b0c2dc20f.png](:/1a95dd8b3c3949108887e6822ee130bc)

Alice e Bob dispongono di un algoritmo di crittografia che è detto <span style="color: #007dff">cifrario </span>costituito da una coppia di funzioni o algoritmi:
- La funzione `E` è l'algoritmo di cifratura (encryption). Prende in ingresso una chiave `K` che è un segreto da immaginare come una sequenza di bit (es: 010100010) che tipicamente ad oggi è dell'ordine di 128 bit. Come si genera? Prendo una "moneta", testa ==> 1, croce ==> 0, la lancio 128 volte e segno i 128 valori. Questa funzione usando i parametri di input mi restituisce il crittogramma `c` che è la cifratura del testo in chiaro da cifrare `p`. Questo c verrà inviato sulla rete e noi ipotizzeremo che il nostro avversario sia così bravo da intercettare `c`. Questo è il thread model d'esempio.
- La funzione `D` è l'algoritmo di decifratura (decryption). `c` arriverà a Bob che prende in ingresso anche la stessa chiave K e l'algoritmo D restituirà il messaggio originario inviato da Alice.

Sia Alice che Bob avranno la loro coppia identica di funzioni `D` ed `E` (librerie python o chip elettronici sulla scheda di rete). La chiave `K` è un segreto condiviso tra Alice e Bob e non deve essere pubblico. La sicurezza di questo sistema che protegge la confidenzialità della comunicazione si basa sulla complessità di `K`.

Se chiunque conosce la chiave `K` ovvero la sequenza esatta di 128 bit, prenderebbe `c`, userebbe l'algoritmo `D` che è pubblico, e otterrebbe `p`. 

❓️Come fanno Alice e Bob ad avere un segreto condiviso `K`

Potrebbero incontrarsi  e scambiarselo al bar, ma funziona meno bene questa soluzione se il client e il server si trovano in locazioni geografiche molto distanti. Come lo stabiliscono è un problema e lo vedremo piùa avanti. Alice da casa sua potrebbe lanciare la moneta e definire `K` e la spedisce a Bob ma se la mando in chiaro l'avversario la intercetta e non sarebbe più sicuro. Per mandarla in rete in modo protetto dovrei cifrarla ma per farlo ci vorrebbe un altra chiave `K`<sub>`1`</sub> e il problema si ripeterebbe. Si può interrompere o con metodi OFFLINE (si incontrano al bar o usando un altro mezzo di comunicazione, la lettera postale con dentro il pin che la banca ci invia a casa) oppure ONLINE ovvero raggiungere un segreto condiviso attraverso la rete, ad esempio il TLS mi permette di raggiungere questo obiettivo ma per farlo è necessaria la crittografia a chiave pubblica.

Per ora il nostro assunto è:
✅ Alice e Bob hanno un segreto `K` condiviso
✅ L'attaccante conosce gli algoritmi utilizzati `D` ed  `E`
✅ L'attaccante puà intercettare `c`

![1ca21be2fa8de17837b6d9c7a75ed222.png](:/55bc1ebce8d14388a37b163ac6bfd09b)

Per far si che tutta la sicurezza sia concentrata in `K` e non nel resto è necessario che dato `c` deve essere difficile determinare `p` senza conoscere la chiave `K`. Di tutte le funzioni `D` ed `E` che posso inventarmi devo trovare quelle per cui deve essere molto difficile trovare `p` non conoscendo `k` e avendo solo `c`. Questa proprietà dipende dal fatto che il mio avversario può intercettare qualsiasi messaggio. Se il mio sistema è sicuro deve esserlo per ogni comunicazione. Dati `c` e `p` deve essere inoltre difficile ottenere la chiave `k`:
![8f1241c4a0ff80296716af6b9182696a.png](:/1b90a7a27a624fe3b7d22282b9af20a5)
L'avversario cercherà di violare almeno una di queste 2 proprietà tramite la <span style="color: #ffc86c">crittoanalisi</span>, ovvero l*o studio delle tecniche matematiche per rompere l'algoritmo crittografico ovvero violare queste 2 proprietà*. Le ipotesi sono: l'avversario ha accesso ai dati trasmessi in forma cifrata ovvero intercettare qualsiasi cosa e l'altra è l'ipotesi di Kerckhoff ovvero l'avversario conosce tutti i dettagli degli algoritmi di cifratura in quanto pubblicamente reperibili.

Tenere segreti gli algoritmi `E` e `D` storicamente non ha mai funzionato: la Security trough Obscurity (vedi film ENIGMA). In genere `E` e `D` sono scritti nel firmware delle schede elettroniche, se fossero sconosciute a tutti tranne che al produttore e dovessero essere rotte da un attaccante, il produttore dovrebbe ritirare tutte le schede elettroniche dal mercato, cambiare `E` e `D` e ridarle ai propri clienti. Cosa diversa se le funzioni hanno passato un analisi di criptoanalisi condivisa a livello globale da diverse istituzioni e standardizzata e dunque conosciuta da tutti.

#### 👥Esempi di cifrari simmetrici👥
<span style="color: #000000"><span style="background-color: #ffc8ab">Algoritmo a sostituzione monoalfabetica</span></span>
![137e4379c644c4f71becbe87672f526e.png](:/6383659c24de458f880ec80807c2d784)
Nell'esempio, `P`<sup>`'`</sup>  contiene le lettere raggruppate a gruppi di 5 solo per evitare di mappare le lettere 1:1 e rendere l'attacco più facile.

L'avversario in rete intercetta `C` e vorrebbe ricavare `P`. L'avversario potrebbe iniziare a ragionare sui caratteri ma quello che sicuramente può fare l'avversario è eseguire un' <span style="color: #ff7f7f">attacco esaustivo alle chiavi</span> o anche detto <span style="color: #ff7f7f">attacco a forza bruta o brute-force</span>, fin quando non ottiene un messaggio avente un senso compiuto. Se lui fa un attacco a forza bruta deve provare tutte le possibili permutazioni, con n elementi le permutazioni sono n!.
In questo caso 26! è circa 4 x10<sup>26</sup> e se anche ci mettesse un microsecondo per ogni permutazione ci vorrebbe troppo tempo. Questo significa che è **DIFFICILE**. Visto così questo algoritmo sembrerebbe molto sicuro, perchè ci vuole molto tempo per un attacco a forza bruta. 

Le lettere però non sono tutte equiprobabili nei testi scritti. Nella lingua inglese la lettera che appare più frequentemente è la lettera 'E' 'T' ed 'A'. Se la lettera più frequente nella lingua inglese è la 'E', ma con l'algoritmo di crittografia dell'esempio io la trasformo in 'S', troverò molte 'S' ed è molto probabile che corrisponda alla lettera 'E'.
![06cfc3bf15a5b2f363d689126a3398c2.png](:/d4e99328fc0e4c54acffac4c9a2eed79)
Si può ragionare anche per coppie di lettere (es. TH in inglese è molto probabile).
Sfruttando le statistiche del linguaggio è possibile crittoanalizzare il testo cifrato e trovare la chiave.
