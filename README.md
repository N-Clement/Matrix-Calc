# Matrix-Calc
Solving systems of linear equation has proven to be a daunting process especially when the number of equations in the system is greater than or equal to four. Procedures such as Gaussian Elimination methods and Reduced Row-Echelon forms have been a great tool for analysing and providing solutions for our systems of equation. However, these processes are daunting as it requires a ton of concentration and brain for computing the desired solution for our system.

This program  solves  systems of linear equations using the Gaussain Elimination technique and Reduced Row Echelon Form as seen in linear algebra. The gauss_elimination function inolves making all entries under the major diagonal of the augmented matrix zero and then performing a back substitution to obtain the vaules of our variables. Similarly, the reduced_row_echelon function makes all entries above and under the diagonal to be zero, then reduces all entries in the diagonal to 1.

N.B: The matrix should be given as a list of lists

for Ax = b
gauss_elimination([A], [b])
reduced_row_echelon([A], [b])
