p,q=map(int,input().split())
for s in range(p,q):
  if s>1:
    for i in range(2,s):
      if s%i==0:
        break
    else:
      print(s,end=" ")
