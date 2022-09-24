'''
Exercise 2: Coupon Bonds
1. Implement the function CB_SemiAnnual(...) for computing the bond price
2. Calculate the bond price using:
    c= 40
    T= 30
    par=1000
    r = 0.08 (annual rate, i.e. SemiAnnual rate is 0.04)
3. Now, extend the function such that it takes an array of values for r
    r =  [0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05]
4. plot r vs price
'''

def CB_SemiAnnual(c, T, r, par):
    price = []
    n = 7
    for i in range(8):
        expon = (1 + r[i]) ** (-2 * T)
        price.append(c / r[i] + (par - c / r[i]) * expon)
    return price

c= 40
T= 30
par=1000
r=[0.02, 0.025, 0.03, 0.033, 0.035, 0.04, 0.045, 0.05]
price = CB_SemiAnnual(c,T, r, par)
print("Coupon Rates", r)
print("Market Price", price)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(r, price, color='red', marker='*') ;
#plt.plot(r, bv ,color= 'blue')
plt.show()

#lets fit a curve (cubic spline) on the points {r[i], bv[i]}
#A cubic spline is a spline constructed of piecewise third-order polynomial which pass through a set of m control points.
from scipy.interpolate import CubicSpline
spl = CubicSpline(r, price, 3)
#lets extract the spline value at r = 0.0324
print("Price for yield of r = 0.0324 using CubicSpline", spl(0.0324))
#this should be the bond value/price = 1200  (refer to the example covered in class).
#Cubic spline seems to be a good fit!

#There are other kinds of splines that can be used for interpolation
#depending on the scatter, not all splines/curves are a good fit
#for example, see BSpline (is not the best fit!!)
from scipy.interpolate import BSpline
spl = BSpline(r, price, 2)
print("Price for yield of r = 0.0324 using BSpline", spl(0.0324))
