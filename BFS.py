import collections
import math


def BFS(G, u):
    P = [-1 for _ in G]  # array dei padri
    DIST = [-1 for _ in G]  # array delle distanze
    P[u] = u  # radice dell'albero BFS
    DIST[u] = 0
    Q = collections.deque()
    Q.append(u)  # accoda u alla coda
    while len(Q) != 0:
        v = Q.popleft()  # preleva il primo nodo della coda
        for adjacent in G[v]:
            if P[adjacent] == -1:
                P[adjacent] = v
                DIST[adjacent] = DIST[v] + 1
                Q.append(adjacent)
    return P, DIST


'''
Il vettore dei padri rappresenta l'albero di visita della BFS e quindi per ogni nodo v contiene un cammino di lunghezza
minima da u a v. Per ricostruire un tale cammino basta partire da v e percorrerlo di padre in padre tramite P fino alla
radice u.
'''


def pathMinDist(G, u, v):
    P = BFS(G, u)[0]
    if P[v] != -1:
        L = collections.deque()
        L.appendleft(v)
        while v != u:
            v = P[v]
            L.appendleft(v)
        return L
    else:
        print("v non è raggiungibile a partire da u, la loro distanza è inf")
        return math.inf


def calcolaNCamminiMinimi(G, u):
    DIST = [-1 for _ in G]
    M = [0 for _ in G]
    DIST[u] = 0
    M[u] = 1
    Q = collections.deque()
    Q.append(u)
    while len(Q) != 0:
        v = Q.popleft()
        for adjacent in G[v]:
            if DIST[adjacent] == -1:
                DIST[adjacent] = DIST[v]+1
                M[adjacent] = M[v]
                Q.append(adjacent)
            elif DIST[adjacent] == DIST[v]+1:
                M[adjacent] = M[adjacent]+M[v]
    return M

grafetto = {
    0: [1, 3, 5],
    1: [2],
    2: [4],
    3: [5],
    4: [0],
    5: [4]
}

graf = {
    0: [2, 3, 4],
    1: [4],
    2: [5],
    3: [5],
    4: [5],
    5: [6, 7],
    6: [1],
    7: [1]
}


graf2 = {
    0: [3, 6, 7],
    1: [5],
    2: [4],
    3: [],
    4: [0, 3],
    5: [0, 2, 7],
    6: [],
    7: [2]
}

#C = BFS(grafetto, 0)
#print("PADRI: "+str(C[0])+"\nDISTANZE: "+str(C[1]))

#print(pathMinDist(grafetto, 0, 4))

#print(calcolaNCamminiMinimi(grafetto, 0))
#print(calcolaNCamminiMinimi(graf, 0))

C = BFS(graf2, 0)
print("PADRI: "+str(C[0])+"\nDISTANZE: "+str(C[1]))


def bfsRecArchi(G, u, contatori, c):
    VIS = [-1 for _ in G]
    c += 1
    VIS[u] = c
    P = [-1 for _ in G]  # array dei padri
    DIST = [-1 for _ in G]  # array delle distanze
    P[u] = u  # radice dell'albero BFS
    DIST[u] = 0
    Q = collections.deque()
    Q.append(u)  # accoda u alla coda
    while len(Q) != 0:
        v = Q.popleft()  # preleva il primo nodo della coda
        for adjacent in G[v]:
            if VIS[adjacent] == -1:
                contatori[0] += 1  # n. archi albero
                c += 1
                VIS[adjacent] = c
                P[adjacent] = v
                DIST[adjacent] = DIST[v] + 1
                Q.append(adjacent)
            elif VIS[adjacent] > 0:
                contatori[1] += 1  # n. archi all'indietro o di attraversamento
    return P, DIST


def calcolaArchiBFS(G, u):
    contatori = [0, 0]
    bfsRecArchi(G, 0, contatori, 0)
    print("n.archi albero: "+str(contatori[0]))
    print("n. archi all'indietro o di attraversamento: " + str(contatori[1]))


calcolaArchiBFS(graf2, 0)
