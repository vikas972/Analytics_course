# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:56:29 2020

@author: Vikas Maurya
"""

#Assignment 2:Statistic Essential for Analytics
'''
Question 1:
In a group of 45 people, 15 are healthy and every person of the remaining 30 has
either high blood pressure, a high level of cholesterol or both. If 17 have high 
blood pressure and 28 have high level of cholesterol:how many people have high 
blood pressure and a high level of cholesterol?If a person is selected randomly 
from this group, what is the probability that he/she
a) has high blood pressure (event A)? 
b) has high level of cholesterol (event B)? 
c) has high blood pressure and high level of cholesterol (event A and B)?
d) has either high blood pressure or high level of cholesterol (event A or B)?
'''
'''

Solution:
    
a) Let x be the number of people with both high blood pressure and high level of cholesterol. Hence (15 - x) will be the number of people with high blood pressure ONLY and (25 - x) will be the number of people with high level of cholesterol ONLY. We now express the fact that the total number of people with high blood pressure only, with high level of cholesterol only and with both is equal to 30.
(17 - x) + (28 - x) + x = 30
solve for x: x = 15
b) 15 have high blood pressure,hence P(A) = 17/45 = 0.378
c) 25 have high level of cholesterol, hence P(B) = 28/45 = 0.622
d) 15 have both,hence P(A and B) = 15/45 = 0.333
e) 30 have either, hence P(A or B) = 30/45 = 0.666
    
e) P(A) + P(B) - P(A and B) = 0.378 + 0.622 - 0.333 = 0.667 = P(A or B)
'''
#Python Code
#a
a=17
b=28
c=a+b
x=c-30
print("People Having both high Blood Pressure and High Level Of Cholesterol",x)

#b
pa=a/(a+b)
print(pa)

#c
pb=b/(a+b)
print(pb)

#d
pa_and_pb=x/(a+b)
print(pa_and_pb)
#e
pa_or_pb=30/(a+b)
print(pa_or_pb)




'''
Question 2:     
Imagine that, while in Mumbai, you also took a side trip to Goa, to pay homage 
to some TV show. Late one night in a hotel you meet a guy who claims to know that
in the casino at the Tito’s street there are two sorts of slot machines: one that 
pays out 10% of the time, and one that pays out 20%of the time. The two types of 
machines are coloured red and blue. The only problem is, the guy did not remember
 which colour corresponds to which kind of machine. Next day you go to the Tito’s
 street to find out more. You find a red and a blue machine side by side. 
 You toss a coin to decide which machine to try first; based on this you then put 
 the coin into the red machine. It doesn’t pay out. How should you update your 
 estimate of the probability that this is the machine you’re interested in? 
 What if it had paid out -what would be your new estimate then?
 '''
 

''' 

Solution:
    
Let P(R) be the probability that the red machine is the one that pays out more often; similarly P(B) = 1 − P(R).

Let P(J) be the probability of payout (“jackpot”).

We are interested in P(R|NJ).

Bayes theorem says

P(R|NJ) = (P(NJ|R)P(R)) / (P(NJ|R)P(R) + P(NJ|B)P(B))

We start with P(R) = P(B) = 0.5. This gives us

P(R|NJ) = 0.8*0.5 / (0.8*0.5 + 0.9*0.5) ≈ 0.47

If the red machine did pay out then we have

P(R|J) = (P(J|R)P(R)) / (P(J|R)P(R) + P(J|B)P(B))

Substituting in...

P(R|J) = 0.2*0.5 / (0.2*0.5 + 0.1*0.5) ≈ 0.66

That is, a pay-out makes you a lot more confident about which is the good machine
than no payout. This makes sense since paying out is a rare event, so you would 
expect it to give you a lot of information.

You may like to take this further by considering how many times you’d have to 
fail to get a payout from the red machine before being say 90% confident it’s 
not that machine. 
 
 '''
 #python Code
 
 
pr=0.5  # probability for choosing Red machine
pb=1-pr # Probabilitu for choosing Blue Machine
pn_jr=0.8 #Probability  red  did not pays out
pn_jb=0.9 # Probability blue Did not pays out

p_jr=1-pn_jr
p_jb=1-pn_jb


prn_j=(pn_jr *pr)/((pn_jr*pr)+(pn_jb*pb))

pr_j=(p_jr *pr)/((p_jr*pr)+(p_jb*pb))





 

 