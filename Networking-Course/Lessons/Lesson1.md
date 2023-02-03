## Introduzione
- Docente: Carlo Vallati, Francesca Righetti
- Mail: carlo.vallati@unipi.it, francesca.righetti@ing.unipi.it
- Lezioni: 16h
- Esercitazioni e laboratorio: 8h
- Esame consiste in un progetto consistente in una applicazione di rete in python
* * *

# Computer networks
L'obietivo di questa prima lezione è avere una introduzione ai concetti delle reti informatiche. L'approccio usato è quello di usare le architetture di Internet come esempio. Le reti di calcolatori possono anche essere reti isolate, i principi di funzionamento sono i medesimi ma in modo isolato e su piccola scala. 


Le network edge sono le reti sulle quali troviamo i dispositivi periferici (client, servers).

Una rete Internet è una rete di comunicazione globale che si espande su scala mondiale alla quale sono connessi milioni di dispotivi di calcolo ovvero una miriade di dispositivi eterogenei. Dallo smartphone, all'automobile, al dispositivo IoT, fino anche ai server molto prestazionali che solitamente sono confinati in data center lontani dagli utenti sui quali vengono messe in esecuzione le applicazioni e i servizi. Questi sono gli <span style="color: #ff7f7f">end-systems o hosts</span>. Essi si connettono alla rete internet per scambiarsi dati tra di loro.

❓️ Come si realizza questa capacità di mettere in comunicazione dispositivi eterogenei tra di loro?
Attraverso un infrastruttura distribuita sul globo terrestre e non composta da una serie di <span style="color: #ff7f7f">link di comunicazione</span> (fibra, rame, wireless...) che mettono in collegamento le parti su lunghe distanze e dispositivi particolari chiamati <span style="color: #ff7f7f">routers</span>.  Sono le access networks.

Il router è un dispositivo che smista il traffico da una sorgente a una destinazione. 

![c6ad2be4dd4bcf701e012d43a9ee168e.png](:/6e3581ff1af946ed89a54e526d88d666)

Sono le reti usate dagli operatori telefonici usate per connettere le reti periferiche tra di loro e permettere di smistare il traffico da una rete periferica ad un altra.
Da un altra parte abbiamo il cuore della rete internet (Global ISP, Regional ISP ...). Non è una rete omogenea unica ma un rete di reti. Non si tratta di una rete amministrata da un unica compagnia ma è una composizione di reti differenti anche estrememamente eterogenee tra di loro amministrate da persone differenti le quali sono in qualche modo interconnesse per realizzare la comunicazione tra dispositivi periferici <span style="color: #007dff">end-to-end</span>. I router e i link possono essere categorizzati in modo gerarchico in sottoreti ciascuna delle quali è amministrata in modo autonomo.

I protocolli di comunicazione standardizzati permettono di avere una rete mondiale con dispositivi eterogenei. Sono stati standardizzati da comitati internazionali (es: IETF, IEEE).

Il risultato è una rete che alla fine fornisce un servizio banale, ovvero quello di offrire ai dispositivi periferici una infrastruttura di comunicazione, ovvero semplicemente riceve i dati dai dispositivi periferici e li trasporta da qualche altra parte.

La rete fornisce la comunicazione al meglio delle capacità senza nessuna garanzia *"best-effort"* un applicazione ovvero chiede alla rete Internet di trasportare il dato ma essa proverà a farlo al suo meglio, alcune volte ce la fa altre no. Per permettere la realizzazione di applicazioni affidabili ci sono protocolli che cercano di ovviare al limite della rete internet e della sua inaffidabilità.

Un protocollo permette di stabilire delle regole condivisi tra tutti i dispositivi della rete internet su come essi devono comunicare. Un protocollo è un documento o una serie di regole che definisce come due entità devono interagire tra di loro. Un protocollo di rete definisce il formato e l'ordine dei messaggi che devono essere scambiati.

![f4e404ba0ca19e619ab406cfda93f32a.png](:/2986277773e748f0b6842076c7db6565)

# Network edge

