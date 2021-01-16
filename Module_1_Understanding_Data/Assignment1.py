# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:49:19 2020

@author: vikas.maurya
"""

#Assignment 1:Statistic Essential for Analytics

"""
Question1:
Guess the Dependent and Independent variable from the below statement.A study is conducted
on new born babies to investigate the association between gestational age at birth (measured
in weeks),and birth weight (measured in grams). We wish to estimate the association between
gestational age and infant birth weight."""


#Infant Birth Weight always be dependant on the Gestational age.Since as Gestational age change then infant weight will change.
# and Gestational age is independent variable 
print("Independent Variable"+"= "+"Gestational age")

print("Dependent Variable"+"= "+"infant Birth Weight")

'''
Question2:
    
Perform the following simple Statistic operations.
Find the mean, median, variance, standard deviation, range of the sets of numbers below:
•76, -56,28,101,8, -24,47,98,15, -39
•3,12,15,8.9,23,0.78,18,45,0,86,7,6.9,5,35,20
•2/5,6/5,25/5,33/12,89/7,23/4,63/33,6/3

'''
set_of_numbers=[76,-56,28,101,8,-24,47,98,15,-39]
set_of_numbers1=[3,12,15,8.9,23,0.78,18,45,0,86,7,6.9,5,35,20]
set_of_numbers2=[2/5,6/5,25/5,33/12,89/7,23/4,63/33,6/3]

print(sum(set_of_numbers1))
def mean(a):
    l=len(a)
    total=sum(a)
    m=total/l
    return m
    
def median(a):
    a.sort()
    l=len(a)
    r=l//2
    if(l%2 != 0):
        return a[r]
    else:
        return (a[r-1]+a[r])/2

print(mean(set_of_numbers))
print(median(set_of_numbers))
print(mean(set_of_numbers1))
print(median(set_of_numbers1))
print(mean(set_of_numbers2))
print(median(set_of_numbers2))

#using Numpy
import numpy as np

print(np.mean(set_of_numbers))
print(np.median(set_of_numbers))
print(np.var(set_of_numbers))
print(np.std(set_of_numbers))
print(max(set_of_numbers)-min(set_of_numbers))

print(np.mean(set_of_numbers1))
print(np.median(set_of_numbers1))
print(np.var(set_of_numbers1))
print(np.std(set_of_numbers1))
print(max(set_of_numbers1)-min(set_of_numbers1))


print(np.mean(set_of_numbers2))
print(np.median(set_of_numbers2))
print(np.var(set_of_numbers2))
print(np.std(set_of_numbers2))
print(max(set_of_numbers2)-min(set_of_numbers2))



'''
Question3:

Two dice are rolled, find the probability that the sum is:
•equal to 1 
•equal to 4
•less than 13
'''
sample_space=[]
for i in range(1,7):
    for j in range(1,7):
        sample_space.append([i,j])

print(sample_space)
Total=len(sample_space)
        
def prob(s):
    count=0
    for i in range(1,7):
        for j in range(1,7):
            if((i+j) == s):
                count=count+1
    return count


#Equal to 1
ans1=prob(1)
print(ans1/Total)


#Equal to 4
ans2=prob(4)
print(ans2/Total)

ans3=0
#Less than 13
#p(x<13)=p(1<=x<=12)
for i in range(1,13):
    ans3+=prob(i)
print(ans3/Total)
            


    
    
