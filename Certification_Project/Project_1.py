# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:16:52 2021

@author: vikas.maurya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams


filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Certification_Project\\uv2towea1d\\OnlineNewsPopularity.csv"

data=pd.read_csv(filePath)

expla=data.describe()

X=data.iloc[:,1:60]
Y=data["shares"]

cor=X.corr()
import seaborn as sns
sns.heatmap(cor)
rcParams['figure.figsize'] = 20, 20


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y=train_test_split(X,Y,random_state=5,test_size=0.20)

model=LinearRegression()

model.fit(train_x,train_y)

predict=model.predict(test_x)



predict = predict.astype(int)


from sklearn import metrics
metrics.accuracy_score(predict,test_y)

test_y.shape
predict.shape


metrics.mean_squared_error(predict, test_y)

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, Y, cv=5)

# Plotting predicted and test data
plt.scatter(predict, test_y)
plt.show()


print("Data is not correlated,quality of the data is very bad")

