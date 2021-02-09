# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:38:56 2021

@author: zahra
"""


import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as plt
# write here some useful notes

#date format ('YYYY-MM-DD')
start = '2019-01-01'
end = '2020-01-01'

df = web.DataReader(['MSFT'], 'yahoo', start , end)
print(df.head())

stock_price = df['Adj Close']
n = stock_price.size
print(n)
x=np.linspace(0, 1, n)
plt.plot(x, df['Adj Close'], label = 'AAPL Price')


#df = web.DataReader(['AAPL, IBM'], 'yahoo', start, end)['Adj Close']
'''

df = web.DataReader(['AAPL', 'IBM'], 'yahoo', start , end)

print(df.head())
'''