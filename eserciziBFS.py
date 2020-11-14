import BFS
import collections
import math
'''
Esercizio [dall'albero alle distanze]
Dato un vettore dei padri P che rappresenta l'albero di una BFS a partire da un nodo u, dare un algoritmo che calcola il
corrispondente array Dist delle distanze da u in tempo O(n).
'''

def calcolaDistanzeArrayPadriBFS(P):
    def dist(Pp, w, DDIST):
        if DDIST[w] == -1:
            if P[w] == w:
                DDIST[w] = 0
            else:
                DDIST[w] = dist(Pp, Pp[w], DDIST) + 1
        return DDIST[w]
    DIST = [-1 for _ in P]
    for i in range(0, len(P)):
        if DIST[i] == -1:
            DIST[i] = dist(P, i, DIST)
    return DIST


'''
Esercizio [stessa distanza]
Descrivere un algoritmo efficiente che, dato un grafo non diretto e connesso e due suoi nodi u e v, trova i nodi che hanno la stessa
distanza da u e v.
'''


def sameDist(G, u, v):
    DIST_u = BFS.BFS(G, u)[1]
    DIST_v = BFS.BFS(G, v)[1]
    S = []
    for node in G:
        if DIST_u[node] == DIST_v[node]:
            S.append(node)
    return S

'''
Esercizio [distanza tra insiemi]
Dato un grafo non diretto G e due sottoinsiemi A e B dei suoi nodi si definisce distanza tra A e B la distanza minima per andare da
un nodo in A ad un nodo in B. Se A e B non sono disgiunti, la loro distanza è 0. Descrivere un algoritmo che, dato G e due
sottoinsiemi dei nodi A e B calcola la loro distanza. L’algoritmo deve avere complessità O(n + m).
'''

def BFS_SET(G, A):
    DIST_A = [-1 for _ in G]
    Q = collections.deque()
    for node in A:
        DIST_A[node] = 0
        Q.append(node)
    while len(Q) != 0:
        v = Q.popleft()
        for adjacent in G[v]:
            if DIST_A[adjacent] == -1:
                DIST_A[adjacent] = DIST_A[v]+1
                Q.append(adjacent)
    return DIST_A

def distInsiemi(G, A, B):
    DIST_A = BFS_SET(G, A)
    d = math.inf
    for node in B:
        if DIST_A[node] < d:
            d = DIST_A[node]
    return d


def calcolaGT(G):
    Gt = {x: [] for x in G}
    for node in G:
        for adjacent in G[node]:
            Gt[adjacent].append(node)
    return Gt

'''
Esercizio [Roma]
Descrivere un algoritmo che, dato un grafo diretto e fortemente connesso e un suo nodo r, trova tutti i cammini minimi tra tutte le
coppie di nodi con il vincolo che questi cammini devono passare per r.

CENTER(G: grafo diretto, r: nodo)
P <- BFS(G, r) /* Vettore dei padri dell'albero dei cammini minimi di G da r */
GT <- TRASP(G) /* Ritorna il grafo trasposto */
PT <- BFS(GT, r) /* Vettore dei padri dell'albero dei cammini minimi di GT da r */
RETURN P, PT


C_u <- lista vuota
DO
C_u.append(u)
u <- PT[u]
WHILE u <> r
C_v <- lista vuota
WHILE v <> r DO
C_v.head(v)
v <- P[v]
C <- concatenazione di C_u e C_v
OUTPUT C
'''


def centerMinPath(G, u, v, r):  # G grafo, u nodo inizio, v nodo fine, r nodo vincolo
    P = BFS.BFS(G, r)[0]
    GT = calcolaGT(G)
    PT = BFS.BFS(GT, r)[0]

    C_u = [u]
    u = PT[u]
    while u != r:
        C_u.append(u)
        u = PT[u]
    C_u.append(r)
    C_v = []
    while v != r:
        C_v.append(v)
        v = P[v]
    C_v.reverse()
    return C_u+C_v



#PADRI = [0, 0, 1, 0, 5, 0]
#print(calcolaDistanzeArrayPadriBFS(PADRI))
Ggg = {
    0: [1, 5],
    1: [0, 2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 6],
    5: [0, 6],
    6: [4, 5]
}

grafoFortConn = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2]
}

print(sameDist(Ggg, 1, 4))

print(distInsiemi(Ggg, {0, 1, 2}, {6}))

print(centerMinPath(grafoFortConn, 0, 2, 3))
