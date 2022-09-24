#Python code for 1-d random walk model
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

dimension = 1
t = 1000
S_t = np.zeros((1, dimension)) #initializes an ndarray using numpy of size (1, dimension)
#print(S_t)

#set the value at the start of the walk
S_t[:1] = 10. # S_0 value

#simulate steps using N(0,1) in 1D => draw out 't' samples from N(0,1)
Z = np.random.normal(loc =0., scale =1., size=(t,dimension))
#Z = norm.rvs(loc=0, scale=1., size=(t,dimension))
#print(Z)

#S_t = (S_0 + Z_1 + Z_2 ....+ Z_t) = rhs
#P_t = exp(r_1+ r_2+ ...)

rhs = np.concatenate([S_t, Z])
normalRandomWalk = rhs.cumsum(0)
#S_0: 1st value of the normalRandomWalk
#S_1: 2st value of the normalRandomWalk
#.
#.
print("normalRandomWalk - values at each S_i", normalRandomWalk)
S_0 = normalRandomWalk[:1]
S_end = normalRandomWalk[-1:]
print("Start and end walker position", S_0, S_end)

fig = plt.figure(figsize=(8,4),dpi=200)
ax = fig.add_subplot(111)
ax.scatter(np.arange(t+1), normalRandomWalk, color='blue', s=0.05) ;
ax.plot(normalRandomWalk, c= 'blue', lw=0.5)
ax.plot(0, S_0, c= 'red' , marker='+')
ax.plot(t, S_end, c='black', marker='o')
plt.title('1d normal random walk')
#plt.show()
plt.savefig("myFirstRandomWalk1")

# What would you expect if the steps are not N(0,1)?
# What modifications are needed to make this into a geometric random walk?
# Enough about random walks! Let's talk about pandas and data analysis

import pandas as pd
#package for data analysis, tabular data, time-series, matrices, recorded data
dat = pd.read_csv("Stock_Bond.csv", delimiter=',')
#relies on 2 data structures: Series(1d), Dataframe (nd)

