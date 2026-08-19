from pathlib import Path
import subprocess

ROOT = Path(__file__).parent / "percorso_giornaliero"

MACROS = r'''.po 0.7i
.nr PS 10
.nr VS 12
.nr PD 7
.de TL
.sp 1
.ce 2
.ft B
.ps 20
\$1
\$2
.ps 10
.ft R
..
.de PP
.sp 0.5
.ti 0
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
.de B
.ft B
..
.de E
.ft R
..
'''

sessions = [
    ("01_grafi", "19 agosto 2026", "Rappresentazione dei grafi e analisi", "liste di adiacenza, matrici, n e m, O(n+m)",
     ["Costruisci una lista di adiacenza a partire da 8 archi e 6 nodi.", "Scrivi una funzione che conta gli archi senza doppio conteggio.", "Classifica la complessita di 5 frammenti con cicli annidati.", "Spiega quando usare lista e quando matrice di adiacenza."],
     "Implementa la costruzione del grafo e testa n=0, n=1 e un grafo sconnesso.", "Sai scegliere la rappresentazione e motivare spazio e tempo?"),
    ("01_grafi", "20 agosto 2026", "DFS: visita in profondita", "marcatura, ricorsione, padre, tempi di ingresso e uscita", ["Esegui DFS su un grafo di 7 nodi indicando ordine e tempi.", "Implementa DFS ricorsiva e iterativa.", "Calcola i nodi raggiungibili da una sorgente.", "Dimostra l'invariante: ogni nodo visitato e raggiunto tramite un cammino DFS."], "Scrivi codice Python per DFS e conta le componenti connesse.", "Sai spiegare perche DFS visita ogni arco al piu una volta?"),
    ("01_grafi", "21 agosto 2026", "DFS: cicli, alberi e componenti", "cicli non orientati, connessione, alberi, foresta DFS", ["Verifica se un grafo e connesso.", "Verifica se un grafo e un albero.", "Trova un ciclo in un grafo non orientato ignorando il padre.", "Dimostra che connettivita e n-1 archi caratterizzano un albero."], "Implementa is_tree(grafo) in O(n+m) e prepara 4 test limite.", "Sai distinguere un ciclo nella struttura dai back-edge della DFS?"),
    ("01_grafi", "22 agosto 2026", "DFS avanzata: ponti e articolazioni", "tin, low, ponti e punti di articolazione", ["Calcola tin e low su un grafo dato.", "Trova tutti i ponti con low[v] > tin[u].", "Trova i punti di articolazione considerando separatamente la radice.", "Scrivi una dimostrazione della condizione per i ponti."], "Implementa ponti e articolazioni con una sola DFS.", "Sai spiegare ogni aggiornamento di low?"),
    ("01_grafi", "23 agosto 2026", "BFS, distanze e DAG", "BFS, cammini minimi non pesati, ordinamento topologico", ["Esegui BFS e compila distanza e padre.", "Ricostruisci un cammino minimo tra due nodi.", "Trova i nodi equidistanti da due sorgenti.", "Produci un ordinamento topologico con Kahn e verifica un ciclo."], "Implementa BFS, ricostruzione cammino e Kahn.", "Sai dimostrare che la prima distanza assegnata da BFS e minima?"),
    ("02_cammini_mst", "24 agosto 2026", "Dijkstra", "rilassamento, heap, cammini minimi con pesi non negativi", ["Applica Dijkstra a un grafo pesato di 6 nodi mostrando ogni rilassamento.", "Ricostruisci il cammino minimo con i predecessori.", "Trova la distanza minima tra due insiemi di nodi.", "Costruisci un controesempio con un peso negativo."], "Implementa Dijkstra con heapq e testa nodi irraggiungibili.", "Sai dire esattamente quale ipotesi rende corretto Dijkstra?"),
    ("02_cammini_mst", "25 agosto 2026", "Bellman-Ford e Floyd-Warshall", "pesi negativi, cicli negativi, cammini tra tutte le coppie", ["Esegui Bellman-Ford per n-1 passate.", "Rileva un ciclo negativo raggiungibile.", "Compila una tabella Floyd-Warshall per un grafo di 4 nodi.", "Confronta Dijkstra, Bellman-Ford e Floyd-Warshall."], "Implementa almeno Bellman-Ford; scrivi la ricorrenza di Floyd-Warshall.", "Sai scegliere l'algoritmo in base a segni dei pesi e numero di sorgenti?"),
    ("02_cammini_mst", "26 agosto 2026", "Kruskal e Union-Find", "alberi ricoprenti minimi, ordinamento archi, proprieta del taglio", ["Calcola un MST a mano ordinando gli archi.", "Implementa MakeSet, Find e Union.", "Implementa Kruskal.", "Dimostra che Kruskal non crea cicli e che la scelta e sicura."], "Testa grafi sconnessi e grafi con pesi uguali.", "Sai distinguere ciclo del grafo e ciclo nell'insieme scelto?"),
    ("02_cammini_mst", "27 agosto 2026", "Prim e confronto degli MST", "frontiera, chiave minima, Prim con heap", ["Applica Prim partendo da tre sorgenti diverse.", "Confronta Prim e Kruskal su grafo sparso e denso.", "Dimostra la proprieta del taglio usata da Prim.", "Spiega perche un MST non e un albero dei cammini minimi."], "Scrivi Prim con heap e misura la complessita in funzione di n,m.", "Sai spiegare cosa cambia se il grafo non e connesso?"),
    ("02_cammini_mst", "28 agosto 2026", "Greedy e approssimazione", "scelta sicura, sottostruttura ottima, rapporto di approssimazione", ["Trova una strategia greedy per selezione di intervalli.", "Costruisci un controesempio a una strategia greedy sbagliata.", "Applica Vertex Cover basato su matching.", "Dimostra il fattore 2 dell'approssimazione."], "Scrivi una dimostrazione completa: soluzione prodotta <= 2 OPT.", "Sai distinguere euristica da algoritmo con garanzia?"),
    ("02_cammini_mst", "29 agosto 2026", "Ripasso integrato dei grafi", "DFS, BFS, DAG, SCC, cammini minimi, MST", ["Risolvi un esercizio su SCC con Kosaraju.", "Costruisci il grafo condensato.", "Trova sorgenti minime che raggiungono tutti i nodi in un DAG.", "Svolgi una prova mista: BFS, Dijkstra e Kruskal."], "Rifai a memoria gli algoritmi e scrivi una tabella delle complessita.", "Sai scegliere l'algoritmo corretto leggendo solo la traccia?"),
    ("03_divide_et_impera", "30 agosto 2026", "Divide et impera", "ricorrenze, ricerca binaria, selezione, sottosegmento, punti vicini", ["Risolvi 5 ricorrenze con il teorema principale.", "Implementa ricerca binaria e primo valore negativo.", "Risolvi il massimo sottosegmento per divide et impera.", "Scrivi idea e ricorrenza della coppia di punti piu vicini."], "Per un esercizio scrivi divisione, combinazione, correttezza e T(n).", "Sai giustificare il costo della combinazione?"),
    ("04_programmazione_dinamica", "31 agosto 2026", "DP: metodo e ricorrenze", "stato, casi base, transizione, top-down e bottom-up", ["Implementa Fibonacci nei due approcci.", "Risolvi la piastrellatura 2 x n.", "Definisci gli stati per stringhe ternarie senza pattern vietati.", "Riduci lo spazio di una DP lineare a O(1) quando possibile."], "Scrivi sempre stato, base, transizione e ordine prima del codice.", "Sai riconoscere sottoproblemi sovrapposti?"),
    ("04_programmazione_dinamica", "1 settembre 2026", "DP su matrici", "cammini massimi, esistenza e conteggio cammini", ["Calcola il massimo costo da alto-sinistra a basso-destra.", "Ricostruisci il cammino massimo.", "Determina se esiste un cammino su celle zero.", "Conta i cammini in una matrice senza ostacoli."], "Implementa una soluzione O(n^2) e gestisci valori negativi.", "Sai spiegare perche ogni cella dipende solo da sopra e sinistra?"),
    ("04_programmazione_dinamica", "2 settembre 2026", "DP: zaino", "zaino 0/1, tabella, ricostruzione, ottimizzazione spazio", ["Compila la tabella dello zaino per 5 oggetti.", "Ricostruisci gli oggetti scelti.", "Implementa la versione con spazio O(C).", "Confronta DP e backtracking sullo stesso input."], "Testa capacita zero, oggetto troppo pesante e valori uguali.", "Sai spiegare perche zaino 0/1 non usa lo stesso stato dello zaino frazionario?"),
    ("04_programmazione_dinamica", "3 settembre 2026", "DP: LCS e supersequenza", "sottosequenza comune, ricostruzione, minima supersequenza", ["Compila la tabella LCS di due stringhe.", "Ricostruisci una LCS dalla cella finale.", "Calcola la minima supersequenza.", "Dimostra la transizione per caratteri uguali e diversi."], "Implementa LCS e una funzione di ricostruzione.", "Sai distinguere sottosequenza, segmento e supersequenza?"),
    ("04_programmazione_dinamica", "4 settembre 2026", "DP avanzata", "palindromi, LIS, Kadane, numeri di Catalano", ["Riempi per diagonali la DP della massima sottosequenza palindroma.", "Calcola la LIS in O(n^2).", "Risolvi il massimo sottosegmento in O(n).", "Calcola i numeri di Catalano in O(n^2)."], "Per ogni esercizio scrivi complessita temporale e spaziale.", "Sai ricavare la direzione di riempimento dalla dipendenza?"),
    ("05_backtracking", "5 settembre 2026", "Backtracking: generazione", "configurazioni, vincoli, potatura, costo dell'output", ["Genera stringhe binarie.", "Genera stringhe palindrome.", "Genera stringhe bilanciate di 0 e 1.", "Genera permutazioni senza duplicati."], "Implementa il modello aggiungi-ricorri-annulla.", "Sai dimostrare O(nS(n)) considerando la stampa?"),
    ("05_backtracking", "6 settembre 2026", "Backtracking: decisione e ottimizzazione", "n-regine, Hamiltoniano, zaino e simulazione", ["Risolvi n-regine usando colonne e diagonali.", "Decidi se un grafo ha un ciclo Hamiltoniano.", "Risolvi zaino con backtracking.", "Svolgi una simulazione completa in 3 ore."], "Dopo la simulazione, riscrivi interamente l'esercizio peggiore.", "Sai giustificare ogni potatura e non solo il risultato?"),
    ("06_simulazioni", "7 settembre 2026", "Correzione della simulazione", "analisi degli errori e riscrittura", ["Rifai Dijkstra senza appunti.", "Rifai una DP su stringhe.", "Rifai n-regine.", "Correggi la simulazione e classifica gli errori: idea, prova, codice o complessita."], "Crea una pagina personale degli errori ricorrenti.", "Quale errore ti farebbe perdere piu punti e come lo previeni?"),
    ("06_simulazioni", "8 settembre 2026", "Simulazione mirata: grafi", "prova a tempo su DFS, BFS, Dijkstra e MST", ["DFS con ponte o articolazione in 15 minuti.", "BFS con cammino in 10 minuti.", "Dijkstra in 15 minuti.", "MST e domanda teorica in 20 minuti."], "Correggi con la checklist: idea, correttezza, tempo, spazio, casi limite.", "Sai completare una risposta rigorosa in meno di un'ora?"),
    ("06_simulazioni", "9 settembre 2026", "Simulazione mirata: paradigmi", "divide et impera, DP, backtracking e approssimazione", ["Risolvi una ricorrenza.", "Progetta una DP su stringhe o matrici.", "Scrivi un backtracking con potatura.", "Dimostra un rapporto di approssimazione."], "Per ogni traccia motiva perche il paradigma scelto e adatto.", "Sai progettare lo stato senza copiare un esempio?"),
    ("06_simulazioni", "10 settembre 2026", "Ripasso finale leggero", "formulario, ipotesi, complessita e preparazione all'esame", ["Ripeti a voce BFS, Dijkstra, Kruskal e una DP.", "Scrivi tutte le complessita senza consultare appunti.", "Svolgi un esercizio breve di grafi.", "Svolgi un esercizio breve di DP."], "Niente argomenti nuovi: prepara materiali e dormi bene.", "Sai iniziare ogni esercizio indicando tecnica e rappresentazione?"),
]

