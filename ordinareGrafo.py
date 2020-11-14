#import simpleStackQueue
import collections

'''
!!!Se un grafo è aciclico, esiste almeno un nodo che non ha archi entranti.!!!
dim: Se così non fosse potremmo partire da un nodo v1 e prendere un suo arco entrante che esce da un nodo v2, poi
prendere un arco entrante in v2 e uscente da un nodo v3 diverso dai primi due perché il grafo è aciclico, anche v3
ha un arco entrante che deve uscire, per le stesse ragioni, da un quarto nodo distinto v4 e procedendo in questo
modo si arriverebbe all'n-esimo nodo ma quest'ultimo ha un arco entrante che necessariamente dovrebbe uscire
da uno dei nodi già considerati chiudendo un ciclo che non può esistere, contraddizione.

Grazie a questa proprietà possiamo costruire un ordine come segue. Come primo nodo scegliamo un nodo v1
senza archi entranti (cioè, una lavorazione senza vincoli). Eliminando v1 dal grafo rimaniamo con un grafo aciclico e
da questo scegliamo un nodo v2 senza archi entranti (cioè, una lavorazione o senza vincoli o che aveva come unico
vincolo v1). Eliminiamo v2 e otteniamo un grafo ancora aciclico e da questo scegliamo v3 un nodo senza archi
entranti (cioè, una lavorazione o senza vincoli o che aveva come vincoli solo v1 o v2). Possiamo procedere in questo
modo fino all'ultimo nodo.--->Implementazione 1: Grafo dato con liste di adiacenza

Ordine topologico
Effettuiamo una DFS su un DAG G. Se la DFS da v termina dopo la DFS da w, siamo certi che non ci può essere un
arco da w a v. Infatti, se ci fosse sarebbe un arco all'indietro ma in un DAG non essendoci cicli non ci possono
essere archi all'indietro. Allora possiamo ottenere un ordinamento topologico di un DAG semplicemente ordinando i
nodi per tempi di fine visita decrescenti. Quindi, ogniqualvolta la DFS da un nodo v termina, inseriremo v in testa
alla lista che mantiene l'ordine.

'''


def dfsOrd(dag, node, VIS, L):
    VIS[node] = 0
    for adjacent in dag[node]:
        if VIS[adjacent] == -1:
            dfsOrd(dag, adjacent, VIS, L)
    L.appendleft(node)

#  Ordinamento nodi per un grafo diretto aciclico
def ordTop(dag):
    L = collections.deque()
    VIS = [-1 for _ in dag]
    for node in dag:
        if VIS[node] == -1:
            dfsOrd(dag, node, VIS, L)
    return L


def calcolaGradoEntranti(dag):
    ge = [0 for _ in dag]
    for node in dag:
        for adjacent in dag[node]:
            ge[adjacent] += 1
    return ge


def ordTop2(dag):
    L = []
    gradoEntranti = calcolaGradoEntranti(dag)  # O(n+m)
    S = []
    for node in dag:  # O(n)
        if gradoEntranti[node] == 0:
            S.append(node)
    while len(S) >= 1:  # Ad ogni passo del while viene preso in considerazione un nodo x senza archi entranti che verrà in seguito "rimosso" da G ed i nodi nella sua lista di adiacienze--> O(n+m)
        v = S.pop()
        L.append(v)
        for adjacent in dag[v]:
            gradoEntranti[adjacent] -= 1
            if gradoEntranti[adjacent] == 0:
                S.append(adjacent)
    return L


grfDag = {
    0: [4, 6],
    1: [2, 5],
    2: [3],
    3: [5],
    4: [1],
    5: [],
    6: [7, 11],
    7: [8, 9],
    8: [],
    9: [1, 10],
    10: [],
    11: []
}
print(ordTop(grfDag))
print(ordTop2(grfDag))

'''
ordTop2

La costruzione dell'array dei gradi entranti ha costo O(n + m) perché fa semplicemente una scansione
dell'intero grafo. L'inizializzazione dello stack dei nodi con grado entrante zero costa O(n). Il WHILE esegue n
iterazioni e complessivamente il numero di iterazioni del FOR interno è pari al numero di tutti gli archi, cioè m.
Quindi la complessità totale è O(n + m).
'''
