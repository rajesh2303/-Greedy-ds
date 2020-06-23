"""k-th prime factor of a given number
Given two numbers n and k, print k-th prime factor among all prime factors of n. For example, if the input number is 15 and k is 2, then output should be “5”. And if the k is 3, then output should be “-1” (there are less than k prime factors).
[11:00 am, 21/06/2020] +91 88389 41811: Input : n = 225, k = 2        
Output : 3
Prime factors are 3 3 5 5. Second
prime factor is 3."""


import math
def kthprime(n):
    li=[]
    while n%2==0:
        n=n//2
        li.append(2)
    for i in range(3,n//2,+2):
        cnt=0
        while(n%i==0):
            n=n//i
            li.append(i)
    if n!=1:
        li.append(n)
    return li
li=kthprime(int(input("Enter n:")))
li.insert(0,-1)
k=int(input("Enter K:"))
if len(li)<=k:
    print("Kth position factor is:",-1)
else:
    print("Kth position factor is:",li[k])
