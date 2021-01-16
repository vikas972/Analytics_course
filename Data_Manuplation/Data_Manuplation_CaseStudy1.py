# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:41:50 2021

@author: vikas.maurya
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Data_Manuplation\\HollywoodMovies.csv"

df=pd.read_csv(filePath)


'''
Case Study1
From the data provided on Hollywood movies:
'''

'''    
    1.Find the highest rated movie in the“Quest” story type.
'''

higest=df[df["Story"]=="Quest"]["AudienceScore"].max()

higest1=df[df["Story"]=="Quest"]["RottenTomatoes"].max()
higest_rated=df[df["RottenTomatoes"]==higest1]

print(higest_rated)


'''
    2.Find the genre in which there has been the greatest number of movie releases
'''

great=df.groupby("Genre").groups

group=df["Genre"].value_counts()

print(group.keys())


movies=[values for values in great.keys()]

print("Comedy genre the greatest number of movie releases s")



genre_groups = df.groupby("Genre").groups


genre_groups.keys()

plt.bar(genre_groups.keys(), [len(values) for values in genre_groups.values()])
plt.xlabel("Genre")
plt.ylabel("Number of movies")
plt.title("Genre vs Number of Movies")

plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

plt.grid()
plt.show()



'''
    3.Print the names of the top five movies with the costliest budgets.
'''

sorted_df = df.sort_values("Budget", ascending=False)
sorted_df = sorted_df[sorted_df["Budget"] > 0]  # removing nan values

print(sorted_df.head(5))



'''
    4.Is there any correspondence between the critics’ evaluation of a movie and 
    itsacceptance by the public? Find out, by plotting the net profitability of a
    movie against the ratings it receives on Rotten Tomatoes.
'''



plt.scatter(df["RottenTomatoes"], df["AudienceScore"])
plt.xlabel("RottenTomatoes")
plt.ylabel("AudienceScore")
plt.grid()
plt.show()

# Yes there is a relation between them... Critics evaluation and public reponse is direcly propotional
# to each other.


plt.scatter(df["RottenTomatoes"], df["Profitability"])
plt.xlabel("RottenTomatoes")
plt.ylabel("Profitability")
plt.grid()
plt.show()




'''   
    5.Perform Operations on Files
    
    5.1: From the raw data below create a data frame
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
    'age': [42, 52, 36, 24, 73], 'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
    
    5.2: Save the dataframe into a csv file as example.csv
    
    5.3: Read the example.csv and print the data frame
    5.4: Read the example.csv without column headingQuestion
    
    5: Read the example.csv andmake the index columns as 'First Name’ and 'Last Name'
    
    
    5.6:  Print  the  data  frame  in  a  Boolean  form  as  True  or  False.  
    True  for  Null/  NaN values and false for non-nullvalues
    
    5.7: Read the dataframe by skipping first 3 rows and print the data frame
    
    5.8: Load a csv file while interpreting "," in strings around numbers as thousands
    seperators. Check the raw data 'postTestScore' column has, as thousands separator. 
    
    
''' 
    
import pandas as pd

# 5.1
df = pd.DataFrame({'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                   'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
                   'age': [42, 52, 36, 24, 73],
                   'preTestScore': [4, 24, 31, ".", "."],
                   'postTestScore': ["25,000", "94,000", 57, 62, 70]})


# 5.2
df.to_csv("example.csv")
print("*"*20)

# 5.3
df = pd.read_csv("example.csv")
print(df)
print("*"*20)

# 5.4
df_without_header = pd.read_csv("example.csv", header=None)
print(df_without_header)
print("*"*20)

# 5.5
df_with_index = pd.read_csv("example.csv", index_col=[
                            "first_name", "last_name"])
print(df_with_index)
print("*"*20)

# 5.6
boolean_df = df.isnull().any()
print(boolean_df)
print("*"*20)

# 5.7
df_skip_rows = pd.read_csv("example.csv", skiprows=3)
print(df_skip_rows)
print("*"*20)

#5.8
data=pd.read_csv("example.csv", index_col=4).filter(regex='\d{4}')





