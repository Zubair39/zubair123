import math
x=int(input())
lis1=list(map(int,input().split()))[:x]
lis1.sort()
p=len(lis1)
b=math.ceil(p/2)
print(b)
