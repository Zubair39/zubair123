import sys, string, math

n = int(input())
L1 = [ int(x) for x in input().split()]
L2 = []
for i in range(0,n) :
    k = 1
    if L1[i] > 0:
        sign = 1
    else:
        sign = -1
    for j in range(i+1,n) :
        if L1[j] > 0:
            if sign == 1 :
                break
            else :
                k += 1
                sign = 1
        else:
            if sign == -1 :
                break
            else :
                k += 1
                sign = -1
    L2.append(k)
print(*L2)