def make_source(date, title, theory, exercises, python_task, check):
    lines = [MACROS, f".TL\nSessione del {date}\n{title}", ".PP", f"Obiettivo della giornata: {theory}.", ".PP", "Tempo consigliato: 60 minuti nei feriali; nei weekend dividere in blocchi di teoria, esercizi, Python e correzione.", ".H\nRipasso essenziale", theory + ". Ripassa solo definizioni, ipotesi, idea dell'algoritmo e complessita. Alla fine prova a spiegare l'argomento in 3 minuti senza appunti.", ".H\nEsercizi del giorno"]
    for i, exercise in enumerate(exercises, 1):
        lines += [f".PP\n{ i}. {exercise}"]
    lines += [".H\nImplementazione Python", python_task + " Scrivi anche almeno tre test, inclusi un caso limite e un caso senza soluzione.", ".H\nVerifica prima di chiudere", check + " Se la risposta e no, segna l'errore e rifai l'esercizio domani prima del nuovo argomento.", ".H\nFormato della soluzione", "Per ogni esercizio consegna a te stesso: idea; pseudocodice; dimostrazione di correttezza; complessita temporale e spaziale; codice; test.", ".PP\nNon guardare le soluzioni della guida generale prima di aver prodotto una prima soluzione autonoma."]
    return "\n".join(lines) + "\n"

for folder, date, title, theory, exercises, python_task, check in sessions:
    target = ROOT / folder
    target.mkdir(parents=True, exist_ok=True)
    slug = date.split()[0].zfill(2) + "_" + date.split()[1].lower()
    source = target / f"{slug}.ms"
    pdf = target / f"{slug}.pdf"
    source.write_text(make_source(date, title, theory, exercises, python_task, check), encoding="utf-8")
    ps = target / f"{slug}.ps"
    subprocess.run(["groff", "-Kutf8", "-Tps", str(source)], stdout=ps.open("wb"), check=True)
    subprocess.run(["ps2pdf", str(ps), str(pdf)], check=True)
    ps.unlink()
