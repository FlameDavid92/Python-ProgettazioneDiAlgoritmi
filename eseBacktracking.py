def printSottSeqCresc(n, X, sol, u, z, check, k):
    if k == n:
        print(sol)
        return
    sol[k] = -1
    printSottSeqCresc(n, X, sol, u, z, check, k+1)
    if X[k] == 0 and check == 0:
        sol[k] = 0
        printSottSeqCresc(n, X, sol, u, z+1, 0, k+1)
    elif X[k] == 1 and z >= (u+1):
        sol[k] = 1
        printSottSeqCresc(n, X, sol, u+1, z, 1, k + 1)


X = [1, 1, 0, 0]
X2 = [0, 1, 0, 1]
sol = [-1 for _ in X]
sol2 = [-1 for _ in X2]
printSottSeqCresc(len(X), X, sol, 0, 0, 0, 0)
print("\n\n")
printSottSeqCresc(len(X2), X2, sol2, 0, 0, 0, 0)

