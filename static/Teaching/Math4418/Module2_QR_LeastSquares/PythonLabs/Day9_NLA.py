#IT IS ALL ABOUT MATRIX A. But what the heck is A?
'''
Let's look at a problem formulation for A
Example 1: Covariance matrix
cov(X, Y) = E(X-E(X)) E(Y - E(Y))
What are the properties of a covariance matrix?
pairwise covariances of features from the data matrix X (n samples, m features)
Plus it is square! symmetric! Also covariance is centered around the mean. For simplicity you can assume mean is 0.
Covariance of two features x, y can then be calculated as the dot product of them.
The covariance of the data matrix with all features can be computed as
A=(X^T X)/(n-1)

Example 2: What is your GPS location (x, y) or (x,y,z) given 'm' satellites that are transmitting signals to your location?
do we need to use all the satellites?
does it suffice to use the satellites with the strongest transmission?
better to use those ones for which the GPS location receives the strongest signals?
Hmm, Linear Algebra connection, really? Who would have thought?
So, let's see ....

'''

#principles used: matrix transpose, dot product and matrix multiplication, matrix inverse, unitary matrix
#python blocks: matrix initializations, packages to perform the above operations.
#python advantages: yuo are in control -upto a certain point - numerical errors.
#algorithmic development: different ways of reaching your goal. usually a tradeoff between efficiency and accuracy.
#however do not underestimate the numerical stability of the algorithm itself.


import numpy as np
from matplotlib import pyplot as plt


#Let's construct a 10x10 square matrix (nothign but a matrix initialization)
matrixSize = 10
R = np.random.rand(matrixSize, matrixSize)
A = np.dot(R,R.transpose())

# Eigen decomposition
print("New Image Size", A.shape)
#for eigen decomposition, you need a full rank matrix!
print("Rank", np.linalg.matrix_rank(A))
# Is it a full rank matrix? Does a matrix inverse exist?
eigen_vals, eigen_vecs = np.linalg.eig(A)
#TODO: TRY this with a matrix that is not full rank - can you find the eigen values? Sadly YES! you will be able to find the values.
#however, would they make sense?

# SVD
U, Sigma, Vh = np.linalg.svd(A, full_matrices=False, compute_uv=True)
A_recreated = U.dot(np.diag(Sigma).dot(Vh))
#print(A, A_recreated)

# Relationship between singular values and eigen values:
print("Sigma = eigenvalues (upto what precision)", np.allclose(Sigma, eigen_vals, 10-2)) # True, Really?
#print(eigen_vecs)
X = np.linalg.inv(eigen_vecs)

A_recreated1 = eigen_vecs.dot(np.diag(eigen_vals).dot(X))
print("A recreated (eigen and svd)", np.allclose(A_recreated, A_recreated1, 10-2))

print("Sigma", Sigma,"\n EigenValues" ,eigen_vals)

print(eigen_vals.shape, Sigma.shape)
for i in range(8) :
  print(eigen_vals[i], Sigma[i])


#Hmm, but theoretically we studied that singular values squared = eigen values.
#So, is the theory wrong? or someone forgot to take care of this in implementing it in the numpy package?
# this is what happens when you code, get 'an' answer, looks ok and you do not validate it! UNBELIEVABLE.
# So should we trust numpy.linalg routines - uh, sometimes we have no choice. but sometimes we just dont know. USE IT WITH CAUTION!
#This is why we are here in the course: we know when something is not right.
#However still, the eigenvalues multiplied by coresponding eigenvectors is correct!
#which means you can use the above to solve the system Ax=b!

#So what good are these decompositions/factorizations?
#they help us solve the system Ax =b
#How so?

print("\n\n\nWHAT TO DO WITH DECOMPOSITIONS?")
data = np.array([
  [0.05, 0.12],
  [0.18, 0.22],
  [0.31, 0.35],
  [0.42, 0.38],
  [0.5, 0.49]])
# Lets say we have A and b as a 5x1 matrix, you seek for a point x 1x1 (its a scalar as a solution):
#Note that A is a rank 1  - column matrix
A, b = data[:,0], data[:, 1]
print("Rank", np.linalg.matrix_rank(A))
print("m, n", A.shape, b.shape)
A = A.reshape(len(A), 1)
plt.scatter(A, b)
plt.show()
print(b)

#direct inverse x = A-1*b
#solving using QR decomposition: QRx = b => x = R-1 Q^T b
Q, R = np.linalg.qr(A)
print(Q,R)
x = np.dot(np.linalg.inv(R), (np.dot(Q.T, b)))
print("Solution via QR", x)
print("A_QR", np.dot(Q, R))

#direct inverse x = A-1*b
#solving using SVD decomposition: U Sigma VT x = b => x =  b
U, Sigma, Vh = np.linalg.svd(A, full_matrices=False, compute_uv=True)
print("U", U,"\nSigma", Sigma, "\nVh", Vh)
invD = np.linalg.inv(np.diag(Sigma))  #What is the inverse of a diagonal matrix? tink about computation times!
print("Inverse Sigma", invD)

A_svd = np.dot(U, np.dot(np.diag(Sigma), Vh))
print("A_SVD", A_svd)
pseudoInv = np.dot(Vh.T, np.dot(invD, U.T))
x = np.dot(pseudoInv, b)
print("Solution via SVD", x)

#One is based on diagonalization (SVD), other on orthogonalization (QR)
'''
#more on QR
QR is just a factorization and every matrix can be decomposed into Q and R.
How to get QR? This is algorithmic development - Classical Gram Schmidt, Modified Gram Schmidt, and others!
All are ok conceptually! What algorithm is used in numpy.linalg.qr()? We will talk about this later. 
Classical GS is NUMERICALLY unstable due to error carried forward and projections. Why so? we have already seen a glimpse
Modified GS - gives us a way of computing the r values in a more numerically stable way.   
Can you implement Classical GS, and Modified GS on your own?

'''



