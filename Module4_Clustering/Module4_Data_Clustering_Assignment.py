# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:39:52 2021

@author: vikas.maurya
"""

#Assignment 4:
    
#Statistic Essential for Analytics 
'''
    Question1:
    
    For the below data sets:X = 55.36, 57.75, 55.26, 55.96, 56.66 
    and Y = 55.75, 55.49, 55.12, 54.70, 53.94, 
    Find the covariance to estimate the linear relationship between the two data sets X & Y.
'''

X=[55.36, 57.75, 55.26, 55.96, 56.66]
Y=[55.75, 55.49, 55.12, 54.70, 53.94]
import numpy as np

#According TO column
cov_mat = np.stack((X, Y), axis = 0)  

print(np.cov(cov_mat))

#According To Row
cov_mat1 = np.stack((X, Y), axis = 1)  

print(np.cov(cov_mat1))

#Overall
print(np.cov(X,Y))

print("It is showing negative covariance")

'''   
    
    Question2:Create the Flow Chart of ‘K-mean Clustering’ and ‘Hierarchical Clustering’.
    
'''








