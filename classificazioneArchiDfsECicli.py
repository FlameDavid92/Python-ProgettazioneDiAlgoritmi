'''
Consideriamo un qualsiasi arco diretto (x, y) non appartenente all'albero della DFS. Per gli intervalli di visita
di x e y sono possibili solamente i seguenti casi:

- Gli intervalli di x e y sono disgiunti: non può essere t(x) < t(y) perchè l'arco (x, y) avrebbe forzato la visita
  di y durante la visita da x e i due intervalli non sarebbe stati disgiunti.
  Però può tranquillamente essere t(y) < t(x), cioè l'arco (x, y) è tra due nodi che non hanno rapporti di
  discedenza e va da quello più giovane a quello più vecchio. Questo tipo di arco
  (che non può esistere in grafi non diretti) è detto "arco di attraversamento" (in inglese cross edge).

- L'intervallo di x è contenuto nell'intervallo di y: l'arco va da un nodo x a un suo antenato y ed è detto arco
  all'indietro (in inglese back edge). Questo tipo di arco esiste anche in grafi non diretti.

- L'intervallo di x contiene l'intervallo di y: l'arco va da un nodo x a un suo discendente y. Questo vuol dire che
  il nodo y è stato visitato durante la DFS da x ma seguendo un cammino diverso dal semplice arco (x, y).
  Questo tipo di arco è detto arco in avanti (in inglese forward edge). Per i grafi non diretti coincide con l'arco
  all'indietro.


Se il grafo non è diretto (e connesso):
   la presenza di un qualsiasi arco all'indietro indica l'esistenza di un ciclo.
   E se non ci sono archi all'indietro il grafo è aciclico perchè coincide con l'albero della DFS.

Lo stesso vale per grafi diretti, cioè il grafo ha un ciclo se e solo se c'è almeno un arco all'indietro.
'''


def DFS_CYCLE(G, v, u, P, dir):
    P[v] = -u  # Il valore negativo indica che la visita è iniziata ma non è terminata
    for w in G[v]:
        if P[w] == 0:
            z = DFS_CYCLE(G, w, v, P, dir)
            if z != 0:  # Un ciclo è già stato trovato
                P[v] = -P[v]
                return z
        elif P[w] < 0 and (w != u or dir == 1):  # Trovato ciclo
            P[w] = 0  # Marca il primo nodo del ciclo
            P[v] = u
            return v
    P[v] = u  # La visita da u è terminata
    return 0  # senza aver trovato un ciclo


def dfs_cycle_nodeList(G, u):
    P = [0 for _ in G]
    w = DFS_CYCLE(G, u, u, P, 1)  # 1 se il grafo è diretto
    L = []
    while w > 0:
        L.append(w)
        w = P[w]
    return L


grf = {
    0: [1,10],
    1: [2],
    2: [3, 4, 7],
    3: [],
    4: [5],
    5: [6],
    6: [2],
    7: [8],
    8: [7, 9],
    9: [],
    10: [9]
}
print(dfs_cycle_nodeList(grf, 0))

'''
Si osservi che l'algoritmo DFS_CYCLE non costa più della DFS. Inoltre, nel caso di un grafo non diretto, può essere
molto più efficiente perché termina sempre in O(n). Infatti, se il grafo è aciclico la DFS stessa impiega O(n) 
perchè il grafo è un albero che ha solamente n - 1 archi. Se invece il grafo ha almeno un ciclo, l'algoritmo 
termina non appena trova un arco all'indietro. Al più saranno visitati tutti gli n - 2 archi dell'albero 
della DFS prima di incontrare un tale arco (dato che un qualsiasi arco o appartiene all'albero 
o è un arco all'indietro). Quindi il costo dell'algoritmo è O(n).
'''