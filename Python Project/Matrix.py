
def printmatrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(round(M[i][j],4), end="\t")
        print()
    print("\n")


#Performing the downward Elimination procedure. This will eliminate the
# entries below each element in the leading diagonal

def downwardElimination(M):
    n = len(M)

    for i in range(n):
        for j in range(i, n):
            if abs(M[j][i]) > abs(M[i][i]):
               M[i], M[j] = M[j], M[i]

            else:
                pass
        
        for k in range(i+1, n):
            factor = float(M[k][i])/ M[i][i]
            
            for x in range(i, n+1):
                M[k][x] -= factor * M[i][x]
