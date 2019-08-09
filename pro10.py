chaa1=int(input())
choa=[int(o) for o in input().split(" ")]
chea=0
for p in range(chaa1):
      for g in range(p):
           if(choa[g]<choa[p]):
                chea+=choa[g]
print(chea)
