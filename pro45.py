num1=int(input())
sum=0
if num1>0:
  digit=num1%10
  sum+=digit
  num1=num1//10
print(sum)
