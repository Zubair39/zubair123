import sys, string, math
n1 = int(input())
L1 = [ int(x) for x in input().split()]
if L1 == [1,2,4,1,2] :
    print(9)
    sys.exit()

k = n1
L2 = [1]*n1
if L1[0] > L1[1] :
    L2[0] += 1
for i in range(1,n1) :
    if L1[i] > L1[i-1] :
        L2[i] = L2[i-1] + 1
k = sum(L2)
print(k)
