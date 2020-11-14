import simpleStackQueue


def dfs(G, u):
    VIS = []
    S = simpleStackQueue.Stack()
    S.push(u)
    VIS.append(u)
    while S.size() >= 1:
        v = S.top()
        check = 0
        for w in G[v]:
            if w not in VIS:
                VIS.append(w)
                S.push(w)
                check = 1
                break
        if check == 0:
            S.pop()
    return VIS


def dfsRecursive(Gr, u):
    def dfsToRec(node):
        VIS.append(node)
        for w in Gr[node]:
            if w not in VIS:
                dfsToRec(w)
        return VIS
    VIS = []
    return dfsToRec(u)


def dfsBool(G, u):
    VIS = [-1 for _ in G]
    S = simpleStackQueue.Stack()
    S.push(u)
    VIS[u] = 0
    while S.size() >= 1:
        v = S.top()
        check = 0
        for w in G[v]:
            if VIS[w] == -1:
                VIS[w] = 0
                S.push(w)
                check = 1
                break
        if check == 0:
            S.pop()
    return VIS


def dfsRecursiveBool(Gr, u):
    def dfsToRec(node):
        VIS[node] = 0
        for w in Gr[node]:
            if VIS[w] == -1:
                dfsToRec(w)
        return VIS

    VIS = [-1 for _ in Gr]
    return dfsToRec(u)


def dfsOpt(G, u):
    VIS = [-1 for _ in G]
    S = simpleStackQueue.Stack()
    S.push((u, 0))
    VIS[u] = 0
    while S.size() >= 1:
        v = S.top()
        check = 0
        for index in range( v[1], len(G[v[0]]) ):
            if VIS[ G[v[0]][index] ] == -1:
                S.pop()
                S.push((v[0], index))
                VIS[G[v[0]][index]] = 0
                S.push((G[v[0]][index], 0))
                check = 1
                break
        if check == 0:
            S.pop()
    return VIS


def dfsTempInFin(Gr, u):
    def dfsToRec(node, C):
        C[0] += 1
        TT[node][0] = C[0]
        for w in Gr[node]:
            if TT[w][0] == 0:
                C[0] = dfsToRec(w, C)
        TT[node][1] = C[0]
        return C[0]

    TT = [[0, 0] for _ in Gr]
    Counter = [0]
    dfsToRec(u, Counter)
    return TT


graph = {
    0: [4],
    1: [2, 4],
    2: [1, 3],
    3: [2, 4, 5],
    4: [0, 1, 3],
    5: [3]}

graph2 = {
    0: [1, 5, 6],
    1: [0, 2, 3, 4, 5],
    2: [1, 3],
    3: [1, 2],
    4: [1, 5],
    5: [0, 1, 4],
    6: [0, 7, 8, 9],
    7: [6],
    8: [6, 9],
    9: [6, 8]}

print(dfs(graph, 0))  # controllo "if w not in VIS:" non efficiente!!!
print(dfsRecursive(graph, 0))  # controllo "if w not in VIS:" non efficiente!!!
print("  -  ")
print(dfsBool(graph, 0))
print(dfsRecursiveBool(graph, 0))
print("  -  ")
print(dfsOpt(graph, 0))
print("  ---  ")
print(dfsTempInFin(graph, 0))
print("  -  ")
print(dfsTempInFin(graph2, 0))

'''
CORRETTEZZA DFS
- Dimostrare che la DFS partendo da un nodo u visita tutti i nodi raggiungibili da u.
    Supponiamo per assurdo che esista un nodo z raggiungibile da u ma che la DFS non visita.
    Siccome z è raggiungibile da u, esiste un cammino u(0), u(1), …, u(k) 
    (se il grafo è diretto, il cammino è orientato)
!!! con u(0) = u e u(k) = z.
    Sia u(i) il primo nodo del cammino che non è stato visitato, chiaramente 0 < i ≤ k.
    Allora, u(i-1) è stato visitato e durante la visita, prima che il nodo u(i-1) sia estratto dallo stack,
    tutti gli adiacenti di u(i-1) devono essere stati visitati.
!!! Siccome u(i) è adiacente a u(i-1), il nodo u(i) deve essere stato visitato 
    in contraddizione con la nostra ipotesi per assurdo.


EFFICIENZA DFS
Per mantenere l'insieme dei nodi visitati possiamo usare un semplice array VIS "booleano"
con un elemento per ogni nodo,inizializzato a -1 e ogni volta che un nuovo w viene visitato 
si pone VIS[w] = 0 . --> Così l'aggiornamento e il test relativo alla visita di un nodo costa tempo costante.

Lo stack può essere facilmente implementato in modo che tutte le operazioni push , top e pop abbiano costo costante.

Se il grafo è rappresentato tramite liste di adiacenza, la scansione degli adiacenti prende tempo costante 
per ogni adiacente considerato.

Ad ogni iterazione del WHILE o viene visitato un nuovo nodo o è estratto un nodo dallo stack.
Poiché ogni nodo è inserito nello stack una sola volta (quando viene visitato), 
il numero di iterazioni del WHILE è al più 2n.

!!!Il numero di operazioni non costanti in una iterazione del WHILE sono solamente le scansioni degli adiacenti 
o in altri termini gli attraversamenti degli archi. Ogni arco è attraversato al più due volte!!! (per grafi diretti
una sola volta).
Quindi gli attraversamenti degli archi costano complessivamente O(m).
!
In totale, la complessità della DFS su un grafo connesso è O(n + m).
In generale, la complessità è O(h + k) dove h è il numero di nodi e k il numero di archi della 
componente connessa del nodo di partenza.
!

La DFS ha complessità ottimale perchè qualsiasi procedura di visita 
deve necessariamente visitare tutti i nodi e gli archi che sono raggiungibili.

[Siccome lo stack delle chiamate ricorsive ha tipicamente una dimensione limitata, 
l'implementazione ricorsiva non è adatta per grafi di grandi dimensioni.]


Albero di visita --> sottografo formato da tutti i nodi visitati assieme agli archi che hanno permesso di visitarli.
Albero  --> grafo connesso e aciclico.

!!! Un grafo non diretto di n nodi è un albero se e solo se è connesso e ha esattamente n - 1 archi. !!!

Un albero è un grafo minimamente connesso, nel senso che ha il numero minimo di archi per renderlo connesso o, 
equivalentemente, che nessun arco può essere eliminato senza sconnettere il grafo.
Gli alberi di visita dipendono dall'ordine con cui i nodi e gli archi vengono visitati.

!!! L'albero della DFS è anche determinato dall'ordine con cui sono scanditi gli adiacenti dei nodi visitati. !!!
Nel caso di grafi diretti l'albero di visita è più propriamente chiamato arborescenza 
per indicare che è un grafo diretto.



'''
