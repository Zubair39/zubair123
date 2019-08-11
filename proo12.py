import sys, string, math
n1,k1 = input().split()
n1,k1 = int(n1), int(k1)
L = [ int(x) for x in input().split()]
for i in range(0,k1) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum(L[a-1:b]))
