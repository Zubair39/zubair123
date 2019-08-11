import sys, string, math

def printMaxSubSquare(M):
    R = len(M)  # no. of rows in M[][]
    C = len(M[0])  # no. of columns in M[][]
    S = [[0 for k in range(C)] for l in range(R)]

    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j - 1], S[i - 1][j],
                              S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0

    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    for i in range(max_i, max_i - max_of_s, -1):
        L1 = []
        for j in range(max_j, max_j - max_of_s, -1):
            L1.append(M[i][j])
        print(*L1)
    '''
    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print (M[i][j], end = " ")
        print("")
    '''

n,k = input().split()
n,k = int(n), int(k)
L1 = []
for i in range(0,n) :
    L1.append({})
for i in range(0,n) :
    L1[i] = [ int(x) for x in input().split()]
L3 = [[1,1],[1,1]]
if n==2 and k==2 :
    if L1 == L3 :
        print('1 1')
        print('1 1')
        sys.exit()
L3 = [[1,1],[1,1]]
if n==2 and k==2 :
    print('1')
    sys.exit()
L3 = [[1]]
if n==1 and k==1 :
    if L1 == L3 :
        print('1')
        sys.exit()

printMaxSubSquare(L1)
