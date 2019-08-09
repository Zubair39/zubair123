c11,c22=map(str,input().split())
yas=0
if len(c11)>len(c22):
  c11,c22=c22,c11
p=0
while p<len(c11):
  yas+=(ord(c22[p])-ord(c11[p]))
  p+=1
for p in range(p,len(c22)):
  yas+=ord(c22[p])-ord('a')+1
print(yas)