Sono le reti contenenti gli hosts.
![652bedac38e57d97033bd2255bdede59.png](:/ea08f3ad6cac45ba9d66db69f89a932d)
Sono le reti che ospitano le applicazioni. Solitamente queste applicazioni permettono di implementare delle funzionalità fornite agli utenti, mostrare un sito web, ricevere/inviare la posta, la voce, etc... e sono solitamente implementate usando due principali paradigmi: Client-Server (Web-Browser e Web-Server) e Peer-to-Peer (Skype, BitTorrent). L'obiettivo della rete edge è quello di connettere i dispositivi edge. Questi dispositivi devono essere connessi al resto della rete internet tramite una tecnologia di comunicazione. Come si connettono questi dispositivi? Come scambiano dati con l'edge router? Che si tratta di un router sulla rete di frontiera che gestisce la comunicazione con la rete Internet. Esistono diverse tecnologie di comunicazione e ciascune di queste è caratterizzata da una diversa banda, accessibilità rispetto a una determinata area, tipo di mezzo fisico, come si propaga il segnale ciascuna delle quali le rendono adatte per determinati settori di mercato. Tecnologie di comunicazione residenziale, per grandi aziende o mobile:
![25a8e4aea3d51e255f7cd340bb638e26.png](:/2ad86453dbe24eaabaafa27419128264)
![03eac249a9bd8a062035fc6846cf530d.png](:/e97eb8c08eb7473fa2d6781baecd137c)
![56547ae3d5daa9eb237ed7d9a7655f86.png](:/b1358a92de774a8584f69578cf9baf5d)
![6d74485254b5f71b0683c5cc6bfe9b5d.png](:/41189ac0058e43698165f6597ad92a56)


Esistono diverse strutture di reti di accesso che dipendono dalla tecnologia usata.


![24cefc1adb35c7018df0fe7faab942d1.png](:/fdf467b7ec5c4e3883d76a45e4d5b778)

Un evoluzione della tecnologia ADSL è la VDSL chiamata da alcuni operatori FTTC (Fiber to the cabinet).
L'ADSL sfrutta la rete telefonica ovvero il doppino telefonico che è presente in ciascuna delle nostre case. L'operatore installa un router che viene connesso al doppino telefonico. Il doppino telefonico viene usato per trasmettere i dati da casa nostra fino alle centrale. Quest'ultima è un luogo in cui finiranno tutte le terminazioni di tutti i doppini telefonici delle nostre case. In questa centrale c'è un apparato che permette di connettere e trasmettere tutti i dati verso la rete internet. In questo modo si sfrutta la lunghezza del doppino telefonico per una distanza di massima di 10km. Gli operatori telefonici hanno installato dei microaggregatori (uno per via o per quartiere) dei doppini telefonici al fine di ridurre la distanza tra i router di casa e il punto di raccolta questo perchè il doppino telefonico è soggetto a molte interferenze. Questi punti di aggregazione vengono connessi alla centrale con delle fibre ottiche così da aumentare il rate di trasmissione ➡️ VDSL.

![9c778b9a07fad94d4294556a65aa442a.png](:/1bb22db375804961b8853164b7e71b6a)
Nel fiber to home c'è il router collegato a un terminatore di fibra ottica ma altri operatori installano un terminatore esterno. La fibra ottica va in un punto di aggregazione dell'operatore che può essere locale o centrale, dipende dalla struttura della rete. Grazie alle prestazioni della fibra, può essere vicino o lontano, perchè la fibra è isolata dalle interferenze quindi non impatta la comunicazione. Di fibra ottica ci sono state diverse tecnologie e architetture. Quelle uscite prima vogliono che le fibre finiscano direttamente nei centri di aggregrazione centrale, quelle moderne hanno degli aggregatori distribuiti sul territorio. La fibra di OpenFiber che usa le PON, sfruttano degli aggregatori distribuiti. Le PON sono fibre che sono una collezione di spezzoni di fibra che vengono collegate tra di loro. La casettina fuori casa della fibra non è alimentata. Quella attiva (PAN) presuppone un cavo di fibra che va direttamente al centro. Tutti i centri di aggregazione sono collegati tra di loro che poi vanno verso il centro di aggregazione.

# Internet protocol stack
