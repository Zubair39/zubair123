a,b=map(int,input().split())
for c in range(a,b):
  if c>1:
    for i in range(2,c):
      if c%i==0:
        break
    else:
      print(c,end=" ")
