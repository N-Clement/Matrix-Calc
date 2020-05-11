
def printmatrix(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(round(M[i][j],4), end="\t")
        print()
    print("\n")


