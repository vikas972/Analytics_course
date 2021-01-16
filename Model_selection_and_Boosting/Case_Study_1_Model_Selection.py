# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:01:17 2021

@author: vikas.maurya
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split,cross_val_score

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Model_selection_and_Boosting\\bio-degradabale-data.csv"

data=pd.read_csv(filePath,sep=';')

data.columns = range(42)
data.head()

X=data.iloc[:,0:41]
Y=data[41]

train_x,test_x,train_y,test_y=train_test_split(X,Y,random_state=5,test_size=.30)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()



model.fit(train_x,train_y)


predict=model.predict(test_x)

from sklearn import metrics

score=metrics.accuracy_score(predict,test_y)
print(score)



cross_score=cross_val_score(model, X, Y, cv=10, scoring='accuracy').mean()

print(cross_score)