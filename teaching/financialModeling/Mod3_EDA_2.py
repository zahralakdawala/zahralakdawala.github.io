import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal
from scipy.stats import norm
from sklearn.neighbors import KernelDensity


def create_distr(N, rseed = 1 ):
    rand =  np.random.RandomState(rseed)
    #randn generates points from N(0, 1²)
    x= rand.randn(N)
    return x

sample = create_distr(1000)
#plt.hist(sample, bins=10, density=True, alpha= 0.5)
#plt.hist(sample, bins=20, density=True, alpha = 0.3)
#plt.hist(sample, bins=3, density=True, alpha = 0.4)
#plt.show()

#Conclusion: the shape of the histogram depends on the number of bins


#Parametric probability
#let's generate a random samle of 1000 observations for N(50, 5^2)
#sample = normal(loc =50, scale = 5, size= 1000)
sample_mean  = 50
sample_std = 5
sample = sample_std*sample +sample_mean
plt.hist(sample, bins =10, density =True)
plt.show()

dist = norm(sample_mean, sample_std)

values = [value for value in range(30,70)]
probabilities = [dist.pdf(value) for value in values]
plt.plot(values, probabilities)
plt.show()

#NON_PARAMETRIC ESTIMATION
N=100
np.random.seed(1)
sample1 = norm(0, 1)
sample2 = norm(5, 1)

X = np.linspace(-5, 10, N)[:, np.newaxis]

#you can use reshape() instead of [:, np.newaxis]
Y = np.concatenate((np.random.normal(0, 1, 30),
                    np.random.normal(5, 1, 70)))[:, np.newaxis]

true_densities = (0.3 * sample1.pdf(X[:, 0]) + 0.7 * sample2.pdf(X[:, 0]))
fig, ax = plt.subplots()
ax.fill(X[:, 0], true_densities, fc='grey', alpha=0.2, label='input distribution')



#instantiate and fit a KDE model (gaussian, exponential, tophat, ...)
kde = KernelDensity(kernel='gaussian', bandwidth = 0.4).fit(Y)
probabilities =np.exp(kde.score_samples(X))
ax.plot(X, probabilities, color= 'red')
plt.show()

#Check out the following website, its pretty cool with an animation of KDE using different kernels, bandwidth and amplitude! https://mathisonian.github.io/kde/
