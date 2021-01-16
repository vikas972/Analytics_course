# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:33:39 2021

@author: vikas.maurya
"""
'''
Assignment 3:
    Statistic Essential for AnalyticsQuestion1:An employee is asked to test the 
    hypotheses:H0:  μ = 80
    HA:  μ > 80
    with α = 0.05
    After taking a sample, he calculates P-value = 0.312.
    After observing the above data, he makes the following 
    conclusion:  "This sample proves that we accept H0".
    Comment on the conclusion and rewrite it correctly.
    '''
    print("We Know that")
    print("P value <= alpha,reject the null hypothesis.This is strong evidence that the null hypothesis is invalid")
    print("P value >alpha,means the alternate hypothesis is weak,so you do not reject the null and we shoud accept null hypothesis")
    print("If P Value is greater than alpha value then we cannot reject the null hypothesis")
    print("Here,  0.312>0.05 so we should accept null hypothesis")
    print("So Comment is true")
    
    '''
    Question2:An Employee is asked to test a null hypothesis on company’ssales data.
    He calculates a probability of 0.75, but then he realizes it is a two-tailed test 
    and doubles this to get a P-value = 1.500. Is this statement valid? If NOT why?
    '''
    print("Yes this Statement is valid since in two-tailed test we double the probabilty to get the P-value")