'''
Lab Exercise
1. Pick out the column GM_AC'
2. Compute the mean.
3. Compute sigma
4. Pick out column F_AC
5. Compute the covariance: cov(GM_AC, F_AC)
6. Compute the correlation coefficient using 4. or otherwise
7. plot (t, GM_AC)
'''

import pandas as pd
import scipy as sp


#package for data analysis, tabular data, time-series, matrices, recorded data
dat = pd.read_csv("Stock_Bond.csv", delimiter=',')
#relies on 2 data structures: Series(1d), Dataframe (nd)
import numpy as np
import matplotlib.pyplot as plt

gm_ac = dat['GM_AC']
tenth_column_value = gm_ac[10]
print(gm_ac.dtype)
print(gm_ac, tenth_column_value)
n= gm_ac.size
print("Steps", gm_ac.size, gm_ac)
t = np.linspace(0, 1, n)

#converts the 'dataFrame' to 'ndarray'
plt.plot(t, dat['GM_AC'].values);
plt.plot(t, dat['F_AC'].values);
plt.show()

#covariance and correlation coeff using pandas dat
print("Pandas Covariance", dat['GM_AC'].cov(dat['F_AC']))
#if you use the covariance from numpy, you get a covariance matrix:
print("Numpy covariance cov(X,Y) \n",np.cov(dat['GM_AC'].values,dat['F_AC'].values) )

#For computing correlation, you call it from pandas or also numpy:
corr_np = np.corrcoef(dat['GM_AC'].values,dat['F_AC'].values)
corr_pandas = dat['GM_AC'].corr(dat['F_AC'])
print("Correlation Coeff.(Pandas, Numpy)", corr_pandas, ", ", corr_np)

fig = plt.figure(figsize=(8,4),dpi=200)
ax = fig.add_subplot(111)
ax.scatter(dat['GM_AC'].values, dat['F_AC'].values, color='blue', s=0.05) ;
plt.show()


