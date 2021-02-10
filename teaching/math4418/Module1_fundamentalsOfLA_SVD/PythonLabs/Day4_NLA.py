# #Here we cover the minimum basics of matplotlib functionality, just enough to illustrate how numpy arrays communicate
# # with Matplotlib. Here we show just the basic interactions possible with matplotlib.
# # Do not consider this a comprehensive guide! For more information on matplotlib, visit:
# # https://matplotlib.org/tutorials/index.html
#
import numpy as np
import matplotlib.pyplot as plt
#
print("######################################################")
print("1. INTRO TO MATPLOTLIB")
x=np.arange(1,5)
y=x**3
#plt.plot([1,2,3,4], [1,4,9,16], "go")
plt.plot(x, y,"r*")
plt.title("Cubic Function")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#
A = np.array([[3,4,4], [4, 3, -4]])
print(A)
print("Shape of A", A.shape)
#
#

# #can you find a function to find the norm of x, y and A?
import numpy.linalg as la
print("Norms", la.norm(x), la.norm(A))
# print("Is this a 2-norm? Frobenius norm?")
#
#
#
# #Define 3 points (to form a triangle)
x = [0,0.5,2]
y = [0,1,-1]
plt.plot(x,y, "r*")
plt.show()
#
#
#
#initialize a 2x2 rotation matrix, reflection matrix, reflection against y=x
#for, example theta = 0.5
#RotationMatrix = np.array([], [])

#can you rotate the triangle (3 2-dvectors) using the rotation matrix?

#linear transformation to a geometrical object defined by a n-dimensional set of m vectors
class ImageProcessor:
    def __init__(self, name=""):
        print("Function:ImageProcessor constructor")
        self.imageName = name
        self.image = 0
    def rotate(self, x, y):
        print("Rotate vector")
        x_new = []
        y_new = []
        return x_new, y_new
    def reflect(self, x, y) :
        print("Function:reflect")
        x_new = []
        y_new = []
        return x_new, y_new
    def plotImage(self, x, y):
        print("Function: Plot Image")

myImage = ImageProcessor("Triangle")
x_new, y_new = myImage.rotate(x, y)
B = myImage.rotate(x, y)


#myImage.plotImage(?, ?)
