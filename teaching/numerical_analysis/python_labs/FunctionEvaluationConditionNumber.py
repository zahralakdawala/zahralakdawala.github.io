# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 10:00:59 2022

@author: zahra
"""
'''
Condition number of function evaluation
We approximate the condition number 

   kappa_r = |f'(x)*x / f(x)| 

via 

changeOutput / changeInput
'''
import math


def my_func(x): 
    f = math.log10(x);    
    return f

#evaluation at this point 
x = 0.1

#relative pertubation epsilon
epsilon = 1e-3
xtilde = x*(1+epsilon)

changeInput  = abs( ( xtilde - x ) / x) 
# should be = epsilon, why isn't it?

print("Epsilon: ", epsilon) 
print("Change in input: ",  changeInput)

changeOutput = abs( ( my_func(xtilde)-my_func(x) ) / my_func(x) )
print("Change in Output: ", changeOutput )

approximateConditionNumber = changeOutput / changeInput

print("Condition number = ", approximateConditionNumber)

