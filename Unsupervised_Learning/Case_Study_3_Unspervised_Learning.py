# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:45:20 2021

@author: vikas.maurya
"""

from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Unsupervised_Learning\\zoo.csv"
data = pd.read_csv(filePath)
data.head()

# Find Unique class types
unique_classtypes = np.unique(data["class_type"].values)

# Initialize Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=4)
abc=agglo.fit(data.iloc[:,1:17])
predicted_values = agglo.fit_predict(data.iloc[:, 1:17])

# Accuracy Score
print("Accuracy Score")
print(metrics.accuracy_score(predicted_values, data["class_type"].values))

# Mean Square Error value
print("Mean Squared Error value")
print(metrics.mean_squared_error(predicted_values, data["class_type"].values))
