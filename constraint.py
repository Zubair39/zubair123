p=int(input())
li=list(map(int,input().split()))[:p]
li.sort()
print(*li,end="")
