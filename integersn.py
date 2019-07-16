number3=int(input())
lt=list(map(int,input().split()))[:number3]
lt.sort()
print(*lt,end=" ")
