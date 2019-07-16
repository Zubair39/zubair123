p1=int(input())
li1=list(map(int,input().split()))[:p1]
li1.sort()
print(*li1,end="")
