import copy
'''
Esercizio [archi]
Vogliamo scrivere un algoritmo che esegue una DFS su un grafo diretto e ritorna il numero di archi dell'albero della
DFS, il numero di archi all'indietro, il numero di archi in avanti e il numero di archi di attraversamento.
'''


def dfsRecArchi(G, u, VIS, contatori, c):
    c += 1
    VIS[u] = -c
    for adjacent in G[u]:
        if VIS[adjacent] == -1:
            contatori[0] += 1  # n. archi albero
            c = dfsRecArchi(G, adjacent, VIS, contatori, c)
        elif VIS[adjacent] < 0:
            contatori[1] += 1  # n. archi all'indietro
        elif VIS[adjacent] > -VIS[u]:
            contatori[2] += 1  # n. archi in avanti
        else: contatori[3] += 1  #n. archi di attraversamento
    VIS[u] = -VIS[u]
    return c


def calcolaArchi(G, u):
    VIS = [-1 for _ in G]
    contatori = [0, 0, 0, 0]
    dfsRecArchi(G, u, VIS, contatori, 0)
    print("n.archi albero: "+str(contatori[0]))
    print("n.archi attraversamento: " + str(contatori[3]))
    print("n. archi all'indietro: " + str(contatori[1]))
    print("n. archi in avanti: " + str(contatori[2]))


'''
Esercizio [trasposto]
Il grafo trasposto di un grafo diretto G = (V, E), e un grafo diretto GT = (V, ET) che ha lo stesso insieme dei nodi ma
tutti gli archi con direzione opposta, vale a dire ET = { (v, u) | (u, v) in E }. Descrivere un algoritmo che dato un grafo
diretto G, rappresentato tramite liste di adiacenza degli adiacenti uscenti, ritorna il grafo trasposto GT
rappresentato nello stesso modo. L'algoritmo deve avere complessita O(n + m).
'''


def dfsTrasp(G, GT, VIS, node):
    VIS[node] = 0
    for adjacent in G[node]:
        GT[adjacent].append(node)
        if VIS[adjacent] == -1:
            dfsTrasp(G, GT, VIS, adjacent)


def creaGTrasp(G):
    VIS = [-1 for _ in G]
    GT = {x: [] for x in G}
    for node in G:
        if VIS[node] == -1:
            dfsTrasp(G, GT, VIS, node)
    return GT

def creaGTrasp2(G):
    GT = {x: [] for x in G}
    for node in G:
        for adjacent in G[node]:
            GT[adjacent].append(node)
    return GT


'''
Esercizio [ponte]
Descrivere un algoritmo che, dato un grafo non diretto G e un arco {u, v} del grafo, determina se G ha un ciclo che
contiene {u, v}. Analizzare il tempo di esecuzione dell’algoritmo. E se, nel caso un ciclo esista, vogliamo anche
trovare un ciclo che contiene l'arco?

Se un arco {u, v} di un grafo non diretto G non è contenuto in nessun ciclo, allora nel grafo G' ottenuto rimuovendo
l'arco da G, i nodi u e v non sono connessi. Infatti, se lo fossero vuol dire che ci sarebbe in G' un cammino che li
collega e siccome tale cammino non contiene l'arco {u, v}, il cammino insieme a tale arco è un ciclo in G che
contiene l'arco, contraddizione. Viceversa, se la rimozione dell'arco {u, v} sconnette i nodi u e v vuol dire che non ci
poteva essere un ciclo che conteneva l'arco. Quindi abbiamo diamostrato
In un grafo non diretto e connesso G, un arco non è contenuto in nessun ciclo se e solo se la rimozione
dell'arco sconnette il grafo.
Un arco la cui rimozione sconnette un grafo connesso è chiamato ponte (bridge). Un algoritmo molto semplice per
determinare se un arco è un ponte di un grafo G non diretto e connesso consiste nel fare una visita del grafo G'
ottenuto rimuovendo l'arco. Se G' è sconnesso, l'arco è un ponte, altrimenti non lo è. Se in generale il grafo non è
connesso lo stesso ragionamento vale per la componente connessa che contiene l'arco da esaminare (ovvero la
visita parte da uno dei due estremi dell'arco). Chiaramente, tale algoritmo ha complessità O(n + m).
Nel caso vogliamo anche trovare un ciclo che contiene l'arco {u, v} (se esiste) basterà fare una DFS a partire da u
facendo in modo che il primo adiacente scelto sia proprio v. In questo modo la DFS troverà un arco all'indietro che
arriva al nodo u e da qui possiamo ricostruire il ciclo come già sappiamo.
'''


def dfs(Gp, u, VIS):
    VIS[u] = 0
    for adjacent in Gp[u]:
        if VIS[adjacent] == -1:
            dfs(Gp, adjacent, VIS)


