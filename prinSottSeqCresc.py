# N[i] = numero delle sottosequenze crescenti di S[0..i] che terminano in i


def numSottSeqCresc(S, n):
    N = [0 for _ in range(0, n)]
    N[0] = 1
    nsc = 1
    for i in range(1, n):
        N[i] = 1
        for j in range(0, i):
            if S[j] < S[i]:
                N[i] = N[i] + N[j]
        nsc = nsc + N[i]
    return nsc

def printModSeq(S,C):
    stringa = "( "
    for x in range(0, len(S)):
        if C[x] == 1:
            stringa += str(S[x])+" "
    print(stringa+")")

def arrModSeq(S,C):
    arr = []
    for x in range(0, len(S)):
        if C[x] == 1:
            arr.append(S[x])
    return arr

def printFullT(T):
    for indice in range(0, len(T)):
        print("T["+str(indice)+"] = ", end='')
        for stsq in T[indice]:
            print(str(stsq)+" ", end='')
        print("\n")


def printTH(Tt, h):
    print("T[" + str(h) + "] = ", end='')
    for stsq in Tt:
        print(str(stsq) + " ", end='')
    print("\n")


def printSottSeqCresc(S, n, T):
    for x in range(n-1, -1, -1):
        T[x].append([S[x]])
        for y in range(x+1, n):
            if S[y] > S[x]:
                for seq in T[y]:
                    A = [S[x]]
                    for elem in seq:
                        A.append(elem)
                    T[x].append(A)
        print("T[" + str(x) + "] è: " + str(T[x]))
    print("\n")
    for x in T:
        for sottosequenza in x:
            print( sottosequenza, end=' ')


S1 = [5, 7, 3, 6]
print(numSottSeqCresc(S1, len(S1)))
S2 = [5, 3, 7, 8, 6]
print(numSottSeqCresc(S2, len(S2)))
S3 = [8, 1, 2, 9]
print(numSottSeqCresc(S3, len(S3)))

T = [[] for _ in S3]
printSottSeqCresc(S3, len(S3), T)
T = [[] for _ in S2]
printSottSeqCresc(S2, len(S2), T)

