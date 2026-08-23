from pathlib import Path
import subprocess

ROOT = Path(__file__).parent / "lezioni"

HEADER = r'''.po 0.7i
.nr PS 10
.nr VS 12
.de T
.sp 1
.ce 2
.ft B
.ps 18
\$1
\$2
.ps 10
.ft R
..
.de H
.sp 0.8
.ft B
.ps 14
\$1
.ps 10
.ft R
.sp 0.3
..
.de P
.sp 0.45
.ti 0
..
.de I
.sp 0.25
.ti 0.2i
\$*
..
'''

lessons = [
    ("PL8", "Cammini minimi e algoritmo di Dijkstra", "Grafi pesati, cammini minimi da sorgente singola, rilassamento e scelta greedy. Dijkstra richiede pesi non negativi.", ["Rilassamento: se d[v] > d[u]+peso(u,v), aggiorna d[v] e padre[v].", "Dijkstra con scansione lineare: O(n^2+m), quindi O(n^2).", "Dijkstra con heap: O((n+m) log n).", "La correttezza usa l'induzione sui vertici resi definitivi: il primo arco del cammino ottimo che attraversa il confine ha gia distanza corretta."], ["Applica Dijkstra mostrando ogni estrazione e rilassamento.", "Ricostruisci il cammino minimo con il vettore dei padri.", "Costruisci un controesempio che mostra perche un peso negativo rende Dijkstra non affidabile.", "Risolvi il problema dei contenitori/versamenti modellandolo come grafo degli stati.", "Progetta un algoritmo per cammini minimi evitando nodi pericolosi."]),
    ("PL9", "Alberi di copertura minimi e Kruskal", "Un MST collega tutti i nodi con costo totale minimo. La lezione sviluppa Kruskal e Union-Find.", ["Kruskal ordina gli archi per peso e aggiunge un arco solo se collega due componenti diverse.", "Union-Find: MakeSet, Find e Union; unione per dimensione/rango.", "La prova per scambio usa il ciclo creato dall'arco greedy e la proprieta del taglio.", "Complessita: ordinamento O(m log m); con Union-Find il costo complessivo e O(m log n) oltre all'ordinamento."], ["Calcola un MST a mano su un grafo pesato.", "Implementa Union-Find con path compression e union-by-size.", "Implementa Kruskal e gestisci pesi uguali.", "Dimostra la correttezza di Kruskal con un argomento di scambio.", "Modella una rete idrica aggiungendo un nodo pozzo artificiale."]),
    ("PL10", "Tecnica greedy", "Un algoritmo greedy compie a ogni passo una scelta locale. La scelta e corretta solo se si dimostrano scelta sicura e sottostruttura ottima.", ["Selezione di attivita: ordina per tempo di fine e scegli la prima compatibile.", "Correttezza tramite scambio della prima attivita di una soluzione ottima.", "Assegnamento di attivita alle aule: ordina per inizio e usa scansione o min-heap.", "Selezione attivita O(n log n); assegnamento semplice O(n^2), con heap O(n log n)."], ["Trova il massimo insieme di intervalli compatibili.", "Costruisci un controesempio a una scelta per durata minima o inizio minimo.", "Assegna intervalli al minimo numero di aule e dimostra il risultato.", "Risolvi un problema di rifornimenti con il minor numero di soste.", "Per ogni strategia indica se e ottima, euristica o falsa e giustifica."]),
    ("PL11", "Algoritmi di approssimazione: Vertex Cover", "Gli algoritmi di approssimazione producono soluzioni ammissibili con una garanzia rispetto all'ottimo; le euristiche non garantiscono un rapporto.", ["Per minimizzazione, A <= rho OPT; rho=1 equivale a una soluzione ottima.", "Vertex Cover: ogni arco deve avere almeno un estremo nella copertura.", "La greedy basata sul grado puo avere rapporto non limitato.", "L'algoritmo che sceglie un arco non coperto e inserisce entrambi gli estremi ha rapporto 2 e costo O(n+m).", "Prova: gli archi scelti sono disgiunti, quindi OPT >= k; la soluzione usa 2k nodi."], ["Calcola una copertura su un grafo assegnato.", "Costruisci un controesempio alla greedy basata sul grado.", "Dimostra formalmente il rapporto 2.", "Confronta euristica e approssimazione sulla stessa istanza.", "Scrivi uno pseudocodice che restituisca anche gli archi scelti."]),
    ("PL12", "Tre algoritmi di approssimazione", "Le slide presentano scheduling su macchine identiche, MAX-CUT e Bin Packing con Next Fit.", ["List scheduling assegna ogni lavoro alla macchina meno carica: con scansione O(nm), con heap O(n log m).", "LPT ordina i lavori in ordine decrescente e migliora il bound fino a 4/3.", "Greedy MAX-CUT assegna ogni vertice al lato che massimizza gli archi tagliati; costo O(n+m), rapporto 2 rispetto al massimo non tagliato.", "Next Fit apre un nuovo contenitore quando il prossimo oggetto non entra; tempo O(n), rapporto minore di 2."], ["Applica list scheduling e LPT a una sequenza di lavori.", "Dimostra il bound del makespan usando carico totale e ultimo lavoro.", "Esegui greedy MAX-CUT su un grafo e calcola il taglio.", "Applica Next Fit a oggetti con capacita fissata.", "Individua dove una prova di rapporto usa un lower bound sull'ottimo."]),
    ("PL13", "Divide et impera: selezione", "Lo schema divide et impera divide il problema, risolve ricorsivamente e combina. La selezione cerca il k-esimo elemento.", ["Quickselect sceglie un pivot, partiziona e ricorre solo nella parte che contiene k.", "Quickselect ha O(n^2) nel caso peggiore e O(n) atteso con pivot casuale.", "Mediana delle mediane usa gruppi di cinque e garantisce O(n) nel caso peggiore.", "La ricorrenza tipica e T(n) <= T(n/5)+T(7n/10)+O(n)."], ["Risolvi ricorrenze con il teorema principale o con un albero di ricorsione.", "Implementa Quickselect e conta le operazioni di partizionamento.", "Spiega perche i gruppi di cinque garantiscono un pivot bilanciato.", "Progetta la ricerca di un punto fisso.", "Risolvi massimo in un array ruotato e primo zero di una funzione monotona."]),
    ("PL14", "Divide et impera: punti vicini e inversioni", "La lezione tratta closest pair in una e due dimensioni e conteggio delle inversioni.", ["Closest pair esaustivo costa Theta(n^2).", "La versione divide et impera ordina per x, risolve le due meta e controlla la striscia centrale in O(n), per un totale Theta(n log n).", "Nella striscia basta confrontare ogni punto con un numero costante di successivi per il principio dei cassetti.", "Le inversioni si contano con merge-and-count in O(n log n), invece dell'esaustivo O(n^2)."], ["Calcola la coppia piu vicina in una dimensione.", "Disegna la striscia centrale e giustifica il numero costante di confronti.", "Implementa merge sort che conta le inversioni.", "Confronta ricerca binaria delle inversioni e merge-and-count.", "Analizza il caso di coordinate duplicate e definisci un tie-break."]),
    ("PL15", "Programmazione dinamica: metodo e tabelle", "La DP sfrutta sottoproblemi sovrapposti e sottostruttura ottima. Le slide presentano memoizzazione top-down, tabulazione bottom-up e vari problemi su sequenze.", ["Fibonacci: dalla ricorsione esponenziale a Theta(n), con spazio O(1) nella versione iterativa.", "Stringhe senza 00: stato basato sull'ultimo simbolo, tempo Theta(n).", "Somma massima non consecutiva: includi o escludi l'elemento corrente.", "Massimo sottovettore: migliore soluzione che termina in i oppure soluzione globale.", "LIS: dp[i] e la lunghezza della LIS che termina in i; O(n^2)."], ["Scrivi Fibonacci top-down e bottom-up.", "Conta stringhe binarie senza due zeri consecutivi.", "Risolvi somma massima di elementi non consecutivi.", "Calcola il massimo sottosegmento e ricostruiscilo.", "Calcola LIS in O(n^2) e ricostruisci una sottosequenza."]),
    ("PL16", "Programmazione dinamica con tabelle bidimensionali", "Le tabelle bidimensionali descrivono prefissi o celle. Sono trattati cammini in matrici, zaino 0/1 e LCS.", ["Cammino massimo: dp[i][j] dipende da sopra e sinistra; tempo O(n^2).", "Zaino 0/1: dp[i][c] sceglie se includere l'oggetto i; tempo O(nC), spazio riducibile a O(C).", "LCS: se gli ultimi caratteri coincidono si usa la diagonale; altrimenti il massimo tra sopra e sinistra; tempo O(nm).", "La soluzione si ricostruisce risalendo dalla cella finale."], ["Trova il massimo costo in una matrice e ricostruisci il cammino.", "Risolvi zaino e ricostruisci gli oggetti.", "Calcola LCS e ricostruisci una sottosequenza.", "Conta cammini in una griglia con ostacoli.", "Progetta minimo numero di monete e cambio possibile."]),
    ("PL17", "DP e cammini minimi: Bellman-Ford e Floyd-Warshall", "Bellman-Ford e una DP sul numero massimo di archi; Floyd-Warshall e una DP sui vertici ammessi come intermedi.", ["Bellman-Ford rilassa tutti gli archi n-1 volte: O(nm), spazio O(n) o O(n^2).", "Un ulteriore miglioramento dopo n-1 passate segnala un ciclo negativo raggiungibile.", "Floyd-Warshall usa dp[k][i][j] e decide se usare il nuovo intermedio k: O(n^3), spazio O(n^2) ottimizzato.", "I cammini minimi senza cicli negativi possono essere scelti semplici e hanno al piu n-1 archi."], ["Applica Bellman-Ford mostrando ogni passata.", "Rileva un ciclo negativo e distingui i nodi raggiungibili.", "Compila la tabella Floyd-Warshall.", "Ricostruisci un cammino minimo con i predecessori.", "Confronta Dijkstra, Bellman-Ford e Floyd-Warshall su tre grafi."]),
    ("PL18", "Backtracking: enumerazione e potatura", "Il backtracking esplora configurazioni parziali, aggiunge una scelta, verifica vincoli, ricorre e annulla. La potatura elimina solo rami sicuramente inutili.", ["Stringhe binarie: costo di stampa O(n 2^n).", "Matrici binarie: enumerazione O(n^2 2^(n^2)); vincoli possono ridurre i nodi visitati.", "Permutazioni: O(n n!); con vincoli si misura O(n S(n)).", "Una potatura perfetta visita essenzialmente gli antenati delle soluzioni valide."], ["Genera stringhe binarie e stringhe con numero fissato di uni.", "Genera matrici con righe o colonne ordinate.", "Genera permutazioni con esattamente k punti fissi.", "Progetta n-regine con controlli di colonna e diagonali.", "Per ogni potatura dimostra che la condizione e necessaria."]),
    ("PL19", "Backtracking: vincoli avanzati", "Le slide studiano stringhe ternarie con conteggi ordinati, matrici con numero crescente di uni e permutazioni senza sottosequenza crescente di lunghezza 3.", ["Per stringhe con a>b>c si calcola il minimo necessario per rendere completabile il prefisso.", "Per matrici si pota usando il massimo numero di uni ottenibile dalle righe restanti.", "Per evitare LIS di lunghezza 3 si mantiene una struttura minimi e si controlla se una scelta chiude la sottosequenza.", "La complessita e espressa rispetto al numero S(n) di soluzioni o N_v di nodi visitati."], ["Genera stringhe ternarie con #a>#b>#c.", "Genera matrici con numero di uni strettamente crescente per riga.", "Genera permutazioni senza LIS di lunghezza 3.", "Scrivi la potatura e dimostra che non elimina soluzioni valide.", "Confronta enumerazione con verifica finale e backtracking potato."]),
    ("PL20", "Backtracking: problemi decisionali e ottimizzazione", "Il backtracking viene applicato a ciclo Hamiltoniano, 3-colorazione, zaino e commesso viaggiatore.", ["Hamiltoniano: estendi un cammino controllando adiacenza e ritorno al nodo iniziale; caso pessimo O(n!).", "3-colorazione: assegna colori e pota i conflitti; caso pessimo O(n 3^n).", "Zaino: pota per capacita e per un upper bound sul valore; caso pessimo O(2^n).", "TSP: costruisce tour e usa un bound inferiore; il costo e esponenziale."], ["Decidi se un grafo ha un ciclo Hamiltoniano.", "Implementa 3-colorazione.", "Risolvere zaino con bound ottimistico.", "Progetta TSP e verifica che il bound non includa la diagonale di costo zero.", "Risolvi uno tra subset sum, Sudoku, cricca massima e problema dei francobolli."]),
]

