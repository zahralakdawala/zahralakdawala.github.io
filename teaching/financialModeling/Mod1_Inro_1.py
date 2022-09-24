from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

X= [1., 2., 3., 4.]
print(X)
x=[]

for i in range(10):
    x.append(0.001*i)
    print("Looping % d" % i, x)

# Linear algebra review
print("######################################################")
print("1. ARRAYS")
u = np.array([1, 2, 3])
print("Rank-1 array: ", u)
print("Type of array: ", type(u))
print("Shape of array: ", u.shape)
print("Elements of array: ", u[0], u[1], u[2])
u[0] = 5                    # Change an element of an array

'''
v = np.array([[1], [2], [3]])

print("Column matrix",v)
print("Shape of v", v.shape)

b = np.array([[1,2,3],[4,5,6]])    #creating a rank-2 array
print("Shape of array", b.shape)
print("Elements of matrix", (b[0, 0], b[0, 1], b[1, 0]))

M = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

print("Matrix M", M)
print("Shape/dimension of M", M.shape)
v_single_dim = np.array([1, 2, 3])
print("Single dimension array", v_single_dim.shape)
print(v + v)
print(3 * v)

print("\n#########################################")
print("2. LOOPS, LISTS, AND DICTIONARY COMPREHENSIONS- USE OF *, **")
for i in range(10):
    for j in range(5):
        print("Looping 2 %d" %j)
    print ("Looping % d" %i )

print ("Outside the loop % d" % i)

filled_list = [a * 2 for a in range(10)]
print("List values (a*2)", filled_list)

'''
n=100
x = np.linspace(-0.2, 0.2, n)
y = np.log(1+x)
print(x.size)
print(x)

fig = plt.figure()
ax = plt.axes()
plt.plot(x, x, '-', color = 'red')
plt.plot(x, y , color='blue')
plt.show()

#Exercise 1.1:
value = norm.pdf(x=0.5)
print("pdf for x=1 for std normal distribution", value)


