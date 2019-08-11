import sys, string, math
def count_1(n) :
    s1 = bin(n)[2:]
    k1 = s1.count('1')
    return k1
n = int(input())
L = [ int(x) for x in input().split()]
#L2 = sorted(L, key=count_1,reverse=True)
L2 = []
for i in range(0,n) :
    L2.append((count_1(L[i]),L[i]))
#print(L2)
L3 = sorted(L2, key=lambda x : (x[0],x[1]),reverse=True)
#print(L3)
L4 = [x[1] for x in L3 ]
for i in range(0,len(L4)) :
    print(L4[i])