def dfsRetInd(G, arcA, arcB, v, C, VIStime, P):
    C[0] += 1
    VIStime[v] = -C[0]
    for adjacent in G[v]:
        if VIStime[adjacent] == 0:
            P[adjacent] = v
            check = dfsRetInd(G, arcA, arcB, adjacent, C, VIStime, P)
            if check != -1:
                return check
        elif v != arcB and adjacent == arcA and VIStime[adjacent] < 0:
            print("trovato v: "+ str(v))
            return v
    VIStime[v] = -VIStime[v]
    return -1


#  Per grafi non diretti!
def trovaPonte(G, u, v):
    Gp = copy.deepcopy(G)
    try:
        Gp[u].remove(v)
        VIS = [-1 for _ in G]
        dfs(Gp, u, VIS)
        if VIS[v] == -1:
            print("l'arco {" + str(u) + "," + str(v) + "} è un ponte")
            return 0  # l'arco è un ponte
        else:
            print("l'arco {"+str(u)+","+str(v)+"} NON è un ponte")
            return 1  # l'arco non è un ponte (c'è un ciclo nel grafo G, rappresentato dal cammino semplice da u a v in Gp a cui si aggiunge l'arco {u,v})
    except ValueError:
        print("arco {"+str(u)+","+str(v)+"} non presente in G")
        return -1  # errore non esiste l'arco {u,v} in G


def checkCycleEdge(G, u, v):
    if trovaPonte(G, u, v) == 1:
        P = [-1 for x in G]
        VIStime = [0 for x in G]
        P[u] = u
        C = [1]
        VIStime[u] = -C[0]
        P[v] = u
        ret = dfsRetInd(G, u, v, v, C, VIStime, P)
        VIStime[u] = -VIStime[u]
        if ret != -1:
            w = ret
            print(str(w), end='')
            while w != u:
                print(" " + str(P[w]), end='')
                w = P[w]
            print("")
        return ret  # se ret != -1 {c,u} rappresenta l'arco all'indietro che chiude il ciclo
    else:
        print("l'arco {"+str(u)+","+str(v)+"} non fa parte di un ciclo")
        return -1  # l'arco {u,v} non fa parte di un ciclo


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

calcolaArchi(grfDag, 0)
print(creaGTrasp(grfDag))
print(creaGTrasp2(grfDag))

grfNonDirCicl = {
    0: [1, 7],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4, 7],
    4: [3, 5, 6],
    5: [4, 6],
    6: [4, 5],
    7: [0, 3, 8],
    8: [7],
}

grfDirCicl = {
    0: [1],
    1: [2],
    2: [3, 9],
    3: [4, 5],
    4: [6],
    5: [6],
    6: [7],
    7: [8],
    8: [6],
    9: []
}
print("________________________")
trovaPonte(grfNonDirCicl, 2, 3)
trovaPonte(grfNonDirCicl, 7, 8)
trovaPonte(grfNonDirCicl, 3, 4)
trovaPonte(grfNonDirCicl, 3, 7)
trovaPonte(grfNonDirCicl, 4, 0)
checkCycleEdge(grfNonDirCicl, 3, 7)
checkCycleEdge(grfNonDirCicl, 4, 6)
#checkCycleEdge(grfDirCicl, 6, 7) #  Errore poiché l'algoritmo vale solo per i grafi NON diretti!

'''
Esercizio [grado due]
Dimostrare che se tutti i nodi di un grafo non diretto G hanno grado almeno due allora c’è almeno un ciclo. Se il
grado di ogni nodo è esattamente due, si puo affermare che G è un ciclo?

Un modo molto semplice di dimostrare che se ogni nodo di un grafo non diretto G ha grado almeno due allora il
grafo contiene un ciclo e di considerare una DFS a partire da un nodo di G. La visita dovrà necessariamente
incontrare un nodo w che è una foglia dell'albero della DFS e siccome w ha grado almeno due, w deve avere
almeno un altro arco oltre a quello che appartiene all'albero. Sappiamo che tale arco, non appartenendo all'albero,
non potrà che essere un arco all'indietro e questo dimostra l'esistenza di un ciclo.
Se ogni nodo di G ha grado esattamente due, non è detto che G sia un ciclo. Potrebbe infatti essere formato da
due o più cicli disgiunti. Se invece è anche connesso, allora è necessariamente un ciclo. Perché?

Perché la DFS a partire da uno qualunque dei nodi di G riuscirà a visitare tutti i nodi di G trovando infine 
nel nodo foglia dell'albero DFS un arco all'indietro verso il nodo da cui è partita la DFS
(poiché anche questo è di grado 2).

'''