"""[10:59 am, 21/06/2020] +91 88389 41811: 1) Given a number N, print all the prime factors and their powers. Here N <= 10^18Input : 1000000000000000000
Output : 2  18
         5  18
Explanation: The prime factors of 1000000000000000000
are 2 and 5. The prime factor 2 appears 18 times in 
the prime factorization. 5 appears 18 times."""


import math
def prime(n):
    cnt=0
    while n%2==0:
        n=n//2
        cnt+=1
    if cnt!=0:
        print(2,cnt)
    for i in range(3,n//2,+2):
        cnt=0
        while(n%i==0):
            n=n//i
            cnt+=1
        if cnt!=0:
            print(i,cnt)
    if n!=1:
        print(n,1)
prime(int(input()))
