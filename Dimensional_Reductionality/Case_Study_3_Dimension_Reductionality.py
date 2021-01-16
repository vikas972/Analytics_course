# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 21:31:35 2021

@author: vikas.maurya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# Data Collection
filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Dimensional_Reductionality\\breast-cancer-data.csv"
data = pd.read_csv(filePath, index_col=0)
data.head()


df_cancer = data
df_cancer.drop(["diagnosis"], inplace=True, axis=1)
df_cancer.head()


# Data Transformation
model_pca = PCA(n_components = 2)
model_pca.fit(df_cancer)
transformer_data = model_pca.transform(df_cancer)


# New DataFrame
new_df = pd.DataFrame(transformer_data)
new_df.index = df_cancer.index # Setting original Index
new_df.columns = ["PC1", "PC2"] # Changing Column names
new_df["diagnosis"] = data["diagnosis"] # Adding Result column
new_df.head()


#Variance Ratio
print(model_pca.explained_variance_ratio_)