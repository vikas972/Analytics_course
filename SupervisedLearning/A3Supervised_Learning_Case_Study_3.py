# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:46:17 2021

@author: vikas.maurya
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\SupervisedLearning\\loan_borowwer_data.csv"



from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import seaborn as sns

# Data Collection
df=pd.read_csv(filePath,header=0)

df.describe()

# Data Wrangling
X = df.iloc[:, 2:13]
Y = df["not.fully.paid"]

# Split Data
train_x, test_x, train_y, test_y = train_test_split(
    X, Y, random_state=10, test_size=0.3)

# Model creation and Fitting Model
random_class = RandomForestClassifier()
random_class.fit(train_x, train_y)

# Data Prediction
predicted_values = random_class.predict(test_x)

# Check Accuracy Score
metrics.accuracy_score(predicted_values, test_y)