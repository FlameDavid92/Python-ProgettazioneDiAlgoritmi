import simpleStackQueue

'''
Discussione dell'esercizio [sensi unici]
La rete viaria della cittadina può essere rappresentata facilmente tramite un grafo diretto in cui i nodi sono gli
incroci di due o più strade e ogni arco corrisponde a una strada (tra due incroci). Allora la proprietà che vorrebbe il
sindaco equivale alla forte connessione del grafo. Si osservi che non fa differenza se due punti A e B che si
vogliono connettere sono sugli incroci o sulle strade.
Come possiamo verificare se un grafo è fortemente connesso? Un modo semplice consiste nel fare una visita a
partire da ogni nodo del grafo. Se tutte le visite raggiungono tutti i nodi del grafo, allora il grafo è fortemente
connesso. Altrimenti non lo è. Ma questo algoritmo è piuttosto inefficiente, infatti richiede n visite e quindi tempo
O(n(n + m)).
Ma non è necessario effettuare così tante visite, cioè una per ogni nodo del grafo. Se un grafo G è fortemente
connesso, fissando un nodo u, sappiamo che tutti i nodi di G sono raggiungibili da u e che da ogni nodo si può
raggiungere u. Inoltre la validità di questa proprietà per uno specifico nodo, implica che il grafo è fortemente
connesso. Infatti, dati due qualsiasi nodi v e w, si può ottenere un cammino che va da v a w concatenando un
cammino da v a u con uno da u a w e tali cammini esistono in virtù della proprietà suddetta; in modo simmetrico si
ottiene un cammino da w a v. Riassumendo abbiamo un algoritmo per verificare se un grafo G è fortemente
connesso: facciamo una visita da un nodo fissato u per verificare che tutti i nodi sono raggiungibili da u e poi, per
verificare che da ogni nodo u è raggiungibile, basta fare una visita da u del grafo trasposto.
'''


def dfs(G, u, VIS):
    VIS[u] = 0
    for w in G[u]:
        if VIS[w] == -1:
            dfs(G, w, VIS)


def checkForteConnessione(G):
    VIS = [-1 for _ in G]
    dfs(G, 0, VIS)  # scegliamo 0 come nodo di partenza ma va bene un qualunque nodo.
    for x in VIS:
        if x == -1:
            print("Non è possibile raggiungere tutti i nodi da 0")
            return -1  # Non è possibile raggiungere tutti i nodi da 0
    Gt = {x: [] for x in G}
    for node in G:
        for adjacent in G[node]:
            Gt[adjacent].append(node)
    for node in G:
        VIS[node] = -1
    dfs(Gt, 0, VIS)
    for x in VIS:
        if x == -1:
            print("Non è possibile raggiungere 0 da tutti i nodi")
            return -1  # Non è possibile raggiungere 0 da tutti i nodi
    print("Il grafo è fortemente connesso")
    return 0


'''Algoritmo di Tarjan'''

def DFS_SCCTarj(G, node, CC, S, c, nc):
    c[0] += 1
    CC[node] = -c[0]  # il tempo di inizio visita in negativo per distinguerlo dall'indice di una componente
    S.push(node)
    back = c[0]
    for adjacent in G[node]:
        if CC[adjacent] == 0:
            b = DFS_SCCTarj(G, adjacent, CC, S, c, nc)
            back = min(back, b)
        elif CC[adjacent] < 0:  # la componente di adjacent non è ancora stata determinata
            back = min(back, -CC[adjacent])
    if back == -CC[node]:  # node è una c-radice
        nc[0] += 1
        w = S.pop()
        CC[w] = nc[0]
        while w != node:
            w = S.pop()
            CC[w] = nc[0]
    return back

def SCCTarj(G):
    CC = [0 for _ in G]  # array che darà l'indice della componente di ogni nodo, inizializzato a 0
    nc = [0]  # contatore componenti
    c = [0]  # contatore nodi visitati
    S = simpleStackQueue.Stack()
    for node in G:
        if CC[node] == 0:
            DFS_SCCTarj(G, node, CC, S, c, nc)
    return CC

def DFSNumVis(G, u):
    def DFSVIS(Gg, uu, VVIS):
        VVIS[uu] = 0
        for adjacent in Gg[uu]:
            if VVIS[adjacent] == -1:
                DFSVIS(Gg, adjacent, VVIS)
    VIS = [-1 for _ in G]
    DFSVIS(G, u, VIS)
    count = 0
    for n in VIS:
        if n == 0:
            count += 1
    return count

#  esercizio nodi broadcast
def DFS_BroadcastNodes(G):
    CC = SCCTarj(G)
    nc = 0
    u = 0
    for node in G:
        if CC[node] > nc:
            nc = CC[node]
            u = node
    vis = DFSNumVis(G, u)
    print(vis)
    B = []
    if vis == len(G):
        for node in G:
            if CC[node] == nc:
                B.append(node)
    return B

grafoFortConn = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [2]
}
grafoNonFortConn1 = {
    0: [1, 2, 3],
    1: [],
    2: [1],
    3: [2]
}

grafoNonFortConn2 = {
    0: [1],
    1: [0],
    2: [0],
    3: [0, 2]
}

#checkForteConnessione(grafoFortConn)
#checkForteConnessione(grafoNonFortConn1)
#checkForteConnessione(grafoNonFortConn2)
print(SCCTarj(grafoFortConn))
print(SCCTarj(grafoNonFortConn1))
print(SCCTarj(grafoNonFortConn2))

print(DFS_BroadcastNodes(grafoNonFortConn2))