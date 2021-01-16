# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:27:30 2021

@author: vikas.maurya
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df =pd.DataFrame({
        'Student':[1,2,3,4,5,6,7],
        'Aptitude_TestScore':[80,65,86,84,78,76,79],
        'DataScience_Score':[70,70,85,86,60,75,86]
        })

#df=df.drop(["Student"],axis=1)

'''
Assignment 6:Statistic Essential for AnalyticsQuestion1: 
    
    Sevenrandomly selected studentsof Edureka!took a statistics aptitude test 
    before they began their Data Sciencecourse. The Data ScienceDepartment has 
    three questions.
    
    1)What linear regression equation best predicts statistics 
    performance, based on statistics aptitude scores?
    2)If a student made a 75on the aptitude test, what grade would we expect her to
    make in Data Science?
    3)How well does the regression equation fit the data?
    
'''





df.describe()
x_chart=df["Aptitude_TestScore"]
y_chart=df["DataScience_Score"]



plt.plot(x_chart,y_chart,'o')
plt.xlabel("Aptitude_TestScore")
plt.ylabel("DataScience_Score")
plt.show()

#1
print("After anayzing the graph,we can say that data it is not dependent")
print("We Need Multiliner Regression Model to predict or Building the model")

import seaborn as sns
#creating a correlation matrix
correlations = df.corr()
sns.heatmap(correlations,square = True, cmap = "YlGnBu")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()


x = df.iloc[:,0:2]
y=df["DataScience_Score"]

#from sklearn.cross_validation import train_test_split


from sklearn.model_selection import train_test_split
#testing data size is of 33% of entire data
x_train, x_test, y_train, y_test =train_test_split(x,y, test_size = 0.33, random_state =10)



from sklearn.linear_model import LinearRegression
#fitting our model to train and test
lm = LinearRegression()
model = lm.fit(x_train,y_train)

#Equation coefficient and Intercept
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

print('Variance score: {}'.format(lm.score(x_test, y_test))) 


pred=pd.DataFrame({
         'Student':[1,2],
        'Aptitude_TestScore':[75,70]
        })
pred_y = lm.predict(x_test)
print(pred_y)

#2
print("If student scored 75 in the Aptitude_Score then he will score 82 Marks in the Data Science ")



plt.plot(y_test,pred_y,'o')
plt.xlabel("test")
plt.ylabel("pred")
plt.show()

#3
print("The Model fits Very Bad since data is not relvant")


