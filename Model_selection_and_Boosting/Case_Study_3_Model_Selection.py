# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:02:36 2021

@author: vikas.maurya
"""
'''
Questions:
1.The data file contains numerical attributes that describe a letter and its
corresponding class. Read the datafile “letterCG.data” and set all the numerical attributes
 as features.Split the data in to train and test sets.
 
2. Fit a sequence of AdaBoostClassifier
with varying number of weak learners ranging from 1 to 16, keeping the max_depth as 1
Plot the accuracy on test set against the number of weak learners.
Use decision tree classifier as the base classifier.

3.Repeat step2 with max_depth set as 2.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Model_selection_and_Boosting\\letterCG.bin"

data=pd.read_csv(filePath,sep=' ')


data.drop(["Unnamed: 5", "Unnamed: 18", "yegvx"], axis=1, inplace=True)
data.fillna(0)



X=data.iloc[:,1:]
Y=data["Class"]

data.head()



from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=5, test_size=0.30)



base_class = DecisionTreeClassifier(max_depth=1)

ada_Boost = AdaBoostClassifier(
    base_estimator=base_class, n_estimators=400, learning_rate=1, algorithm='SAMME')

ada_Boost.fit(train_x, train_y)
predicted = ada_Boost.predict(test_x)
metrics.accuracy_score(predicted, test_y)

plt.plot(predicted,test_y)
plt.xlabel("predicted")
plt.ylabel("test")
plt.show()

import seaborn as sns
sns.countplot(predicted)

base_class = DecisionTreeClassifier(max_depth=2)
ada_Boost = AdaBoostClassifier(
    base_estimator=base_class, n_estimators=400, learning_rate=1, algorithm='SAMME')

ada_Boost.fit(train_x, train_y)
predicted = ada_Boost.predict(test_x)
metrics.accuracy_score(predicted, test_y)



