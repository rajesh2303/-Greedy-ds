"""[11:00 am, 21/06/2020] +91 88389 41811: Minimum operations to make GCD of array a multiple of k
[11:00 am, 21/06/2020] +91 88389 41811: nput : a = { 4, 5, 6 }, k = 5
Output: 2
Explanation: We can increase 4 by 1 so that it becomes 5 and decrease 6 by 1 so that it becomes 5. Hence minimum operation will be 2."""
import math
print("Enter List :")
li=list(map(int,input().split(" ")))
k=int(input("Enter K value :"))
cnt=0
for i in range(len(li)):
    if li[i]%k!=0:
        cnt+=1
        li[i]=5
if min(li)!=k:
    cnt+=1
print(cnt)
