"""
This program  solves  systems of linear equations using the Gaussain Elimination technique and Reduced Row Echelon Form as seen in linear algebra.
The gauss_elimination function inolves making all entries under the major diagonal of the augmented matrix zero and then performing a back
substitution to obtain the vaules of our variables. Similarly, the reduced_row_echelon function makes all entries above and under the diagonal to be
zero, then reduces all entries in the diagonal to 1.
 

"""
# matrix should be given as a list of lists
# b should be given as a list

##Importing the neccessary modules

import Matrix

def gauss_elimination(matrix, b):
    M = matrix
    

# creating my augmented matrix. That is, a matrix which conatains
# both the  original matrix and the solution set.
    a = 0
    for x in M:
        x.append(b[a])
        a += 1

    print("The augmented matrix is")
    
    Matrix.printmatrix(M)

    n = len(M)

    Matrix.downwardElimination(M)   
                
    print("The upper triangular matrix is")
    Matrix.printmatrix(M)
    
#perfroming back substitution
    new_list = [ ]
    for i in range(n):
       new_list.append(0)

    if M[n-1][n-1] != 0 :
            
        new_list[n-1] = float (M[n-1][n] / M[n-1][n-1])

        for i in range(n-1, -1, -1):
            answer = 0
            for j in range(i+1, n):
                answer += float(M[i][j] * new_list[j])
            new_list[i] = float(M[i][n] - answer) / M[i][i]

        solution = [ '%2f' % elem for elem in new_list]
        for i in range(len(solution)):
            solution[i] = float(solution[i])

        print("The solution to this system is")
        
        return solution

    else:
        print("The solution contains a free variable")
        Matrix.printmatrix(M)
