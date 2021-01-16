# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:29:34 2021

@author: vikas.maurya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\SupervisedLearning\\horse.csv"

df=pd.read_csv(filePath,header=0)

df.describe()


letse=df.isna()

Y = df["outcome"]
X = df.drop(["outcome"], axis=1)


X = pd.get_dummies(X)
X.head()



X = X.apply(lambda x: x.fillna(x.value_counts().index[0]))


from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer


# 4.Fit a decision tree classifier and observe the accuracy.
dec_tree = DecisionTreeClassifier()
dec_tree.fit(X, Y)
predicted_outcome = dec_tree.predict(X)
metrics.accuracy_score(predicted_outcome, Y)

# 5.Fit a random forest classifier and observe the accuracy
random_forest = RandomForestClassifier()
random_forest.fit(X, Y)
predicted_outcome = random_forest.predict(X)
metrics.accuracy_score(predicted_outcome, Y)
