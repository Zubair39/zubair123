it1,new=map(int,input().split())
lil=list(map(int,input().split()[:it1]))
count=0
for i in range(0,it1):
    if(lil[i]==new):
        count=count+1
print(count)
