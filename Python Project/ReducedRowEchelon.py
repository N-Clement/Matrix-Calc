# matrix should be given as a list of lists
# b should be given as a list

##Importing the neccessary modules
import Matrix

def reduced_row_echelon(matrix, b):
    M = matrix
   
    a = 0
    for x in M:
        x.append(b[a])
        a += 1
    print("The augmented matrix is")
    Matrix.printmatrix(M)

    #Performing the downward elimination procedure
    n = len(M)
    Matrix.downwardElimination(M) 

    print("The upper triangular matrix is")
    Matrix.printmatrix(M)

#performing upward elimination 
    temp = []
    for w in range(len(M) - 1, 0, -1):
        pivotPosition = 0
        
        # Determining the pivot on the given row
        for j in range(len(M[w]) - 1):
            if M[w][j] != 0:
                pivotPosition = j
                break

        if pivotPosition != 0 and M[w][pivotPosition] != 0:
                # Making sure the pivot is one
                if M[w][pivotPosition] != 1:
                    factor = M[w][pivotPosition]
                    for h in range(len(M[w])):
                        M[w][h] = M[w][h] / factor
                for i in range(w - 1, -1, -1):
                    if M[i][pivotPosition] != 0:
                        factor = M[i][pivotPosition] / M[w][pivotPosition]
                        for j in range(len(M[i])):
                            M[i][j] = M[i][j] - factor * M[w][j]
        temp.append(M[w])

    pivotPosition = -1
    for j in range(len(M[0]) - 1):
        if M[0][j] != 0:
            pivotPosition = j
            break
    if pivotPosition != -1 and M[0][pivotPosition] != 1:
        factor = M[0][pivotPosition]
        for h in range(len(M[w])):
            M[0][h] = M[0][h] / factor

    temp.append(M[0])
    temp.reverse()

    
    print("The reduced echelon form is")
    Matrix.printmatrix(M)

    solution = [ ]
    for i in range(len(temp)):
        solution.append(temp[i][-1])

    solution = [ '%2f' % elem for elem in solution]
    for i in range(len(solution)):
        solution[i] = float(solution[i])

    print("The solution to this system is")   

    return solution
