z=int(input())
sum=0
temp=z
while(temp>0):
    c=temp%10
    sum=sum+c**3
    temp=temp//10
if(z==sum):
    print("yes")
else:
    print("no")