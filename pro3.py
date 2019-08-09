a1,b=input().split()
char=abs(len(b)-len(a1))
for g in range(len(a1)):
  if(len(b)==1 and b[g] in a1):
    break
  if(a1[g]!=b[g]):
    char=char+1
print(char)
