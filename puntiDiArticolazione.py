'''
C'è una certa parentela tra i punti di articolazione e i ponti. Se {u, v} è un ponte tale che u ha grado almeno 2, allora
u è un punto di articolazione. Però se u è un punto di articolazione, non è detto che qualche arco incidente in u sia
un ponte.

Punti di articolazione
Vediamo allora come trovare i punti di articolazione. Facciamo una DFS di un grafo non diretto e connesso G,
partendo da un nodo u. Come possiamo riconoscere se u è un punto di articolazione? Chiaramente, una
condizione sufficiente affinché non lo sia è che la rimozione di u non sconnetta l'albero di visita (se la rimozione non
sconnette l'albero di visita a maggior ragione non sconnette G). È anche una condizione necessaria perché u non
sia un punto di articolazione? In altri termini, se la rimozione di u sconnette l'albero di visita, sconnette anche il
grafo?
Iniziamo con la radice u dell'albero della DFS. Se la rimozione di u sconnette l'albero, allora u ha almeno due
sottoalberi figli. Se eliminiamo u i sottografi relativi a questi sottoalberi saranno connessi solo se ci sono archi tra di
essi. Ma non ci possono essere tali archi perchè non sarebbero archi all'indietro. Quindi, se la rimozione di u
sconnette l'albero di visita, sconnette anche il grafo. Ne segue che la radice della DFS è un punto di articolazione
se e solo se ha almeno due figli. Vediamo ora gli altri nodi. Se un nodo v è un punto di articolazione, la sua
rimozione necessariamente sconnette almeno un sottoalbero S della DFS da v. Nel senso che i nodi di S non sono
più raggiungibili da u, nel grafo senza v. Questo accade se e solo se non ci sono archi all'indietro da nodi di S a
antenati di v. Quindi, un nodo v, diverso dalla radice della DFS, è un punto di articolazione se e solo se esiste un
sottoalbero della DFS da v che non ha archi all'indietro verso antenati di v.
Possiamo incorporare queste osservazioni in un algoritmo per trovare i punti di articolazione. Modifichiamo la DFS
per mantenere i tempi di inizio visita dei nodi in un array tt . Inoltre, per determinare le condizioni circa gli archi
all'indietro dei sottoalberi, facciamo sì che la procedura modificata di visita DFS da v ritorni il minimo tempo di inizio
visita tra quelli di tutti i nodi toccati durante la DFS da v. Così, un nodo v è un punto di articolazione se e solo se
esiste un figlio w di v per cui il valore b ritornato dalla visita modificata da w soddisfa b >= tt[v] .
'''


def dfsPA(G, u, tt, C, A):
    C[0] += 1
    tt[u] = C[0]
    back = C[0]
    children = 0
    for adjacent in G[u]:
        if tt[adjacent] == 0:
            children += 1
            b = dfsPA(G, adjacent, tt, C, A)
            if tt[u] > 1 and b >= tt[u]:
                A.add(u)
            back = min(back, b)
        else:
            back = min(back, tt[adjacent])
    if tt[u] == 1 and children >= 2:
        A.add(u)
    return back


def trovaPuntiArticolazione(G):
    tt = [0 for _ in G]  # array dei tempi di inizio visita
    C = [0]  # contatore dei nodi visitati
    A = set()  # insieme dei punti di articolazione
    dfsPA(G, 0, tt, C, A)
    return A


def dfsPAAtoB(G, a, b, tt, C, A):
    C[0] += 1
    tt[a][0] = C[0]
    back = C[0]
    children = 0
    for adjacent in G[a]:
        if tt[adjacent][0] == 0:
            children += 1
            bc = dfsPAAtoB(G, adjacent, b, tt, C, A)
            if tt[a][0] > 1 and bc >= tt[a][0] and tt[b][0] > tt[a][0] and tt[b][1] <= tt[a][1]:
                A.add(a)
            back = min(back, bc)
        else:
            back = min(back, tt[adjacent][0])
    return back


def trovaPuntiCriticiAtoB(G, a, b):
    tt = [[0, 0] for _ in G]  # array dei tempi di inizio visita
    C = [0]  # contatore dei nodi visitati
    A = set()  # insieme dei punti di articolazione
    dfsPAAtoB(G, a, b, tt, C, A)
    return A


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

print(trovaPuntiArticolazione(grfNonDirCicl))
print(trovaPuntiCriticiAtoB(grfNonDirCicl, 0, 4))
