import copy
'''
Esercizio [pozzo]
In un grafo diretto, un nodo si dice pozzo universale se ha grado entrante n − 1 e grado uscente 0.
Dimostrare che un grafo diretto non può avere più di un pozzo universale.
Descrivere un algoritmo che preso un grafo diretto G, rappresentato tramite matrice di adiacenza, determina
se G contiene o meno un pozzo universale. L’algoritmo deve avere complessità O(n).
Dimostrare che il problema non è risolvibile in tempo O(n) se il grafo è rappresentato con liste di adiacenza.


- Se un grafo ha un pozzo universale u allora per un qualsiasi altro nodo v c'è l'arco (v, u) che essendo un arco
uscente da v impedisce che v possa essere un pozzo universale.

-Se consideriamo due nodi qualsiasi u e v e ci chiediamo se c'è un arco da u a v in base alla risposta
possiamo escludere con certezza che uno dei due nodi sia il pozzo (se l'arco c'è escludiamo u altrimenti
escludiamo v). A questo punto l'idea di un algoritmo per trovare il pozzo universale, se esiste, è molto
semplice. Scegliamo due nodi, diciamo u e v, e vediamo se c'è l'arco da u a v. Per quanto detto almeno uno
dei due nodi sarà scartato e quindi scegliamo un altro nodo w. Applichiamo la stessa procedura ai due nodi
in esame scartandone almeno uno. Continuando così fino a considerare tutti i nodi, alla fine o rimarremo con
un solo nodo oppure li avremo scartati tutti e il pozzo universale non c'è. Se rimaniamo con un nodo
dobbiamo solamente verificare che sia il pozzo universale.


N.B.
Se il grafo è rappresentato tramite liste di adiacenza non è possibile risolvere il problema in tempo O(n)
perché per verificare che un nodo sia un pozzo universale bisogna controllare che abbia grado entrante n - 1
e questo richiede la scansione delle liste di adiacenza di tutti gli altri nodi.
'''


def pozzo(matG):
    p = 0  # nodo qualsiasi, es. nodo iniziale nella rappresentazione a matrice
    for node in range(0, len(matG)):
        if node != p and matG[p][node] == 1:
            #  il p corrente ha un arco uscente e quindi non può essere un pozzo
            p = node
    for node in range(0, len(matG)):
        if node != p and (matG[node][p] == 0 or matG[p][node] == 1):
            print("Non ci sono pozzi universali nel grafo")
            return -1
    print("Il pozzo universale del grafo è "+str(p))
    return p


matGpoz = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

matGnopoz = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

pozzo(matGpoz)
print(" ")
pozzo(matGnopoz)

'''
Esercizio per casa [strade critiche]
La rete viaria di una cittadina non è stata progettata molto bene. Tutte le strade sono a doppio senso di marcia e da
un qualsiasi incrocio è possibile arrivare ad un qualsiasi altro incrocio. Ma ci sono delle strade critiche che se
interrotte (ad esempio per lavori) dividono la cittadina in due parti e non si può più andare da una parte all'altra.
Vogliamo un algoritmo efficiente che analizzando la rete viaria trovi tutte le strade critiche.

- Algoritmo che trova tutti i ponti di un Grafo non diretto connesso
-nodi: incroci
-archi: strade a doppio senso
'''

def dfs(Gp, u, P):
    for adjacent in Gp[u]:
        if P[adjacent] == -1:
            P[adjacent] = u
            dfs(Gp, adjacent, P)

#  Per grafi non diretti!
def trovaPonteConVetPadri(G, u, v, P):
    Gp = copy.deepcopy(G)
    try:
        Gp[u].remove(v)
        P[u] = u
        dfs(Gp, u, P)
        if P[v] == -1:
            print("l'arco {" + str(u) + "," + str(v) + "} è un ponte")
            return 0  # l'arco è un ponte
        else:
            print("l'arco {"+str(u)+","+str(v)+"} NON è un ponte")
            return 1  # l'arco non è un ponte (c'è un ciclo nel grafo G, rappresentato dal cammino semplice da u a v in Gp a cui si aggiunge l'arco {u,v})
    except ValueError:
        print("arco {"+str(u)+","+str(v)+"} non presente in G")
        return -1  # errore non esiste l'arco {u,v} in G


def dfsPonti(G, node, VIST, L, M):
    VIST[node] = 0
    for adjacent in G[node]:
        if VIST[adjacent] == -1 and M[node][adjacent] == -1:
            P = [-1 for _ in G]
            c = trovaPonteConVetPadri(G, node, adjacent, P)
            if c == 1:
                P[node] = adjacent
                print(str(adjacent), end='')
                w = adjacent
                M[w][P[w]] = 0
                M[P[w]][w] = 0
                while w != node:
                    print(" "+str(P[w]), end='')
                    w = P[w]
                    M[w][P[w]] = 0
                    M[P[w]][w] = 0
                print("")
                print(str(M))
            elif c == 0:
                L.append((node, adjacent))
            dfsPonti(G, adjacent, VIST, L, M)


def trovaPontiNonEff(G):
    L = []
    M = [[-1 for _ in G] for _ in G]
    VIST = [-1 for _ in G]
    for node in G:
        if VIST[node] == -1:
            dfsPonti(G, node, VIST, L, M)
    return L


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
print(trovaPontiNonEff(grfNonDirCicl))

