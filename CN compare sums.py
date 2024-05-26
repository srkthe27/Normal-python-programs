##
##def find_the_larger(n,v):
##    # Write your code here.
##    min1=v[0]
##    sum1=0
##    sum1=sum1+min1
##    sum2=0
##    for i in range(1,len(v)):
##        if (n==1):
##            return 0
##        else:
##
##            if min1<v[i]:
##                sum1=sum1+v[i]
##                min1=v[i]
##            else:
##                if min1==v[i-1]:
##                    sum2=sum2+min1
##                sum2=sum2+v[i-1]
##    if sum1>sum2:
##        print(sum1,sum2)
##        return 0
##    elif sum1==sum2:
##        print(sum1,sum2)
##        return -1
##    else:
##        print(sum1,sum2)
##        return 1
##
##n=4
##a=[1,3,5]
##print(find_the_larger(n, a))
from typing import *

def find_the_larger(n: int, v: List[int]):
    # Write your code here.
    desc,asc=set(),set()
    for i in range(1,n):
        if v[i-1]<=v[i]:
            asc.add(i)
            asc.add(i-1)
        if v[i-1]>=v[i]:
            desc.add(i)
            desc.add(i-1)
    asum,dsum=0,0
    for i in asc:
        asum+=v[i]
    for i in desc:
        dsum+=v[i]
    if asum<dsum:
        return 1
    elif dsum<asum:
        return 0
    else:
        return -1

n=4
a=[1,3,5]
print(find_the_larger(n, a))
