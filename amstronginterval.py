import math 
n,m=map(int,input().split())
for i in range(n+1,m):
 temp=i
 arm=i
 p=0
 sum=0
 rem=0
 while i>0 :
  i=i//10
  p=p+1
 while temp>0 :
  rem=temp%10
  sum=sum+math.pow(rem,p)
  temp=temp//10
 if arm==sum :
  print(arm,end=" ")
 else :
  continue
