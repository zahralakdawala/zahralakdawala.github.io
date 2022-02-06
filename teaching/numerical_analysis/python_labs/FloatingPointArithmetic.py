# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:19:28 2022

@author: zahra
"""

# Floating point arithmetic
import numpy as np
import sys

x = 1400000.00
y = 1.4E6
#Is x = y?
x = y
print(x==y)

myNum = 14 
print(myNum)

#An integer can be converted to a float using the float constructor
myNum = float(myNum)
print(myNum)

print("\nBe careful: Using (In-)Equalities using floating point numbers can be dangerous.")
x=0.1
y =0.2
z =0.3
print((x+y)==z)

print("0.1 = {0:.52f}".format(0.1))
print("0.2 = {0:.52f}".format(0.2))
print("0.3 = {0:.52f}".format(0.3))


#multiplying "zero" a hundred thousand times is not zero
print("\nMultiplication of a value repeatedly by zero is not necessarily a  zero.")
print(np.sin(np.pi))
print(1e5*np.sin(np.pi)) 

res = np.sin(np.pi)
for i in range(0,10):
    res = 10*res
    print(i, res)

#subtracting numbers of almost the same size is usually not a good idea
print("\nBe careful: Subtracting numbers of almost the same size/magnitude")
print(1.000000000001- 1)

print("\nBe careful: Adding numbers of largely different magnitudes")
#neither is adding numbers of very different size
res = np.sqrt(1e-15 + 1) -1
print(res)
res = np.sqrt(1e-16 + 1) - 1
print( res)
print("res = {0:.52f}".format(res))


# unit round 
print("\nMachine level epsilon", sys.float_info.epsilon)
print("Is machine level epsilon really 2^-52 on a 52 digit mantissa? Yes, it is" , 2**(-52))
#print("largest number? ", 2**(52))

#overflow - exceeding the largest float
print("\nUnderstanding overflows")
print("exp(10)", np.exp(10))
print("exp(100)", np.exp(100))
print("exp(1000)", np.exp(1000))

#underflow - exceeding the smallest float
print("\nUnderstanding underflows")
print("exp(-10)", np.exp(-10))
res = np.exp(-100)
print("exp(-100)", res, "res = {0:.52f}".format(res))
res = np.exp(-1000)
print("exp(-1000)", res, "res = {0:.52f}".format(res))

'''
#exceptions
print(0/0)
print(0*np.Inf)
print(np.Inf-np.Inf)
print(np.exp(np.Inf))
print(np.exp(-np.Inf))
print(np.sin(np.Inf))
'''

#rounding and trunction results in noise/errors (small scale)
def my_func(x):
    y = -1 + 3*x - 3*x*x + x*x*x
    return y

#x = np.linspace(0.998, 1.002, 150)
x = np.linspace(0.99998, 1.00002, 150)
y = my_func(x)


import matplotlib.pyplot as plt
plt.figure()
plt.plot(x, y, "*", label= 'Noisy y')
plt.show()
