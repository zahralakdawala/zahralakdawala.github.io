# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:20:18 2021

@author: zahra
"""
# Import libraries 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Creating vectors X and Y 
#linspace is a  is used to create an evenly spaced sequence in a specified interval.
x = np.linspace(0, 1, 100)
print(x) 
y = np.exp( 2*x)
  
fig = plt.figure(figsize = (10, 5)) 
# Create the plot 
plt.plot(x, y, '*') 


y0 = np.ones(np.size(x))
y1 = 1 + 2*x
y2 = 1 + 2*x + (2*x)*(2*x)/2.
y3 = 1 + 2*x + (2*x)*(2*x)/2. + (2*x)*(2*x)*(2*x)/(3*2.)
y4 = 1 + 2*x + (2*x)*(2*x)/2. + (2*x)*(2*x)*(2*x)/(3*2.) + (2*x)*(2*x)*(2*x)*(2*x)/(4*3*2.)
plt.plot(x, y0, 'b')
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'g')
plt.plot(x, y3, 'y')
plt.plot(x, y4, 'o')

#use for loops 
#for loops in python
y =[]
for i in range(10):
    print(i)

'''
Weekends TODO list:
    1. Install Anaconda  Navigator (https://docs.anaconda.com/anaconda/install/)
    2. Open Anaconda Prompt to install matplotlib and numpy packages via: 
        > pip install matplotlib
        > pip install numpy
    3. Open Spyder, Go to File->Open and chose 'PlottingFunctions.py' file
    4. Press 'Run->Run' to run/execute the script file.
    5. You should be able to view the outputs and plots
'''