explanations = {
    "PL8": ("Il problema e trovare il costo minimo per andare da una sorgente a tutti gli altri nodi. "
             "L'idea di Dijkstra e rendere definitiva, a ogni passo, la distanza piu piccola ancora provvisoria. "
             "Questa scelta e sicura solo con pesi non negativi: un cammino futuro non puo tornare indietro e migliorare "
             "un valore gia fissato. Per ogni arco si prova quindi se passare da u migliora il costo di v; questa operazione "
             "si chiama rilassamento. Il vettore padre serve solo a ricostruire il cammino, non a calcolarne il costo."),
    "PL9": ("Un MST non cerca il cammino piu breve tra ogni coppia: cerca invece un insieme di archi che colleghi tutti i nodi "
             "con somma dei pesi minima e senza cicli. Kruskal parte dagli archi piu economici e li accetta finche collegano "
             "componenti diverse. Union-Find mantiene proprio questa informazione. La proprieta del taglio spiega perche "
             "l'arco piu leggero che attraversa un taglio e una scelta sicura."),
    "PL10": ("Greedy significa decidere subito senza tornare indietro. Questo non rende automaticamente corretto l'algoritmo: "
             "bisogna dimostrare che la prima scelta puo essere sostituita a una scelta di una soluzione ottima senza peggiorarla. "
             "Nella selezione di attivita la scelta corretta e l'intervallo che finisce prima, perche lascia piu spazio alle attivita "
             "successive. Nell'assegnamento alle aule si usa invece la prima attivita che inizia e si riutilizza l'aula che si libera prima."),
    "PL11": ("Quando trovare l'ottimo e difficile, si puo accettare una soluzione non ottima ma con una garanzia. La garanzia "
             "confronta il valore prodotto con OPT. Per Vertex Cover, scegliendo un arco ancora non coperto e prendendo entrambi "
             "gli estremi si costruisce una copertura. Gli archi scelti sono disgiunti: ogni soluzione ottima deve prendere almeno "
             "un estremo per ciascuno, mentre l'algoritmo ne prende due. Da qui nasce il fattore 2."),
    "PL12": ("Le tre tecniche usano un limite inferiore sull'ottimo per misurare quanto e lontana la soluzione. Nello scheduling "
             "si distribuiscono i lavori sulla macchina meno carica; LPT migliora il risultato ordinando prima i lavori dal piu lungo "
             "al piu corto. In MAX-CUT ogni vertice viene assegnato al lato che aumenta il taglio. In Next Fit si riempie il contenitore "
             "corrente e se il prossimo oggetto non entra se ne apre uno nuovo. La prova non dimostra che la scelta locale e ottima, "
             "ma che il suo errore non supera un fattore stabilito."),
    "PL13": ("Divide et impera funziona quando un problema grande puo essere ridotto a un sottoproblema piu piccolo. Quickselect "
             "partiziona l'array rispetto a un pivot: dopo la partizione sappiamo in quale parte si trova il k-esimo elemento e scartiamo "
             "l'altra. A differenza di QuickSort, non risolviamo entrambe le parti. Un pivot cattivo produce O(n^2); la mediana delle "
             "mediane costruisce invece un pivot abbastanza equilibrato da garantire O(n) nel caso peggiore."),
    "PL14": ("Per la coppia di punti piu vicini, controllare tutte le coppie e semplice ma costa quadratico. Divide et impera separa "
             "i punti per coordinata x, risolve i due lati e controlla solo la striscia vicino alla linea centrale. La geometria dimostra "
             "che nella striscia ogni punto puo essere confrontato con un numero costante di punti. Per le inversioni, durante il merge "
             "quando si prende un elemento dalla meta destra si contano in un colpo solo tutti gli elementi rimasti nella meta sinistra."),
    "PL15": ("La domanda da porsi nella programmazione dinamica e quale informazione minima descriva un sottoproblema. Fibonacci "
             "ripete gli stessi valori, quindi li memorizziamo. Negli altri problemi il valore di dp[i] descrive una soluzione che termina "
             "in i oppure usa i primi i elementi. La ricorrenza divide le possibilita in casi disgiunti, i casi base fermano la tabella e "
             "l'ordine bottom-up rispetta le dipendenze. La ricostruzione richiede di conservare anche la scelta fatta."),
    "PL16": ("Una tabella bidimensionale si usa quando la soluzione dipende da due indici: una cella della matrice, un prefisso di due "
             "stringhe oppure un oggetto e una capacita. Per il cammino, l'ultimo passo arriva da sopra o da sinistra. Per lo zaino, "
             "l'oggetto o viene preso o viene lasciato. Per LCS, se i caratteri finali coincidono si prende la diagonale; altrimenti si "
             "conserva il migliore tra eliminare un carattere dalla prima o dalla seconda stringa. La tabella calcola il valore, i parent "
             "o la direzione permettono di ricostruire la soluzione."),
    "PL17": ("Bellman-Ford e Floyd-Warshall risolvono cammini minimi usando DP e quindi accettano pesi negativi. Bellman-Ford ragiona "
             "sul numero massimo di archi: dopo n-1 passate sono state considerate tutte le soluzioni semplici. Una passata ulteriore "
             "che migliora indica un ciclo negativo raggiungibile. Floyd-Warshall ragiona invece sui vertici che possono essere usati come "
             "intermedi: per ogni coppia sceglie se usare o non usare il nuovo vertice k."),
    "PL18": ("Il backtracking costruisce una soluzione un simbolo, una riga o una scelta alla volta. Dopo ogni scelta controlla un vincolo; "
             "se il prefisso non puo piu essere completato, interrompe subito quel ramo. Quando arriva a una configurazione completa la "
             "stampa o la valuta. La complessita va espressa rispetto alle soluzioni stampate quando il problema e di enumerazione: il costo "
             "inevitabile di scrivere ogni soluzione non puo essere ignorato."),
    "PL19": ("Qui la potatura non controlla soltanto se il prefisso e gia invalido: calcola se esiste ancora abbastanza spazio per completarlo. "
             "Per le stringhe ternarie si contano i simboli minimi necessari per ottenere #a>#b>#c. Per le matrici si usa il massimo numero "
             "di uni aggiungibile nelle righe rimanenti. Per le permutazioni si mantiene informazione sulle sequenze crescenti di lunghezza "
             "due, cosi si riconosce subito quando una nuova scelta creerebbe una LIS di lunghezza tre."),
    "PL20": ("I problemi decisionali chiedono se esiste una soluzione, mentre quelli di ottimizzazione chiedono la migliore. Il backtracking "
             "esplora le configurazioni e torna indietro quando una scelta viola un vincolo. Nel ciclo Hamiltoniano il prefisso deve restare "
             "un cammino semplice e alla fine deve chiudersi. Nella colorazione si vietano colori uguali su estremi adiacenti. Nello zaino e "
             "nel TSP si aggiunge anche un bound: se nemmeno la stima piu ottimistica puo battere la soluzione corrente, il ramo si pota."),
}

