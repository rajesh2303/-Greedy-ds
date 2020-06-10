def LCS(X, Y):
    m = len(X)
    n = len(Y)
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    print(T[m][n])
S1=input("Enter String1 :")
S2=input("Enter String2 :")
LCS(S1,S2)
