import numpy as np
from matplotlib import pyplot


if __name__ == '__main__':
    A = np.array([[3,4,4], [4, 3, -4]])
    print(A)
    print(A.shape)
    print("Rank", np.linalg.matrix_rank(A))
    # Factorization of A = U Sigma Vt
    U, Sigma, Vt = np.linalg.svd(A, full_matrices=False, compute_uv=True)
    #print(result)


    print("U", U) #2x2 matrix
    print("Sigma", Sigma) # 2 singular values
    print("Vt", Vt) # 3x3 matrix

    print(np.diag(Sigma))
    A_recreated = np.dot((np.dot(U, np.diag(Sigma))), Vt)
    print(A_recreated)

    pyplot.subplot(321)
    pyplot.imshow(A)
    pyplot.subplot(322)
    pyplot.imshow(A_recreated)
    pyplot.show()

    print("TO: Factorize matrix A by hand to confirm that svd fro numpy was correct")