pitfalls = {
    "PL8": "Non usare Dijkstra con pesi negativi e non confondere distanza minima con numero di archi.",
    "PL9": "Un MST non e un albero dei cammini minimi; con pesi uguali possono esistere piu MST corretti.",
    "PL10": "Una scelta intuitiva non e una prova: cerca sempre scambio e sottostruttura ottima.",
    "PL11": "Un'euristica senza rapporto non e un algoritmo di approssimazione.",
    "PL12": "Per un rapporto serve un bound rispetto a OPT, non solo un esempio favorevole.",
    "PL13": "Quickselect ricorre su una sola parte; usare QuickSort cambiando entrambe le ricorsioni altera il costo.",
    "PL14": "Nel merge delle inversioni non contare una inversione alla volta: conta il blocco rimanente.",
    "PL15": "Non definire dp prima di aver chiarito se descrive un prefisso, un suffisso o una soluzione che termina in i.",
    "PL16": "La tabella calcola il valore; per ricostruire una soluzione servono confronti o direzioni durante il ritorno.",
    "PL17": "Un ciclo negativo rende la distanza non definita solo per i nodi che possono raggiungerlo e da cui si puo uscire.",
    "PL18": "Una potatura e lecita solo se la condizione esclusa e necessaria per ogni completamento valido.",
    "PL19": "Non confondere il numero di nodi visitati con il numero di soluzioni: la potatura puo cambiare molto il primo.",
    "PL20": "Un bound ottimistico deve essere davvero ottimistico; nel TSP non includere la diagonale di costo zero.",
}

