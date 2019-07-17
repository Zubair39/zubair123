x2=list(input())
y1=[]
for j in x1:
   if j not in y1:
      y1.append(j)
if x1==y1:
   print("Yes")
else:
   print("No")
