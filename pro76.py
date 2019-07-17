z1=int(input())
flag2=0
if(z1>2):
    for i in range(2,int(z1/2)+1):
        if z1%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or z1==2:
    print("no")
