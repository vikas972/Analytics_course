# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:37:47 2021

@author: vikas.maurya
"""

'''    Assignment 5:
    
    Statistic Essential for AnalyticsQuestion1:
        
    An employee is asked to calculate the
    chi-square value, for company data set for which observed frequency is 9.5 and
    expected frequency is 19.What will be the Chi-Square value?
    
   
    '''
    print(" chi-Square=(obeserved-expected)^2 / Expected")
    ob=9.5
    ex=19
    c_sq=pow(ob-ex,2)/ex
    print("Chi-square = ",c_sq)
    

    
    '''
    Question2:In a Railway Station frequency of trainsis observedfor 2 hrs, the observed
    frequency is found to be 6 trains per hr and expected frequency should be 8 trains per
    hr. What will be the Chi-Square valuefor the observation?
    
    '''
    ob_train=6
    ex_train=8
    chi_sq=pow(ob_train-ex_train,2)/ex_train
    print("Chi-square = ",chi_sq)
    
    print("It is observd for 2 hours hence, chi_square = ",2*chi_sq)