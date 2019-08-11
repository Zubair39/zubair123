import sys, string, math
n11,k11 = input().split()
n11,k11 = int(n11), int(k11)
L = [ int(x) for x in input().split()]
for i in range(0,k11) :
    x = 0
    a,b = input().split()
    a,b = int(a), int(b)
    for j in range(a-1,b) :
        x = x ^ L[j]
        #print(L[j],x)
    print(x)
