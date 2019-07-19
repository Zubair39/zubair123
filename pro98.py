z1=int(input())
d2=list(map(int,input().split()))
for q in range(len(d2)-1):
     if(d2[q]>d2[q+1]):
           print(q)
           break
