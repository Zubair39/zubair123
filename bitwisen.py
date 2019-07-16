s1,r2=map(int,input().split())
s1=s1^r2
r2=r2^s1
s1=s1^r2
print(s1,r2)