# 6. Perform Operations on Files
# 6.1: From the raw data below create a Pandas Series 'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'
# a) Print all elements in lower case
# b) Print all the elements in upper case
# c) Print the length of all the elements
# 6.2: From the raw data below create a Pandas Series ' Atul', 'John ', ' jack ', 'Sam'
# a) Print all elements after stripping spaces from the left and right
# b) Print all the elements after removing spaces from the left only
# c) Print all the elements after removing spaces from the right only
# 6.3: - Create a series from the raw data below 'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
# a) split the individual strings wherever ‘_’ comes and create a list out of it.
# b) Access the individual element of a list
# c) Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
# 6.4: Create a series and replace either X or dog with XX-XX
# 'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
# 6.5: Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'
# 6.6:- Create a series and reverse all lower case words 'india 1998', 'big country', np.nan
# 6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.
# '1', '2', '1a', '2b', '2003c'
# 6.8: Create pandas series and print true if value is containing ‘A’
# '1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
# 6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values 'a', 'a|b', np.nan, 'a|c'
# 6.10: Create pandas dataframe having keys and ltable and rtable as below - 'key': ['One', 'Two'], 'ltable': [1, 2] 'key': ['One', 'Two'], 'rtable': [4, 5] Merge both the tables based of key

import pandas as pd
import numpy as np
import re

# 6.1
series_1 = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b',
                      np.nan, 'Car', 'dog', 'cat'])
print(series_1)

# a) Print all elements in lower case
series_lower_cases = [str(ele).lower() for ele in series_1]
print(series_lower_cases)

# b) Print all the elements in upper case
series_upper_cases = [str(ele).upper() for ele in series_1]
print(series_upper_cases)

# c) Print the length of all the elements
print(len(series_1))

#################################################################

# 6.2
series_2 = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
print(series_2)

# a) Print all elements after stripping spaces from the left and right
series_stripped = [str(ele).strip() for ele in series_2]
print(series_stripped)

# b) Print all the elements after removing spaces from the left only
series_lstripped = [str(ele).lstrip() for ele in series_2]
print(series_lstripped)

# c) Print all the elements after removing spaces from the right only
series_rstripped = [str(ele).rstrip() for ele in series_2]
print(series_rstripped)

#################################################################

# 6.3
series_3 = pd.Series(
    ['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(series_3)

# a) split the individual strings wherever ‘_’ comes and create a list out of it.
list_splited = [str(ele).split("_") for ele in series_3]
print(list_splited)

flatten_list = []

# b) Access the individual element of a list
for sublist in list_splited:
    for l in sublist:
        flatten_list.append(l)
        print(l)

# c) Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
print(flatten_list)

#################################################################

# 6.4: Create a series and replace either X or dog with XX-XX
# 'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
series_4 = pd.Series(['A', 'B', 'C', 'AabX', 'BacX',
                      '', np.nan, 'CABA', 'dog', 'cat'])
print(series_4)

series_replace_X = [str(ele).replace(
    "X", "XX-XX").replace("dog", "XX-XX") for ele in series_4]
print(series_replace_X)

#################################################################

# 6.5: Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'
series_5 = pd.Series(['12', '-$10', '$10,000'])
print(series_5)

series_remove_dollar = [str(ele).replace("$", "") for ele in series_5]
print(series_remove_dollar)


#################################################################

# 6.6:- Create a series and reverse all lower case words 'india 1998', 'big country', np.nan
series_6 = pd.Series(['india 1998', 'big country', np.nan])
print(series_6)

print(series_6[::-1])

#################################################################

# 6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.
# '1', '2', '1a', '2b', '2003c'
series_7 = pd.Series(['1', '2', '1a', '2b', '2003c'])
print(series_7)

series_aplha_check = [str(ele).isalnum() for ele in series_7]
print(series_aplha_check)

#################################################################

# 6.8: Create pandas series and print true if value is containing ‘A’
# '1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
series_8 = pd.Series(['1', '2', '1a', '2b', 'America',
                      'VietnAm', 'vietnam', '2003c'])
print(series_8)

series_true_if_contains_A = ["A" in str(ele) for ele in series_8]
print(series_true_if_contains_A)

#################################################################

# 6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values 'a', 'a|b', np.nan, 'a|c'
series_9 = pd.Series(['a', 'a|b', np.nan, 'a|c'])
print(series_9)

series_a_b_c_exists = [1 if re.match(
    "[abc]", str(ele)) else 0 for ele in series_9]
print(series_a_b_c_exists)

#################################################################

# 6.10: Create pandas dataframe having keys and ltable and rtable as below - 'key': ['One', 'Two'], 'ltable': [1, 2] 'key': ['One', 'Two'], 'rtable': [4, 5] Merge both the tables based of key
df1 = pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2]})
df2 = pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})

print(df1)
print(df2)

df_merge = pd.merge(df1, df2, sort=True)
print(df_merge)
