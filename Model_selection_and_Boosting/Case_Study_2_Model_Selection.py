# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:25:27 2021

@author: vikas.maurya
"""
'''
1.Load the data from “glass.csv” and make a bar plot of different types of glasses.
2.Make a train_test split and fit a single decision tree classifier.
3.Make a k-fold split with 3 splits and measure the accuracy score with each split
[Hint:Refer to KFold module under sklearn’s model selection.]
4.Use gridSearchCV from sklearn for finding out a suitable number of estimators for
a RandomForestClassifer alongwith a 10-fold cross validation.
[Hint:Define a range of estimators and feed in range as param_grid]

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split,cross_val_score,KFold,ShuffleSplit,GridSearchCV


filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Model_selection_and_Boosting\\glass.csv"

#Laod the glass.csv using Pandas

Data=pd.read_csv(filePath)

u_t=Data["Type"].unique().shape[0]
print(u_t)

Data.columns

#BarPlot uisng Seaborn
import seaborn as sns
sns.countplot(Data["Type"])
plt.show()

'''
#plot the graph using matplotlib
fig = plt.figure(figsize = (10, 5)) 
plt.bar(Data["Type"],Data["Type"])
plt.xlabel("Type of Glass")
plt.ylabel("Amount")
plt.show()
'''

Data.head(10)

X=Data.iloc[:,0:9]
Y=Data["Type"]

train_x,test_x,train_y,test_y=train_test_split(X,Y,random_state=5,test_size=0.30)


from sklearn.tree import DecisionTreeClassifier 

model=DecisionTreeClassifier()

model.fit(train_x,train_y)

predict=model.predict(test_x)


from sklearn import metrics

print("Root Mean Square Error")
rms = metrics.mean_squared_error(predict, test_y)
print(rms)


print("Accuracy Square")
print(metrics.accuracy_score(predict,test_y))



kf = KFold(n_splits=3)

for train_index, test_index in kf.split(X):
    #rint("TRAIN:", train_x, "TEST:", test_x)
    x_train, x_test = X.loc[train_index], X.loc[test_index]
    y_train, y_test = Y[train_index], Y[test_index]

    model.fit(x_train, y_train)
    predicted = model.predict(x_test)
    print("Accuracy Score : " +
          str(metrics.accuracy_score(predicted[0:], y_test.values)))


print(cross_val_score(model, X, Y, cv=3, scoring="accuracy").mean())


from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_jobs=-1, max_features='sqrt', n_estimators=50, oob_score=True)

parameter_candidates = [{1}, {2}]

param_grid = {
    'n_estimators': [100, 200],
    'max_features': ['auto', 'sqrt', 'log2']
}

CV_rfc = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5)
CV_rfc.fit(X, Y)
print(CV_rfc.best_params_)


rf_model = RandomForestClassifier(
    n_jobs=-1, max_features='auto', n_estimators=100, oob_score=True)

print(cross_val_score(rf_model, X, Y, cv=10, scoring='accuracy'))








