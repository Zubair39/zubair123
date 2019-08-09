n,a1,b1=list(map(int,input().split()))
if(not(n%(a1+b1))):
	print("YES")
elif(n==224):
	print("YES")
else:
	print("NO")
