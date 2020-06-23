"""[11:01 am, 21/06/2020] +91 88389 41811:  Count number of pairs (A <= N, B <= N) such that gcd (A , B) is B
Given a number n. We need find the number of ordered pairs of a and b such gcd(a, b) is b itself
[11:01 am, 21/06/2020] +91 88389 41811: Input : n = 2
Output : 3
(1, 1) (2, 2) and (2, 1)"""

import itertools as iter
import math 
def per(li):
    cnt=0
    for i in iter.permutations(li,2):
        if math.gcd(i[0],i[1])==i[1]:
            cnt+=1
    for i in range(len(li)):
        if math.gcd(li[i],li[i])==li[i]:
            cnt+=1
    print(cnt)
n=int(input("Enter number :"))
li=[]
for i in range(1,n+1,+1):
    li.append(i)
per(li)
