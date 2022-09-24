#Let's not loose track. Let's focus on structure and style
#Struggling to scroll up and down to find what you did when?
#Lets talk about CLASS: they encapsulates common utility (functions) for an object (datatype)
'''
Python: programming language (same version of python)
Interpreter: ease of use for progamming in python (Jupyter notepook, Spyder, pycharm, Anaconda)
packages: implemented libraries/utilities for a specific purpose (numpy, matplotlib, scipy.stats)
'''
import numpy as np
import matplotlib.pyplot as plt
#import scipy as sp
from scipy.stats import norm

class NormalDistribution:
    #Reference https://towardsdatascience.com/
    #exploring-normal-distribution-with-jupyter-notebook-3645ec2d83f8
    def __init__(self, mean =0., std = 1.):
        print("NormalDistribution::constructor")
        self.mu = mean
        self.sigma = std
        print("Mu, Sigma", self.mu, self.sigma)

    def reset(self, mean = 0., std = 1.):
        print ("NormalDistribution::reset")
        self.mu = mean
        self.sigma = std

    def computePdf(self, givenX):
        value = norm.pdf(givenX)
        print("I am in NormalDistribution::computePdf()")
        return value

    #\Phi(givenx)
    def computeCdf(self, givenx):
        print("I am in NormalDistribution::computeCdf()")
        value = norm.cdf(x=givenx, loc=self.mu, scale=self.sigma)
        return value

    def Exercise11(self, givenX):
        self.reset(0., 1.)
        value = self.computePdf(givenX)
        print("Computed Value for pdf", value)

    def Exercise12(self, startX=-4., endX=4., startY=0., endY=0.45, mean=0., sigma=1.):
        self.reset(mean, sigma)
        h = (endX - startX)/ 1000.
        x = np.arange(startX, endX, h)
        y= self.computePdf(x)
        #print(x, y)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        # lets refine our view
        ax.set_xlabel('x', fontsize=20)  # set x label
        ax.set_ylabel('pdf(x)', fontsize=20, rotation=90)  # set y label
        #ax.set_ylim(startY, endY)  # range

        xval =1.
        yval = self.computePdf(xval)
        xplot = ax.plot([xval], [yval], marker='o', markersize=15, color="red")  # coordinate point
        plt.show()

    def Exercise31(self):
        # Exercise 3.1 - referring to the lecture notes(slides)
        fig, ax = plt.subplots()
        #generate random normal distribution numbers according to the scale which is standard deviation
        xs = norm.rvs(scale=2, size=1000)
        new_variance = np.var(xs)
        new_mean = np.mean(xs)
        print("Mu, Var", new_mean, new_variance)

        ax = fig.add_subplot(111)
        x = np.linspace(-10, 10, 100)
        y = norm.pdf(x, scale=2)
        ax.plot(x, y, 'r-', lw=2)

        ax.set_xlabel('x')
        ax.set_ylabel('pdf(x)')
        ax.set_title(f'mean={new_mean:.2f}, var={new_variance:.2f}')
        ax.hist(xs, bins=10, alpha=0.5, density=True)
        ax.grid(True)
        plt.show()

class TestingUtility:

    def __init__(self):
        print("TestingUtility::constructor")

    def understandingLog(self, start =-0.2, end=0.2, n =1000):
        x = np.linspace(start, end, n)
        y = np.log(1 + x)
        print(x.size)
        print(x)
        return x, y

    def plotXY(self, X, Y):
        fig = plt.figure()
        ax = plt.axes()
        plt.plot(X, X, '-', color='red')
        plt.plot(X, Y, color='blue')
        plt.show()

print("\n#########################################")
print("INITIATING A CLASS OBJECT, AND CALLING SOME FUNCTIONS")

#variables/data types: int, string, float, TestingUtility
'''
my_test = TestingUtility()
x_array, y_array = my_test.understandingLog(-0.4, 0.4, 10)
my_test.plotXY(x_array, y_array)
'''

my_dist = NormalDistribution()
my_dist.Exercise11(0.5)

my_dist.Exercise12()
my_dist.Exercise31()

#Do it yourself:
#Exercise2.2
#Exercise4.1
