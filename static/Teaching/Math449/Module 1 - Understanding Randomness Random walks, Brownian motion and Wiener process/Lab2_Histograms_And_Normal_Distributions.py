# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:15:56 2021

@author: zahra
"""

import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
# write here some useful notes

#date format ('YYYY-MM-DD')
start = '2017-01-01'
end = '2020-01-01'

df = web.DataReader(['AAPL'], 'yahoo', start , end)
print(df.head())

stock_price = df['Adj Close']
n = stock_price.size
print(n)
x=np.linspace(0, 1, n)
plt.plot(x, df['Adj Close'], label = 'AAPL Price')
plt.clf()
plt.scatter(x, df['Adj Close'] , color='r', s=0.5)

#getting only the info you require for multiple stocks (memory is precious)
stocks = ['TSLA', 'IBM', 'MSFT', 'AAPL']   
df = web.DataReader(stocks, 'yahoo', start, end)['Adj Close']
print( df[:10])
plt.clf()
plt.hist(x=df.AAPL, density=True)

my_array = np.array([[1,2,3], [4,5,6]])
print(" size,  element in the first row, second column of the array", my_array.size, my_array[0][1])

appl_array = np.array(df.AAPL)
mean = np.mean(appl_array)
std = np.std(appl_array)
var = np.var(appl_array)
print("mean, std, var", mean, std, var, std*std, np.power(std, 2.))
print("mean,", mean, df.AAPL.mean())
print("std,", std, df.AAPL.std())

# generation of random numbers
n = np.random.normal(mean, std, 10)
plt.hist(n, density=True, alpha =0.5)


