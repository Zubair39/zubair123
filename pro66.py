z1=int(input())
flag2=0
if z1>2:
    for i in range(3,int(z1/2)):
        if z1%i==0:
            flag2=1
            print("no")
            break
if flag2==0 or z1==2:
    print("yes")
