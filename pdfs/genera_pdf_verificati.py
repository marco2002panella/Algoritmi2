from pathlib import Path
import subprocess

TARGET = Path(__file__).parent / "percorso_giornaliero/01_grafi/19_agosto.pdf"
TMP = Path("/tmp/19_agosto_verificato.ms")
PS = Path("/tmp/19_agosto_verificato.ps")

text = r'''.po 0.7i
.nr PS 10
.nr VS 12
.de T
.sp 1
.ce 2
.ft B
.ps 18
Sessione del 19 agosto 2026
Grafi: definizioni e rappresentazioni
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
.T
.P
Fonte verificata: PL2.pdf, Introduzione alla Teoria dei Grafi, slide 1-22.
Questa sessione corregge e sostituisce la precedente versione generica.
.H
Obiettivi
.P
Devi saper distinguere il grafo matematico dalla sua rappresentazione, usare
n per i nodi e m per gli archi, scegliere tra matrice e lista di adiacenza e
motivare tempo e spazio delle operazioni principali.
.H
Teoria indispensabile
.P
Un grafo e una coppia G=(V,E), dove V e l'insieme dei nodi ed E l'insieme
degli archi. Nei grafi non orientati un arco e una coppia non ordinata {u,v};
nei grafi orientati e una coppia ordinata (u,v).
.P
Matrice di adiacenza: M[i][j]=1 se esiste un arco da i a j, 0 altrimenti.
Occupa Theta(n^2), verifica un arco in O(1) e scorre i vicini di un nodo in
Theta(n).
.P
Lista di adiacenza: ogni nodo u ha associata una lista dei nodi adiacenti.
Occupa Theta(n+m), scorre i vicini di u in Theta(grado(u)) e verifica un
arco in O(grado(u)), nel caso peggiore O(n). Nei grafi non orientati ogni
arco compare nelle liste di entrambi gli estremi.
.P
In Python, una lista di liste usa spesso l'indice come nodo. Un dizionario ha
la stessa idea: ogni chiave e un nodo e il valore e la lista dei suoi vicini.
.H
Esercizi del giorno
.P
1. Sia G un grafo non orientato con nodi 0,1,2,3,4,5 e archi {0,2}, {0,5},
{1,2}, {1,3}, {2,4}, {3,4}, {3,5}, {4,5}. Costruisci la lista di adiacenza
completa e verifica che la somma delle lunghezze sia 2m.
.P
2. Scrivi una funzione che, data una lista di adiacenza non orientata, conti
gli archi. Indica l'ipotesi per cui la somma va divisa per due e la complessita.
.P
3. Confronta matrice e lista per queste operazioni: verificare un arco,
scorrere tutti i vicini di u, memorizzare un grafo sparso e visitare il grafo.
Riporta tempo e spazio secondo PL2.
.P
4. Formalizza la differenza tra grafo orientato e non orientato e riscrivi la
lista dell'esercizio 1 come grafo orientato usando gli stessi archi solo nel
verso indicato da te.
.P
5. Dimostra che per un albero vale m=n-1. Poi spiega perche i grafi planari e
gli alberi sono esempi di grafi sparsi.
.P
6. Risolvi gli esercizi teorici della sezione finale di PL2: somma dei gradi,
numero pari di nodi di grado dispari, ciclo se ogni grado e almeno 2, due nodi
con lo stesso grado e connettivita di G o del complementare.
.H
Python da scrivere
.P
Implementa costruzione, stampa e conteggio di una lista di adiacenza. Usa solo
liste e funzioni semplici; non usare librerie esterne. Testa grafo vuoto,
un solo nodo, grafo sconnesso e grafo con archi duplicati non ammessi.
.H
Verifica finale
.P
Senza appunti, spiega in tre minuti: (a) cosa rappresenta G[u]; (b) perche un
arco non orientato viene memorizzato due volte; (c) perche la lista occupa
Theta(n+m); (d) quando la matrice e preferibile.
.H
Riferimenti
.P
PL2.pdf: definizione di grafo slide 1-2; matrici slide 8-9; liste slide 10-11;
dizionari slide 12; pozzo universale slide 15-21; esercizi slide 22.
'''

TMP.write_text(text, encoding="utf-8")
with PS.open("wb") as output:
    subprocess.run(["groff", "-Kutf8", "-Tps", str(TMP)], stdout=output, check=True)
subprocess.run(["ps2pdf", str(PS), str(TARGET)], check=True)
TMP.unlink()
PS.unlink()
