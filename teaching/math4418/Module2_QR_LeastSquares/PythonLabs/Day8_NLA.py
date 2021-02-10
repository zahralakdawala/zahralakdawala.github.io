import numpy as np
from matplotlib import image
from matplotlib import pyplot

#QR factorization (default uses LAPACK)


A = np.array([[1, 2, 4],
               [0, 0,5],
               [0, 3, 6]])

#reduced, complete
print("Rank of A",  np.linalg.matrix_rank(A))
orthonormal, upper_triangle = np.linalg.qr(A)
print("Q matrix", orthonormal)
print ("R matrix", upper_triangle)
A_recreated = np.dot(orthonormal,upper_triangle)
print(A_recreated)
#
#
# NOT Always is the QR Factorization so nice (in terms of inteǵer values)
#Try it for:
#A = np.array([[1, -1],
#               [-1, 2],
#               [0, -1]])


# difference between zero (in our heads) and 'numerical zeros' (scientific notation)
epsilon = 1.E-03
# print(epsilon)
#
# print("1+epsilon-sqaured", 1+pow(epsilon, 2))
# epsilon= 1+pow(epsilon, 2)
m = np.array([[1, 1, 1],
                [epsilon, 0, 0],
                [0, epsilon, 0 ],
                [0, 0,  epsilon ]])
# # reduced, complete
orthonormal, upper_triangle = np.linalg.qr(m, 'reduced')
print("Q matrix", orthonormal)
print ("R matrix", upper_triangle)
A_recreated = np.dot(orthonormal,upper_triangle)
print("A-epsilon", m, A_recreated)
#
