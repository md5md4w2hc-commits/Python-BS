r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = [7, 8, 9]

s1 = [1, 2, 1]
s2 = [6, 2, 3]
s3 = [4, 2, 1]

A = []
B = []

A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

dim = 3

# C[i][j] is the dot product of the i'th row of A, and the j'th column of B

for i in range(0, dim):
    for j in range(0, dim):
        for k in range(0, dim):
            C[i][j] += A[i][k] * B[k][j]

print(C)

import numpy

X = numpy.asmatrix(A)
Y = numpy.asmatrix(B)
print(X)
print(Y)
print(X*Y)