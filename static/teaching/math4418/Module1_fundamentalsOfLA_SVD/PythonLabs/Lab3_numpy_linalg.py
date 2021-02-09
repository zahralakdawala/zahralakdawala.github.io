import numpy as np
# Numpy is the core library for scientific computing in Python.
# It provides a high-performance multidimensional array object, and tools for working with these arrays.
# If you are already familiar with MATLAB, you might find this tutorial useful to get started with Numpy.

# Linear algebra review
print("######################################################")
print("1. ARRAYS")
# u = np.array([1, 2, 3])
# print("Rank-1 array: ", u)
# print("Type of array: ", type(u))
# print("Shape of array: ", u.shape)
# print("Elements of array: ", u[0], u[1], u[2])
# u[0] = 5                    # Change an element of an array
#
# v = np.array([[1], [2], [3]])
# print("Column matrix",v)
# print("Shape of v", v.shape)
#
# b = np.array([[1,2,3],[4,5,6]])    #creating a rank-2 array
# print("Shape of array", b.shape)
# print("Elements of matrix", (b[0, 0], b[0, 1], b[1, 0]))
#
# M = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])
#
# print("Matrix M", M)
# print("Shape/dimension of M", M.shape)
#
# v_single_dim = np.array([1, 2, 3])
# print("Single dimension array", v_single_dim.shape)
# print(v + v)
# print(3 * v)

print("######################################################")
print("2. CONVENIENCE FUNCTIONS FOR CREATING MATRICES/VECTORS")
# a = np.zeros((2, 2))
# print("Initializing a zero matrix")
# b = np.ones((2, 1))
# print(b)
#
# c = np.full((3, 2), 7)
# print("Singe-value matrix", c)
#
# d = np.eye(3)
# print("Identity matrix:", d)
#
# e = np.random.random((2, 2))
# print("Random matrix", e)
#
# # Other ways to create a matrix
# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])
# v3 = np.array([7, 8, 9])
# M = np.vstack([v1, v2, v3])
# print("v1, v2, v3: ", v1, v2, v3)
# print("Stacked matrix M:", M)
# print("M[:2, 1:3]", M[:2, 1:3])

print("######################################################")
print("3. COMPONENT-WISE MULTIPLICATION")
# print(np.multiply(M, v))
# print(np.multiply(v, v))

print("######################################(################")
print("4. TRANSPOSE")
# print("M.v", M.dot(v))
# print("Matrix transpose & shape", M.T, M.T.shape)
# print("Vector transpose & shape", v.T, v.T.shape)

print("######################################################")
print("5. DOT PRODUCT")
# print("v^Tv:", v.T.dot(v))

print("######################################################")
print("6. LINALG LIBRARY OF NUMPY")
# M = np.array([[3, 0, 2],
#               [2, 0, -2],
#               [0, 1, 1]])
# print("M matrix:", M)
# print("Determinant of M", np.linalg.det(M))
# print("Inverse of M", np.linalg.inv(M))

print("######################################################")
print("6. DEFINING FUNCTIONS IN PYTHON")
#def AddVectors(v1,v2):
#   return (v1+v2)
#call the function like this:
#result = AddVectors(v1,v2)
#print(result)

