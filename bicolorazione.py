import simpleStackQueue

'''
COLORAZIONE DI UN GRAFO
-Dato un grafo si vogliono colorare i nodi usando il numero minimo di colori che garantiscono che due
qualsiasi nodi adiacenti hanno colori diversi.

Problema: sapere se esiste e in tal caso trovare una cosidetta 2-colorazione del nostro grafo.

Un altro modo di vedere il problema è di vedere l'assegnamento dei due colori ai nodi come la partizione del grafo
in due insiemi (disgiunti) tali che non ci sono archi tra nodi appartenenti alla stessa parte.
Un grafo che può esserecosì partizionato si dice bipartito.
'''


def dfsBiCol(G, node, bc):
    bc[node] = 0
    S = simpleStackQueue.Stack()
    S.push(node)
    while S.size() >= 1:
        v = S.top()
        control = 0
        for adjacent in G[v]:
            if bc[adjacent] == -1:
                bc[adjacent] = 1 if bc[v] == 0 else 0
                control = 1
                S.push(adjacent)
            else:
                if bc[adjacent] == bc[v]:
                    return -1
        if control == 0:
            S.pop()
    return 0


def dfsBiCol2(G, u, bc):
    for adjacent in G[u]:
        if bc[adjacent] == -1:
            bc[adjacent] = 1 if bc[u] == 0 else 0
            c = dfsBiCol2(G, adjacent, bc)
            if c == -1:
                return -1
        elif bc[adjacent] == bc[u]:
            print("Grafo non bicolorabile!")
            return -1
    return 0


def biCol(G):
    bc = [-1 for _ in G]
    for node in G:
        if bc[node] == -1:
            if dfsBiCol(G, node, bc) == -1:
                return None
    return bc


def biCol2(G):
    bc = [-1 for _ in G]
    for node in G:
        if bc[node] == -1:
            bc[node] = 0
            if dfsBiCol2(G, node, bc) == -1:
                return None
    return bc


graph = {
    0: [4],
    1: [2, 4],
    2: [1, 3],
    3: [2, 4, 5],
    4: [0, 1, 3],
    5: [3],
    6: [7, 8],
    7: [6],
    8: [6, 9],
    9: [8],
    10: [11, 12, 13],
    11: [10],
    12: [10],
    13: [10]
}

G_nonbic2 = {
    0: [1, 4],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 0]}

print(biCol2(graph))
print(biCol2(G_nonbic2))

'''
Usando la DFS si può risolvere il problema della 2-colorazione (o bipartizione) in modo molto efficiente, cioè, in
tempo O(n + m).

In generale, il problema della colorazione è molto più difficile. Determinare se un grafo è 3-colorabile è già un
problema per cui non si conoscono algoritmi efficienti. Gli algoritmi migliori hanno complessità esponenziale nella
dimensione del grafo.
'''
