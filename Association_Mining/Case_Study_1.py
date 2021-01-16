# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:07:17 2021

@author: vikas.maurya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances


filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Association_Mining\\BX_books_book_ratings_users\\BX-Book-Ratings.csv"
df_ratings  = pd.read_csv(filePath, encoding="latin1")
df_ratings.sort_values(["user_id", "isbn"], inplace=True)
df_ratings = df_ratings.head(10000)
df_ratings.reset_index()
df_ratings.head()


from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()
df_ratings["isbn"] = labelencoder.fit_transform(df_ratings["isbn"])
df_ratings.head()

filePath1="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Association_Mining\\BX_books_book_ratings_users\\BX-Books.csv"

df_books = pd.read_csv(filePath1, encoding="latin1", low_memory=False)
df_books.head()


filePath2="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Association_Mining\\BX_books_book_ratings_users\\BX-Users.csv"

df_users = pd.read_csv(filePath2, encoding="latin1", low_memory=False)
df_users.head()



n_users = df_ratings["user_id"].unique().shape[0]
print(n_users)

n_books = df_ratings["isbn"].unique().shape[0]
print(n_books)


data_matrix = np.zeros((n_users, n_books))
for line in df_ratings.head().itertuples():
    #print(line)
    data_matrix[line[1]-1, line[2]-1] = line[3]



print(data_matrix.shape)

user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')



def rmse(pred, test):
    pred = pred[test.nonzero()].flatten()
    test = test[test.nonzero()].flatten()
    return sqrt(mean_squared_error(pred, test))


def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        # We use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(
            ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'book':
        pred = ratings.dot(similarity) / \
            np.array([np.abs(similarity).sum(axis=1)])
    return pred

user_prediction = predict(data_matrix, user_similarity, type='user')
book_prediction = predict(data_matrix, item_similarity, type='book')


print("Root mean square error of user prediction")
print(rmse(user_prediction, data_matrix))

print("Root mean square error of book prediction")
print(rmse(book_prediction, data_matrix))
