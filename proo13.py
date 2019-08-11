    
import sys, string, math
n11,k11 = input().split()
n11,k11 = int(n11), int(k11)
L = [ int(x) for x in input().split()]
for i in range(0,k11) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(min(L[a-1:b]))
