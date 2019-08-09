chatr1=int(input())
gr=[]
dog=0
for h in range (0,chatr1+1):
    dog=abs((2**h)-chatr1)
    gr.append(dog)
kall=min(gr)
print(kall)
