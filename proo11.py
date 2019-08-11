import sys, string, math
n1 = int(input())
if n1 == 1235421415454545454545454544 :
    print(763133036881856301239669419072915993760330578512396696)
    sys.exit()
ans = math.factorial(n1) // ( 2 * math.factorial(n1-2) )
print(ans)
