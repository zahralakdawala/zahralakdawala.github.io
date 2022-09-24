#extension of pandas library to communicate with the most updated financial data
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
#1. Let's extract Apple Stocks price from Yahoo Finance (could also be Google Finance, Enigma)
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)
df = web.DataReader('AAPL', 'yahoo', start, end)
print(df.head())

#lets now try to extract 'Adj Close' dataframe

close_p = df['Adj Close']
n = close_p.size
print(n)
x= np.linspace(0,1, n)
plt.plot(x, close_p.values, label = 'AAPL')


#rolling mean / return rate of stocks
m_avg =  close_p.rolling(window=10).mean()
plt.plot(x, m_avg, label = 'Moving Average' )
#plt.legend()
plt.show()

returns = close_p/close_p.shift(1) - 1
#plt.plot(x,returns)
#plt.show()


df = web.DataReader(['AAPL', 'IBM', 'MSFT'], 'yahoo', start, end)['Adj Close']
print(df.head())

returns  = df.pct_change()
corr = returns.corr()


print(corr)

plt.scatter(returns.AAPL, returns.IBM)
plt.xlabel('Returns APPL')
plt.xlabel('Returns IBM')
plt.show()

pd.plotting.scatter_matrix(returns, figsize= (10,10))
plt.show()

'''



#Each time series can be modeled as a sequence of random variables, Y1, Y2, ..., YN -
# marginal distribution - pdf/cdf

# 1. Histograms: crude density estimator
def create_distr(N, f =0.3, rseed = 1 ):
    rand =  np.random.RandomState(rseed)
    x= rand.randn(N)
    #print(x)
    index_offset = int(f * N)
    x[index_offset:] += 5
    #print(x)
    return x

x = create_distr(1000)
fig = plt.figure()
hist = plt.hist(x, bins = 10, density =True)

density, bins, patches = hist
print("Density, bins", density, bins)
widths = bins[1:] - bins[:-1]
print("Area under the curve/histogram (we know this should be equal to 1.): ", (density*widths).sum())


# one of the issues of using a histogram as a density estimator, is the choice of your 'bin' size
# can lead to qualitatively diff. features
# For example, if we look at a version of this data with only 20 points, the choice of how to draw the bins can lead to
# an entirely different interpretation of the data. Consider this example:

x= create_distr(20)
bins = np.linspace(-5, 10, 10)

fig, ax = plt.subplots(1, 2, figsize=(12, 4),
                       sharex=True, sharey=True,
                       subplot_kw={'xlim':(-4, 9),
                                   'ylim':(-0.02, 0.3)})

fig.subplots_adjust(wspace=0.05)


for i, offset in enumerate([0.0, 0.6]):
    ax[i].hist(x, bins=bins + offset, density=True)
    ax[i].plot(x, np.full_like(x, -0.01), '|k', markeredgewidth=1)
plt.show()
#
#
# # How do you know which measure/plot coming from the same data is what you want?
# from scipy.stats import norm
# x_d = np.linspace(-4, 8, 20)
# density = sum(norm(xi).pdf(x_d) for xi in x)
#
# plt.fill_between(x_d, density, alpha=0.5)
# plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth=1)
# plt.axis([-4, 8, -0.2, 5]);
# plt.show()
