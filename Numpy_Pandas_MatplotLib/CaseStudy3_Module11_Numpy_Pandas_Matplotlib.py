# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:53:44 2021

@author: vikas.maurya
"""

import pandas as pd
import matplotlib.pyplot as plt

'''
Module 4 –Introduction to Numpy, Pandas & Matplotlib

Study1.
'''
'''
1.You are given a dataset, which is present in the LMS, containing the number 
of hurricanes occurring in the United States along the coast of the Atlantic. 
Load the data from the dataset into your program and plot a Bar Graph of the data, 
taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis. 
'''
filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\DS_mod4_tcwlr\\DS_mod4\\Hurricanes.csv"

df = pd.read_csv(filePath)
x=df["Year"]
y=df["Hurricanes"]


plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("Hurricanes")
plt.title("Hurricanes in US")
plt.grid()
#plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()



'''
2.The dataset given, records data of city temperatures over the years’2014 and 2015. 
Plot the histogram of the temperatures over this period for the cities of San Francisco
 and Moscow.
 '''

import numpy as np
 
filePath1="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\DS_mod4_tcwlr\\DS_mod4\\CityTemps.csv"

df1 = pd.read_csv(filePath1)
x=df1.filter(["San Francisco"])
y=df1.filter(["Moscow"])

fig,ax = plt.subplots(1,1)

ax.hist(x, bins = [0,25,50,75,100])
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('SanFrancisco')
ax.set_ylabel('Values')
plt.grid()
plt.show()



fig,ax = plt.subplots(1,1)

ax.hist(y, bins = [0,25,50,75,100])
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('Moscow')
ax.set_ylabel('Values')
plt.grid()
plt.show()


x_san_Francisco=df1.filter(["San Francisco"])
x_mosco=df1.filter(["Moscow"])
plt.hist(x_mosco, len(x_mosco), facecolor='blue', alpha=0.5)
plt.hist(x_san_Francisco, len(x_san_Francisco), facecolor='red', alpha=0.5)

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperatures of Mosco and San Francisco")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()

 
''' 
3.Create csv file from the data file available in LMS which goes by the name 
‘M4_assign_dataset’and read this file into apandas data frame4.
Let the x axis data 
points and y axis data points areX = [1,2,3,4]y = [20, 21, 20.5, 20.8]
5.1: Draw a Simple plot
5.2: Configure the line and markers in simple plot
5.3: configure the axes
5.4: Give title of Graph & labels of x axis and y axis
5.5: Give error bar if  y_error = [0.12, 0.13, 0.2, 0.1]
5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
5.7: Give a font size of 14
5.8: Draw a scatter graph of any 50 random values of x and y axis
5.9: Create a dataframe from following data
'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73], 
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]
'''


import pandas as pd

filePath1="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\os96pz8d4p\\data_file.txt"

df_data_file = pd.read_csv(filePath1)
df_data_file.to_csv("data_file.csv")

# 4. Let the x axis data points and y axis data points are
# X = [1,2,3,4]
# Y = [20, 21, 20.5, 20.8]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X = [1, 2, 3, 4]
Y = [20, 21, 20.5, 20.8]

# 1. Draw a Simple plot
plt.plot(X, Y)
plt.show()

#################################################################

# 2. Configure the line and markers in simple plot
plt.plot(X, Y)
plt.grid()
plt.show()

#################################################################

# 3. configure the axes

plt.xlabel("Value")
plt.ylabel("Floats")
plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')  # Rotate Axis Labels

#################################################################

# 4. Give title of Graph & labels of x axis and y axis
plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#################################################################

# 5. Give error bar if  y_error = [0.12, 0.13, 0.2, 0.1]
y_error = [0.12, 0.13, 0.2, 0.1]

plt.plot(X, Y, y_error)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#################################################################

# 6. define width, height as figsize=(4,5) DPI and adjust plot dpi=100
plt.figure(figsize=(4,5),dpi=100)

#################################################################

# 7. Give a font size of 14
plt.rcParams.update({'font.size': 14})

#################################################################

# 8. Draw a scatter graph of any 50 random values of x and y axis
x = np.random.random(50)
y = np.random.random(50)

plt.scatter(x, y)
plt.show()

#################################################################

# 9. Create a dataframe from following data
# 'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
# 'female': [0, 1, 1, 0, 1],
# 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, 2, 3],
# 'postTestScore': [25, 94, 57, 62, 70]
# Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

plt.scatter(df["preTestScore"], df["postTestScore"])
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()

#################################################################

# 10. Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore
# with the size = 300 and the color determined by sex

df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

x = df["preTestScore"]
y = df["postTestScore"]
colors = df["female"]

plt.scatter(x, y, c=colors, alpha=0.5)
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()