def render(code, title, summary, key_points, exercises, source):
    lines = [HEADER, f".T\n{code}\n{title}", ".P", "Materiale ricostruito dalle slide ufficiali del corso.", ".H\nChe problema stiamo risolvendo?", summary, ".H\nSpiegazione intuitiva", explanations[code], ".H\nCosa devi sapere"]
    for item in key_points:
        lines += [f".P\n- {item}"]
    lines += [".H\nEsercizi"]
    for i, item in enumerate(exercises, 1):
        lines += [f".P\n{i}. {item}"]
    lines += [".H\nErrore tipico da evitare", pitfalls[code], ".H\nMetodo di svolgimento", "Per ogni esercizio scrivi idea, pseudocodice, correttezza, complessita temporale, complessita spaziale, codice Python e test limite.", ".H\nFonte", source]
    return "\n".join(lines) + "\n"

for code, title, summary, key_points, exercises in lessons:
    source = f"{code}.pdf: contenuto verificato sulle slide ufficiali collegate nella pagina del corso."
    slug = code.lower()
    ms = Path(f"/tmp/{slug}_lezione.ms")
    ps = Path(f"/tmp/{slug}_lezione.ps")
    pdf = ROOT / f"{code}_{title.lower().replace(' ', '_').replace(':', '').replace(',', '').replace('è', 'e').replace('à', 'a')}.pdf"
    ms.write_text(render(code, title, summary, key_points, exercises, source), encoding="utf-8")
    with ps.open("wb") as output:
        subprocess.run(["groff", "-Kutf8", "-Tps", str(ms)], stdout=output, check=True)
    subprocess.run(["ps2pdf", str(ps), str(pdf)], check=True)
    ms.unlink()
    ps.unlink()
