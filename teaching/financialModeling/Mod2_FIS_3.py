import Bond
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

maturityTime = [3, 5, 10, 14, 20]
yields = [0.0747, 0.08074, 0.08718, 0.09080, 0.1071]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(maturityTime, yields, color = 'red', marker= '*')
plt.plot(maturityTime, yields)
#plt.show()
bonds=[]

# you can initiate 5 instances of CouponBond at 5 different maturity times.
#for i in range(5):
#    bonds.append(Bond.CouponBond(maturityTime[i]))
#or you can do the following:
bonds = [Bond.CouponBond(i) for i in maturityTime]
prices = [bonds[i].ZCB_Annual() for i in range(0,4)]
print("MaturityTime", maturityTime, "\nPRICE",  prices)


# a way to remove the value at index =2 from maturityTime
maturityTime.pop(2)
marketYield = yields.pop(2)

print("Maturity Time", maturityTime, "\nYields ", yields)
ax.scatter(maturityTime, yields, color = 'red', marker= '*')
plt.plot(maturityTime, yields)
plt.show()

interpolatedPrice = np.interp(10, maturityTime, prices)
print("Interpolated price (should be 55.83947769151179):", interpolatedPrice)

spl = CubicSpline(maturityTime, prices, 3)
print("Print to Maturity at 10 years, using Cubic spline: ", spl(10.))

rel_error = (interpolatedPrice- 55.83947769151179)/55.83947769151179
print("Relative Error for prices (%):",rel_error*100 )

interpolatedYield = np.interp(10, maturityTime, yields)
print("\n\nInterpolated yield (should be 0.08718 ):", interpolatedYield)
rel_errorYield = (interpolatedYield- 0.08718)/0.08718
print("Relative Error for yields (%):",rel_errorYield *100)


# yield to maturity is more accurate than price to maturity.
# yield curves are less sensitive to errors in estimation, compared to price curves
# yield curves (maturity time vs yield/rates/spot rates) are the best and most commonly used
# measure for understanding the beahvioural pattern of bonds over different maturity times.


