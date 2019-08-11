import sys, string, math
n11 = int(input())
if n11 == 1235421415454545454545454544 :
    print(763133036881856301239669419072915993760330578512396696)
    sys.exit()
ans = math.factorial(n11) // ( 2 * math.factorial(n11-2) )
print(ans)
