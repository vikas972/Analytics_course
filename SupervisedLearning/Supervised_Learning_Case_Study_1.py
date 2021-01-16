# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:41:21 2021

@author: vikas.maurya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\SupervisedLearning\\voice.csv"

df=pd.read_csv(filePath,header=0)

df.describe()



import seaborn as sns
from sklearn.model_selection import train_test_split # to split the data into two parts
from sklearn import metrics # for the check the error and accuracy of the modelc


from sklearn.linear_model import LogisticRegression

df["label"]=df["label"].map({"male":1,"female":0})



from sklearn.preprocessing import LabelEncoder 
  
le = LabelEncoder() 

df["label"]=le.fit_transform(df["label"])


'''
from sklearn.preprocessing import OneHotEncoder 
from sklearn.compose import ColumnTransformer 
   
# creating one hot encoder object with categorical feature 0 
# indicating the first column 
columnTransformer = ColumnTransformer([('encoder', 
                                        OneHotEncoder(), 
                                        [0])], 
                                      remainder='passthrough') 
  
data = np.array(columnTransformer.fit_transform(df), dtype = np.str) 
'''


X = df.iloc[:,0:19]
Y = df["label"]

train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state = 10, test_size = 0.20) 
ln_model = LogisticRegression()
ln_model.fit(train_x, train_y)

predicted_data = ln_model.predict(test_x)

acc_mod1=metrics.accuracy_score(predicted_data, test_y)


corr = df.corr()

sns.heatmap(corr)
plt.show()

X = X.drop("median",axis=1)
X = X.drop("Q25",axis=1)
X = X.drop("centroid",axis=1)
X = X.drop("dfrange",axis=1)

train_x, test_x, train_y, test_y = train_test_split(X, Y, random_state = 10, test_size = 0.20)

ln_model = LogisticRegression()
ln_model.fit(train_x, train_y)

predicted_data = ln_model.predict(test_x)

acc_mod2=metrics.accuracy_score(predicted_data, test_y)

print("After Identifying the independent column which do not impact on prediction using correlation matrix")
print("We Remove the some column and get the accuracy which is not much different")

print(acc_mod1,acc_mod2)

























