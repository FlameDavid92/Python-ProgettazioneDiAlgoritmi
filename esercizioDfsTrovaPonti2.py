'''
Discussione dell'esercizio [strade critiche]
Possiamo rappresentare la rete viaria con un grafo G non diretto in cui i nodi sono gli incroci e due nodi sono
collegati da un arco se c'è una strada che collega i corrispondenti incroci. Per ipotesi G è un grafo connesso. Una
strada critica corrisponde a un ponte del grafo G. Per trovare tutti i ponti, un algoritmo molto semplice consiste
nell'esaminare ogni arco {u, v} considerando il grafo G' che si ottiene rimuovendo l'arco da G e controllare se G' è
connesso (se non lo è, l'arco è un ponte, altrimenti non è un ponte). Ma l'algoritmo è molto inefficiente, infatti
richiede m visite di grafi che sono quasi uguali a G e quindi ha complessità O(m(n + m)).

Possiamo fare di meglio?
Possiamo tentare di usare una DFS opportunamente modificata per trovare i ponti.
Supponiamo di fare una DFS, a partire da un nodo qualsiasi, del nostro grafo connesso G.
Sappiamo che tutti gli archi saranno classificati o come archi dell'albero della DFS o come archi all'indietro.
Un arco all'indietro può essere un ponte? No, perché sappiamo che ogni arco all'indietro appartiene
ad almeno un ciclo e un ponte non può far parte di cicli.
Quindi rimangono solamente gli archi dell'albero. Sia {u, v} un arco dell'albero e supponiamo,
senza perdita di generalità, che u sia il padre di v.
Sia Tree(v) l'insieme dei nodi del sottoalbero della DFS da v. Se c'è un arco all'indietro da un nodo di
Tree(v) verso u o un antenato di u, allora l'arco {u, v} non è un ponte (perchè c'è un ciclo che contiene l'arco).
Viceversa, se non c'è un arco all'indietro da Tree(v) a u o un antenato di u? Supponiamo per assurdo che esista un
cammino che collega u e v e che non contiene l'arco {u, v}. Allora sia z il primo nodo del cammino (percorrendolo
da v verso u) che non è in Tree(v). E sia w il predecessore di z, sempre nel cammino, quindi w è in Tree(v). Ne segue
che {w, z} è un arco da Tree(v) a un nodo fuori di Tree(v) per cui non può essere un arco dell'albero e deve
necessariamente essere un arco all'indietro, in contraddizione con l'ipotesi che tali archi non ci sono.

Quindi per determinare se un arco è un ponte basterà controllare che sia un arco dell'albero della DFS e che non ci
siano archi all'indietro dal sottoalbero di un estremo dell'arco all'altro estremo o un suo antenato. Per fare questo
controllo facciamo in modo che la funzione che esegue la DFS da u ritorni il minimo tra il tempo d'inizio visita di u e
il tempo di inizio visita dei nodi antenati di u relativi agli archi all'indietro da Tree(u). Inoltre dobbiamo passargli
anche il padre di u per evitare che scambi l'arco tra u e il padre di u per un arco all'indietro.

'''


def dfsPonti(G, u, z, tt, C, Pt):
    C[0] += 1
    tt[u] = C[0]
    back = C[0]
    for adjacent in G[u]:
        if tt[adjacent] == 0:
            b = dfsPonti(G, adjacent, u, tt, C, Pt)
            if b > tt[u]:  # è un arco ponte
                Pt.append({u, adjacent})
            back = min(back, b)
        elif adjacent != z:
            back = min(back, tt[adjacent])
    return back


def trovaPonti(G):
    tt = [0 for _ in G]   #array dei tempi di inizio visita inizializzato a 0
    C = [0]  #contatore dei nodi visitati
    Pt = []  #lista dei ponti
    dfsPonti(G, 0, 0, tt, C, Pt)
    return Pt

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

print(trovaPonti(grfNonDirCicl))

print(trovaPonti(grfDirCicl))
