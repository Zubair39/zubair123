z1=input()
n2=len(z1)
if n2%2!=0:
    z1=z1[:int(n2/2)]+'*'+z1[int(n2/2)+1:n2]
else:
    z1=z1[:int(n2/2)-1]+'**'+z1[int(n2/2)+1:n2]
print(z1)
