# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 10:13:27 2022

@author: zahra
"""
import numpy as np

def normwise_Kr(x,y):
    size = np.size(y)
    print(size)
    res=[]
    for i in range(size):
        if (abs(x)>abs(y[i])) :
            res.append( (abs(x)/abs(y[i])+1))
        else :
            res.append((abs(y[i])/abs(x)+1))
    return res


# Condition number of multiplication

x = 3;
y = np.linspace(-20,20, 200) #1 1e5
#print(y)
size = np.size(y)

xdiff = 1e-8;
ydiff = xdiff;

xtilde = x + xdiff;
ytilde = y + ydiff;

changeOutput =[]
changeInputNormwise =[]
changeInputCompwise=[]
approximateConditionNumberNormwise=[]
approximateConditionNumberCompwise =[]
for i in range(size):
    changeOutput.append(np.abs( (x*y[i] - xtilde*ytilde[i]) / (x*y[i]) ))
    changeInputNormwise.append(max(np.abs(x-xtilde),np.abs(y[i]-ytilde[i])) / max(np.abs(x),np.abs(y[i])))
    changeInputCompwise.append(max(np.abs((x-xtilde)/x), np.abs((y[i]-ytilde[i])/y[i])))
    approximateConditionNumberNormwise.append(changeOutput[i] / changeInputNormwise[i])
    approximateConditionNumberCompwise.append(changeOutput[i] / changeInputCompwise[i])

print('Relative input error / relative output error\n\n')
print('Normwise:', approximateConditionNumberNormwise[1])
print('Componentwise:', approximateConditionNumberCompwise[1])


# plot
res = normwise_Kr(x,y)
componentwise_evaluated = [2] * size 
print()
import matplotlib.pyplot as plt
plt.figure()
plt.plot(y, res, label= 'Normwise evaluated')
plt.plot(y, componentwise_evaluated, label= 'Componentwise evaluated')
plt.plot(y, approximateConditionNumberNormwise, label= 'K_r computed')
plt.plot(y, approximateConditionNumberCompwise, label= 'K_r^c computed')

plt.xlabel("y")
plt.ylabel("cond(3y)")
plt.legend(loc=1)
plt.title("Relative output error/relative input error")
plt.savefig("./MultiplicativeConditionNumber.png")


