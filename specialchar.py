zub=input()
o1=0
for i in range(len(zub)):
    if (zub[i].isalpha() or zub[i].isnumeric() or zub[i]==" "):
      continue
    o1=o1+1
else:
    print(o1)
