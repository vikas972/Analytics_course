# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:57:53 2021

@author: vikas.maurya
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Supervised_Learning_II\\voice-classification.csv"
data = pd.read_csv(filePath)
data.head()


X = data.iloc[:, :len(data.columns)-1]
Y = data["label"]

train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=10, test_size=0.30)

g_model = GaussianNB()
g_model.fit(train_x, train_y)

predicted_values = g_model.predict(test_x)
metrics.accuracy_score(predicted_values, test_y)
