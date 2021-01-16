# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:17:51 2021

@author: vikas.maurya
"""


'''

Implementation:
    1)Read the data fileand check for any missing values
    2)Change the headers to country and year accordingly.
    3)Cleanse the data if required and remove null or blank values
    4)After the EDA part is done, try to think which algorithm should be applied here.
    5)As we need to make this across years we need to apply PCA first.
    6)Apply PCA on the dataset and find the number of principal components which 
    explain nearly all the variance.
    7)Plot elbow chart or scree plot to find out optimal number of clusters.
    8)Then try to apply K means, Hierarchicalclustering and showcase the results.  
    9)You can either choose to group the countries based on years of data or using the 
    principal components.
    10)Then see which countries are consistent and which are largest importers of the
    good based on scale and position of cluster.
    
    '''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from sklearn.model_selection import train_test_split

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Certification_Project\\574_proj_dataset_v3.0\\Project_Data_1.csv"

data=pd.read_csv(filePath,index_col=0, decimal=",")
datacopy=pd.read_csv(filePath)

data.isna()

data.dropna()

data.fillna(data.mean())




data_for_decomposition = data.iloc[:, 0:]
data_for_decomposition.head()

import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# PCA for dimension reduction
model_pca = PCA(n_components=2)
pca_data = model_pca.fit(data_for_decomposition).transform(
    data_for_decomposition)

new_data = pd.DataFrame(pca_data, columns=["pca_1", "pca_2"])
new_data.index = data.index
new_data.head()




# elbow method to find number of clusers
wcss = []  # wcss - within cluster squared sum of inertia

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++',
                    max_iter=300, n_init=10, random_state=10)
    kmeans.fit(new_data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("wcss")
plt.show()


# It indicates the number of clusters will be 3

# Kmeans Algorithm
kmeans = KMeans(n_clusters=3)
# fir the model
kmeans.fit(new_data)
# clusters centers
print(kmeans.cluster_centers_)

# adding cluster column
new_data["cluster"] = kmeans.labels_
new_data.head()

# plotting the cluster data
sns.lmplot('pca_1', 'pca_2', data=new_data, hue='cluster',
           palette='coolwarm', height=6, aspect=1, fit_reg=False)


# adding cluster column to original data
data["cluster"] = kmeans.labels_


# export data for analysing
new_data.sort_values(["cluster", "pca_1", "pca_2"])
new_data.to_csv("output.csv", index=True)


data.describe()

# Largest Importer and constantly increasing
data.loc["Sierra Leone"]
X = data.loc["Sierra Leone"].index[0:18]
Y = data.loc["Sierra Leone"].values[0:18]

plt.bar(X, Y)
plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

plt.show()


# most consistent
data.loc["Monaco"]
X = data.loc["Monaco"].index[0:18]
Y = data.loc["Monaco"].values[0:18]

plt.bar(X, Y)
plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

plt.show()








