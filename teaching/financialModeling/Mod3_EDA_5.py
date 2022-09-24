from math import exp
from numpy import log, sqrt
import matplotlib.pyplot as plt
import numpy as np

def PlotSeriesAndHist(series, title = 'None'):
    plt.figure(1)
    plt.subplot(221)
    plt.plot(series)
    plt.subplot(222)
    plt.hist(series)
    plt.title(title)
    plt.show()
# what do we understand by transformations?
ts = [i**2 for i in range (1,100)]
transformed_ts = sqrt(ts)
#PlotSeriesAndHist(ts)
#PlotSeriesAndHist(transformed_ts)

ts1 = [exp(i) for i in range(1, 100)]
#PlotSeriesAndHist(ts1)
transform = log(ts1)
#PlotSeriesAndHist(transform)

from scipy import stats
# creating dummy arrays of sample data that is skewed to the left
x = stats.loggamma.rvs(5, size = 500) + 5
#x = np.random.normal(0, 1, 100)
PlotSeriesAndHist(x)

transform = log(x)
PlotSeriesAndHist(transform, "Log Transformed (skewed data)")
PlotSeriesAndHist(np.sqrt(x), "SquareRoot Transformation")

y, l = stats.boxcox(x)
PlotSeriesAndHist(y, "Box-Cox Transformation")
print("Lamda used for transforming my data closest to normal", l)

'''
Box-Cox Transformation (BCT) can be considered as reciprocal, reciprocal square root transform, log transform, 
square root transform or no transform, depending on the value of lambda. 
Play around with lambda = [-1, -0.5, 0., 0.5, 1]
'''








