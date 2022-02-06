# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:18:30 2022

@author: zahra
"""

import numpy as np
import matplotlib.pyplot as plt
import math

import numpy as np
import matplotlib.pyplot as plt
import math


def function1(x):
    return np.exp(x)

#variant 1
def Polynomial(x, degree):
    polynomial =0
    for i in range(degree+1):
        term = x**i/math.factorial(i)
        polynomial = polynomial + term
    y = function1(x)
    error = y - polynomial 
    return polynomial, error

x = np.linspace(-1, 1, 15)
y = function1(x)
print("Range/Array in x-axis", x)
p1, e1 = Polynomial(x, 1)
p2, e2 = Polynomial(x, 2)
p3, e3 = Polynomial(x, 3)
p4, e4 = Polynomial(x, 4)
plt.figure()
plt.plot(x, p1, label= 'P1')
plt.plot(x, p2, label= 'P2')
plt.plot(x, p3, label= 'P3')
plt.plot(x, p4, label= 'P4')
plt.plot(x, y, label='f(x)')
plt.legend()

plt.show()

plt.plot(x, e1, label= 'e1')
plt.plot(x, e2, label= 'e2')
plt.plot(x, e3, label= 'e3')
plt.plot(x, e4, label= 'e4')
plt.legend()

#Can you implement the 'recurive' and 'nested multiplication' variant yourself? 
def Polynomial_v2(x, degree):
    #polynomial  = a0 + a1x 
    #power = x
    #for j=2:n
    #   power = x*power
    #   poly = poly + aj*power
    polynomial =0
    return polynomial

def Polynomial_v3(x, degree):
    #polynomial  = an 
    #for i=n-1:0
    #   polynomial = a_i + x*polynomial
    #   i= i-1
    polynomial =0
    return polynomial

'''
Verify that v3 is best in terms of operation count
#How to: On paper, one counts the number of operations
#On python: one way is to track time for each variant
 - that gives you a notion of measuring performance
 
'''