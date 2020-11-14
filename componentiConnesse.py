import simpleStackQueue

'''
Per tenere traccia delle componenti connesse si può usare un array che ad
ogni nodo assegna l'indice della sua componente connessa (gli indici sono determinati dall'ordine con cui sono
trovate le componenti)
'''


def dfsCC(G, node, arrayCc, countComp):
    S = simpleStackQueue.Stack()
    S.push(node)
    arrayCc[node] = countComp
    while S.size() >= 1:
        v = S.top()
        control = 0
        for adjacent in G[v]:
            if arrayCc[adjacent] == -1:
                arrayCc[adjacent] = countComp
                S.push(adjacent)
                control = 1
        if control == 0:
            S.pop()


def CC(G):
    arrayCc = [-1 for _ in G]
    countComp = 0
    for node in G:
        if arrayCc[node] == -1:
            dfsCC(G, node, arrayCc, countComp)
            countComp += 1
    return arrayCc


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
print(CC(graph))


'''
Quindi CC(G) ritorna un array che per ogni nodo di G dà l'indice della sua componente connessa.
Per grafi non diretti ciò è corretto ed è anche efficiente in quanto la complessità è ancora una volta O(n + m).

!!!Per grafi diretti l'algoritmo non determina in generale le componenti fortemente connesse.!!!

'''