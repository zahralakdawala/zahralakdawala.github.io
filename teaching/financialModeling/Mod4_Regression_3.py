import pandas as pd
import numpy as np

X1=[25,25,27,30,23,20]
X2=[30,30,21,24,26,28]
X3=[18,30,29,29,24,26]
list_of_tuples = list(zip(X1, X2,X3))
df = pd.DataFrame(list_of_tuples, columns = ['Stock A', 'Stock B', 'Stock C'])

m1= np.mean(X1)
m2= np.mean(X2)
m3= np.mean(X3)

print("Average prices for Stock A, B, C", m1, m2, m3)

m=(m1+m2+m3)/3
print("Overall mean", m)

SSb=6*((m1-m)**2 + (m2-m)**2 + (m3-m)**2)
MSb = SSb/2
print("Sum of squared difference in between samples, MSb", SSb, MSb)

err1 = list(X1-m1)
err2= list(X2-m2)
err3 = list(X3-m3)
err = err1 + err2 + err3
ssw = []
for i in err:
    ssw.append(i**2)
SSw = np.sum(ssw)
MSw = SSw/15
print ("Sum of squared difference in within samples, MSw", SSw, MSw)

F= MSb/MSw
print("FScore", F)

import scipy.stats as stats
print("Scipy.Stats f-score" , stats.f_oneway(X1, X2, X3))

#if our null hypothesis is true, then F-score should be Fisher-distribution (2, 15) degrees of freedom.
from scipy.stats import f
import matplotlib.pyplot as plt
dfk = 2
dfd = 15 #(n-1)*k
x= np.linspace(f.ppf(0.01, dfk, dfd), f.ppf(0.99, dfk, dfd))
fig, ax = plt.subplots(1,1)
y= f.pdf(x, dfk, dfd)
plt.axvline(x=3.68) #cdf value for  0.05
plt.axvline(x=F, label='F-score', color = 'red')
print("Critical value for my hypthesis testing with confidence level%: ", f.pdf(F, dfk, dfd)*100)
#So, you can conclude that you can accept the hypthesis with a 76.94% confidence level.

ax.plot(x, y)
plt.show()
