a,e=input().split()
char=abs(len(ee)-len(a))
for g in range(len(a)):
  if(len(ee)==1 and ee[e] in a):
    break
  if(a[g]!=ee[g]):
    char=char+1
print(char)
