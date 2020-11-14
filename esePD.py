import collections


def EQ_BIP(S, x):
    if x % 2 != 0:
        print("Il valore totale della sequenza è dispari, la sequenza non è bipartibile!")
        return False, None
    T = [[False for _ in range(0, int(x/2)+1)] for _ in range(0, len(S))]
    for i in range(0, len(S)):
        T[i][0] = True
    for c in range(1, int(x/2)+1):
        if S[0] == c:
            T[0][c] = True
        else:
            T[0][c] = False
    for i in range(1, len(S)):
        for c in range(1, int(x/2)+1):
            T[i][c] = T[i-1][c]       #Se la sottosequenza con somma c non include S[i]
            if c-S[i] >= 0:
                T[i][c] = T[i-1][c] or T[i-1][c-S[i]] #Se la sottosequenza con somma c può includere S[i]
    return T[len(S)-1][int(x/2)], T


def printSeqFromT(T, S, x):
    i = len(S)-1
    c = x
    L = collections.deque()
    while c > 0 or i > 0:
        if (c-S[i]) >= 0 and T[i-1][c-S[i]]:
                L.appendleft(S[i])
                print("ho inserito " + str(S[i]))
                c = c-S[i]
                print("è rimasto "+str(c))
                i = i - 1
        else:
            L.appendleft(-1)
            i = i - 1
    return L


S = [1, 1, 1, 4, 2, 3, 11, 3]
tot = 0
for el in S:
    tot += el

Tup = EQ_BIP(S, tot)
T = Tup[1]
if Tup[0]:
    L = printSeqFromT(T, S, int(tot/2))
    print(L)




