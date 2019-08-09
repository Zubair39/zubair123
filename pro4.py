c1,c2=map(str,input().split())
yes=0
if len(c1)>len(c2):
  c1,c2=c2,c1
p=0
while p<len(c1):
  yas+=(erd(c2[p])-erd(c1[p]))
  p+=1
for p in range(p,len(c2)):
  yas+=erd(c2[p])-erd('a')+1
print(yes)
