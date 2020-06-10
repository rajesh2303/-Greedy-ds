def obar1(W, wt, val, n):
    for i in range(w+1):
        for j in range(n+1):
            k[i][j]=0
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w]
    print(K[n][W])
n=int(input("Enter n value"))
wt,val=[],[]
for i in range(n):
    wt.append(int(input("Enter weight:")))
    val.append(int(input("Enter Value:")))
W=int(input("Enter storage Weight"))
obar1(W,wt,val,n)
