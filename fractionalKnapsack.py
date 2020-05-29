n=int(input("Enter Size :"))
li=[]
for i in range(n):
    val=float(input("Enter value :"))
    wei=float(input("Enter Weight :"))
    res=val/wei
    li.append([res,val,wei])
weight=float(input("Enter Knapsack Capacity:"))
li=sorted(li)
li=li[::-1]
profit,i=0,0
while weight>0 and i<n:
    if weight<li[i][2]:
        profit+=li[i][0]*weight
        weight=0
    else:
        profit+=li[i][1]
        weight-=li[i][2]
    i+=1
print("Maximum possible Value :{}".format(int(profit)))
