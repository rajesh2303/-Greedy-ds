def longestRepeatedSubstring(str): 
    n = len(str) 
    LCSRe = [[0 for x in range(n + 1)]  
                for y in range(n + 1)]
    res = "" 
    res_length = 0 
    index = 0
    for i in range(1, n + 1): 
        for j in range(i + 1, n + 1): 
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)): 
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
                if (LCSRe[i][j] > res_length): 
                    res_length = LCSRe[i][j] 
                    index = max(i, index) 
            else: 
                LCSRe[i][j] = 0
    if (res_length > 0): 
        for i in range(index - res_length + 1,index + 1): 
            res = res + str[i - 1] 
    return len(res) 
for i in range(int(input())):
    n=input()
    if len(n)<=1:
        print("No")
    else:
        c=longestRepeatedSubstring(n)
        res=len(n)-2*c
        if len(n)==res:
            print("No")
        else:
            print("Yes")
