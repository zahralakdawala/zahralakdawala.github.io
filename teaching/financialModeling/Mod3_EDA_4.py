import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot_2samples

def ecdf(data):
    """ Compute ECDF """
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return(x,y)

mu, sigma = 5, 1
# generate random data for ECDF
rand_normal = np.random.normal(mu, sigma, 1000)
x, y = ecdf(rand_normal)
#plt.plot(x,y)
#plt.xlabel('x', fontsize=16)
#plt.ylabel('Fn(x)', fontsize=16)
#plt.show()

mu1, sigma1 = 4, 0.5
rand_normal1 = np.random.normal(mu1, sigma1, 100)
x,y = ecdf(rand_normal1)
#plt.scatter(x=x, y=y, label = 'N(4,0.5)');


mu2, sigma2= 4, 1
rand_normal2 = np.random.normal(mu2, sigma2, 100)
x,y = ecdf(rand_normal2)
#plt.scatter(x=x, y=y, label = 'N(4,1)')

mu3, sigma3 = 4, 2
rand_normal3 = np.random.normal(mu3, sigma3, 100)
x,y = ecdf(rand_normal3)
'''
plt.scatter(x=x, y=y, label ='N(4,2)')
plt.xlabel('x', fontsize=16)
plt.ylabel('Fn(x)', fontsize=16)
plt.legend()
#plt.show()
'''

y0 = np.quantile(rand_normal, .1) # N(5,1)
y1=np.quantile(rand_normal1, .1)  #N(4, 0.5)
y2 = np.quantile(rand_normal2, .1) #N(4, 1)
y3 = np.quantile(rand_normal3, .1) #N(4, 2)
print(".5 sample quantile = 50th percentile (median): ", y1, y2, y3, y0)

#Take your apple stock prices (or better still, returns) to see how the shape of EDF looks like.
#Chances are this will be different from how a normal sampled data looks like
import pandas_datareader as web
import datetime

start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2020, 1, 1)
df = web.DataReader('AAPL', 'yahoo', start, end)
print(df.head())

#lets now try to extract 'Adj Close' dataframe
#"EDF vs CDF"
close_p = df['Adj Close']
n = close_p.size
x1,y1 = ecdf(close_p.values)
plt.scatter(x1,y1)

mu= close_p.mean()
sigma = close_p.std()
sample_normal = np.random.normal(mu, sigma, n)
x,y = ecdf(sample_normal)
plt.plot(x,y, color='red')
plt.xlabel('x')
plt.ylabel('Fn(x)')
plt.title("EDF and CDF for APPL Prices")
plt.show()

returns = close_p/close_p.shift(1) - 1
n = returns.size
x1, y1 = ecdf (returns.values)
plt.scatter(x1, y1, label='returns')

mu = returns.mean()
sigma = returns.std()
sample_normal = np.random.normal(mu, sigma, n)
x,y = ecdf(sample_normal)

plt.plot(x,y, color='orange', label='normal')
plt.xlabel('x')
plt.ylabel('Fn(x)')
plt.title('EDF and CDF for AAPL Returns')
plt.legend()
plt.show()
print("Median for normal/returns - 0.5 quantile:", np.quantile(y, .5), np.quantile(y1, .5))

#=>Central limit theorem says:
#Many estimators have an approximate normal distribution if the sample size is sufficiently large.
#This is true of sample quantiles by the central limit theorem

#How to tell 'how much' do we deviate from the normal distribution?
#=> NORMAL PROBABILITY PLOTS - a graphical technique for assessing whether or not a data set
# is approximately normally distributed. The data are plotted against a theoretical normal
# distribution in such a way that the points should form an approximate straight line.
# qth sample quantile = \mu + \sigma CDF^-1 (q) , for all q less than 1, greater 0

#A quantile-quantile plot, or a Q-Q plot, is a graph comparing two probability distributions
# by plotting their quantiles against each other.

n= returns.size
data_points = np.random.lognormal(mu, sigma, n)
sm.qqplot(data_points, line ='r')
plt.title("QQ Plot for Data points from normal distribution")
plt.show()

sm.qqplot(close_p.values, line ='r')
plt.title("QQ plot for Prices")
plt.show()

sm.qqplot(returns.values, line ='r')
plt.title("QQ plot for Return")
plt.show()

pp_x = sm.ProbPlot(data_points, stats.t, fit =True)
pp_y = sm.ProbPlot(close_p.values)
qqplot_2samples(pp_x, pp_y, xlabel='normal data points', ylabel= 'Prices', line='r')
plt.title('Shape of quantile-quantile plot')
plt.show()

# Let's consider the density estimate
from sklearn.neighbors import KernelDensity
N=100
X = np.linspace(-5, 10, N)[:, np.newaxis]
Y = np.concatenate((np.random.normal(0, 1, 30),
                    np.random.normal(5, 1, 70)))[:, np.newaxis]


#Kernel Density Estimator
kde = KernelDensity(kernel='gaussian', bandwidth = 0.4).fit(Y)
probabilities =np.exp(kde.score_samples(X))

fig, ax = plt.subplots()
ax.plot(X, probabilities, color= 'red')

sm.qqplot(probabilities, line ='r')
plt.show()










