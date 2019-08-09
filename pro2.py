from itertools import combinations
N,k=map(int,input().split())
z=len(str(N))
lst=list(combinations(str(N),z-k))
lst=sorted(lst)
print(*lst[0],sep='')
