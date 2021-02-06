import numpy as np
from matplotlib import image
from matplotlib import pyplot

def LossyCompression(image_matrix, k):
    U, S, V = svd(image_matrix)
    rank = len(S)
    print("Rank", rank)
    #if rank < k :
	 #   return image_matrix

    #take columns less than k from U
    truncated_u = U[:,:k]

    # take rows less than k from V
    truncated_v = V[:k,:]

    # build the new S matrix with top k diagonal elements
    truncated_s = np.zeros((k, k), image_matrix.dtype)

    for i in range(k):
    	truncated_s[i][i] = S[i]

    print ("truncated_u shape {0}, truncated_s shape {1}, truncated_v shape {2}".format(
	    truncated_u.shape, truncated_s.shape, truncated_v.shape))

    #compressed/truncated matrix
    return np.dot(np.dot(truncated_u, truncated_s), truncated_v)




def svd(X):
    # Data matrix X, X doesn't need to be 0-centered
    n, m = X.shape
    # Compute full SVD
    U, Sigma, Vh = np.linalg.svd(X,
      full_matrices=False, # It's not necessary to compute the full matrix of U or V
      compute_uv=True)
    return U, Sigma, Vh



if __name__ == '__main__':
    #load image as pixel array

    #data = image.imread('JamesJosephSylvester.jpg')
    #data = image.imread('Coco.jpeg')
    data = image.imread('wallpaper.jpeg')

    # summarize shape of the pixel array
    print("Date type", data.dtype)
    print("Image Size", data.shape)
    #
    # # reshaping image into 2D
    A = data[:, :, 0]
    print("New Image Size", A.shape)
    #
    # display the array of pixels as an image
    pyplot.imshow(A)
    pyplot.title("Original image")
    pyplot.show()
    #
    # #recreating image using SVD results
    U, Sigma, Vh = svd(A)
    A_svd1 = np.dot(np.dot(U, np.diag(Sigma)), Vh)
    #
    pyplot.subplot(321)
    pyplot.imshow(A)
    pyplot.title("Original image")
    #
    pyplot.subplot(322)
    pyplot.title("Fully recreated after SVD")
    pyplot.imshow(A_svd1)
    pyplot.show()
    print("Rank of A",np.linalg.matrix_rank(A))
    #
    # #Transform A with SVD components
    # A_svd = np.dot(U, np.diag(Sigma))
    #
    k = 220
    A_compressed = LossyCompression(A, k)
    print("Shape A", A.shape)
    print("Compressed A", A_compressed.shape)
    #
    pyplot.subplot(323)
    pyplot.title("Fully recreated after SVD")
    pyplot.imshow(A_svd1)
    #
    pyplot.subplot(324)
    pyplot.title("Lossy_Compressed")
    pyplot.imshow(A_compressed)
    name = "Result_" + str(k) +".png"
    image.imsave(name, A_compressed)
    pyplot.show()
    #
