# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:17:32 2021

@author: vikas.maurya
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Unsupervised_Learning\\driver-data.csv"
data = pd.read_csv(filePath)
data.head()



X=data["mean_dist_day"]
Y=data["mean_over_speed_perc"]


kmeans = KMeans(n_clusters=5)

kmeans.fit(data)

kmeans.cluster_centers_

print (kmeans.labels_)
print (len(kmeans.labels_))


print (type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_, return_counts=True)
print(dict(zip(unique, counts)))


# plot the data 
import seaborn as sns
data['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('mean_dist_day', 'mean_over_speed_perc',data=data, hue='cluster',
           palette='coolwarm',size=6,aspect=1,fit_reg=False)



print("Inertia\n")
print(kmeans.inertia_)


