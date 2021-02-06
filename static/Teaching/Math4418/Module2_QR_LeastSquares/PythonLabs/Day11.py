import numpy as np
import matplotlib.pyplot as plt
#THIS LAB IS ABOUT LEAST SQUARES PROBLEM AND POLYNOMIAL INTERPOLATION
m = 10
order =3 # order of polynomial
n = order
start = 0
end = 1

#least squares - finding the coefficients of n order polynomial that best fits 'm' data points in 2D
matrix_dim = (m, n)  # nth order  polynomial
x = np.linspace(start, end, m)
print("X values", x)

#generate the y values 'randomly'
np.random.seed(1)
y = np.abs(np.random.randn(m))
print("Y values", y)
#now we have 'm' (x,y) pairs of data points - 2D points

#Lets create the coefficient matrix A using x values for the least squares problem Ac = y

print("Before flip" ,np.vander(x, matrix_dim[1]))
A = np.fliplr(np.vander(x, matrix_dim[1]))
print("A", A)
print("Rank of A", np.linalg.matrix_rank(A))
result = np.linalg.lstsq(A, y, rcond = None)
print("Result of least squares", result)

#Lets name  the results
coefs, residuals, rank , singular_values = np.linalg.lstsq(A, y, rcond=None)
print("C", coefs)
print("Singular Values", singular_values)

#polynomial interpolation
#interpolated curve for plotting!

interp_m = 50
interp_x = np.linspace(start, end, interp_m)
interp_y = np.zeros(interp_m)
for ind, ix in enumerate(interp_x):
    interp_y[ind] = np.sum(coefs * ix ** np.arange(0, n))
plt.figure()
plt.plot(interp_x, interp_y, '-b', label='interp line')
plt.plot(x, y, '*r', label='data points')
plt.xlabel('x value')
plt.ylabel('y value')
plt.title('poly interp demo')
plt.show()
#plt.savefig('poly_fit_demo22.png')

'''
#THINK ABOUT THE FOLLOWING:
#How can you find the distance between each point and the curve
#The entire task was to minimize the euclidean distance (2 norm) between the points and the fitted polynomial.
#How good is your residual? Do we understand what approximations mean - how close your solution is to the 'exact' problem
#all this is understood in terms of error analysis - conditioning of the problem and the numerical stability of the algorithm
'''