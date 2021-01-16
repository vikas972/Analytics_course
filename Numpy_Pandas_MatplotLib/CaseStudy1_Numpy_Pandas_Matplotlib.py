# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:33:19 2021

@author: vikas.maurya
"""

#Module 4–Introduction to NumPy, Pandas& Matplotlib

#Case Study1.

'''
Extract data from the givenSalaryGender CSV file and store the data from each column 
in a separate NumPy array
'''
import pandas as pd
import numpy as np

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\574_m4_datasets_v3.0\\SalaryGender.csv"
SalaryGender=pd.read_csv(filePath)

numArray=[group.values for i,group in SalaryGender.groupby(level=0,axis=1)]

'''
2.Find:
    1. The number of men with a PhD 2. The number of women with a PhD 
'''
Men=SalaryGender[(SalaryGender["PhD"]==1) & (SalaryGender["Gender"]==1)]
Count_men_with_PhD=len(Men)

Women=SalaryGender[(SalaryGender["PhD"]==1) & (SalaryGender["Gender"]==0)]
Count_Women_with_PhD=len(Women)

'''
3.Use SalaryGender
 CSV file. Store the “Age” and “PhD” columns in one DataFrame and delete the data of all 
 people who don’t have a PhD 
 '''
 
Salary_col=SalaryGender[["Age","PhD"]]
HavingPhd=Salary_col[SalaryGender["PhD"]==0]

ans=Salary_col.drop(HavingPhd.index, axis=0)
 
 '''
 4.Calculate the total number of people who have a PhD degreefrom
 SalaryGender CSV file.
 '''
 
 count=SalaryGender[SalaryGender["PhD"]==1]
 print(len(count))
 
 SalaryGender.PhD.value_counts()
 
 
 '''
 5.How  do  you  Count  The  Number  Of  Times  Each  Value  Appears  In  An  Array  Of 
 Integers?[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]Answer should be 
 array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1]) which means 0 comes 4 times, 1 comes 2 times, 
 2 comes 1 time, 3 comes 1 time and so on.
 '''
 array=[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
 
 np.asarray(array)
 
 uniqueArray,countA=np.unique(array,return_counts=True)
 
 
 
 
 '''
 6.Create a numpyarray [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) and filter the elements 

greater than 5.
'''

arr=np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])

print(arr[arr<5])

'''
7.Create a numpy array having NaN (Not a Number) and print it.
array([ nan,   1.,   2.,  nan,
3.,   4.,   5.])Print the same array omitting all elements which are nan
    
'''
import numpy
a = numpy.array([numpy.nan, 1,2,numpy.nan,3,4,5])
print(a)
print(a[~numpy.isnan(a)])
'''
8.Create  a  10x10 
 array  with  random  values  and  find  the  minimum  and  maximum values.
 '''
import numpy as np
x = np.random.random((10,10))
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)



 '''
 9.Create a random vector of size 30 and find the mean value.
 '''
 
 import numpy as np
x = np.random.random(10)
print("Original array:")
print(x)
ans=x.mean()
print("mean Value:")
print(ans)
 
 
 '''
 10.Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
 '''
import numpy as np

arr = np.arange(11)

arr[3:9] = np.multiply(arr[3:9],-1)

print(arr)
 
 '''
 11.Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn, 
 2ndcolumn or 3rdcolumn.
 '''
 a = np.array([[9, 2, 3],
           [4, 5, 6],
           [7, 0, 5]])
    
    
 sa0=a[np.argsort(a[:, 0])]
 sa1=a[np.argsort(a[:, 1])]
 sa2=a[a[:,2].argsort()]
 
 
 '''
 12.Create a four dimensions array get sum over the last two axis
 at once.
 
 '''
 arr=np.arange(0,16).reshape(2,2,2,2)
 ans=arr.sum(axis=(2,3))
 print(ans)
 
 
 '''
 13.Create a random array and swap two rows of an array.
 
 '''
my_array = np.arange(12).reshape(3, 4)
print("Original array:")
print(my_array)
#swap column
my_array[:,[0, 1]] = my_array[:,[1, 0]]

#swap row
my_array[[0, 1],:] = my_array[[1, 0],:]

print("\nAfter swapping arrays:")
print(my_array)
 
 
 '''
 14.Create a randommatrix and Compute a matrix rank.
 
 '''
 #method1
 from numpy.linalg import matrix_rank
 array=np.arange(16).reshape(4,4)
 rank=matrix_rank(array)
 print(rank)
 
 #Method2
np_array = np.random.random(16).reshape(2, 2, 2, 2)
print(np_array)

array = np.array([4, 2, 7, 1])
temp = array.argsort()
ranks = np.empty_like(temp)
ranks[temp] = np.arange(len(array))

print(ranks)
 
 
 
# 15.Analyse  various  school  outcomes  in  Tennessee  using  pandas.
# Suppose  you  are  a public   schooladministrator.   Some   schools   in   your
# state   of   Tennessee   are performing  below  average  academically.  Your  superintendent,
# under  pressure from frustrated parents and voters, approached you with the task of understanding
# why  these  schools  are  under-performing.To  improve  school  performance,  you need to
# learn more about these schools and their students, just as a business needs to understand
# its own strengths and weaknesses and its customers. Though you is eager  to  build  an
# impressive  explanatory  model,  you  knowthe  importance  of conducting  preliminary
# research  to  prevent  possible  pitfalls  orblind  spots.  Thus, you engages in a
# thorough exploratory analysis, which includes: a lit review, data collection, descriptive
# and inferential statistics, and data visualization.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns

# Phase 1 -Data CollectionHere  is  a  data  of  every  public  school  in  middle  Tennessee.
# The  data  also  includes various  demographic,  school  faculty,  and  income  variables.
# You  need  to  convert  the data into useful information.
# •Read the data in pandas data frame
# •Describe the data to find more details
filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\574_m4_datasets_v3.0\\middle_tn_schools.csv"

df_school_data = pd.read_csv(filePath)
print(df_school_data.head())
df_school_data.describe()

# Phase 2 -Group data by school ratingsChooses  indicators  that  describe  the  student
# body  (for  example,reduced_lunch)  or school administration (stu_teach_ratio) hoping
# they will explainschool_rating.reduced_lunchis  a  variable  measuring  the  average
# percentage of students per school enrolled in a federal program that provides lunches
# for students from lower-income households. In short,reduced_lunchis a good proxy for
# household income. Isolates‘reduced_lunch’and groups the data by‘school_rating’using
# pandasgroupby method and then usesdescribeon the re-shaped data
df_grouped_data = df_school_data.groupby("school_rating").describe()
print(df_grouped_data.head())

# Phase 3 –Correlation analysisFind the correlation between ‘reduced_lunch’and‘school_rating’.
# The values in the correlation matrix table will be between -1 and 1. A value of -1 indicates
# the strongest possible negative correlation, meaning as one variable decreases the other increases.
# And a value of 1 indicates the opposite.
corrmat = df_grouped_data.corr()
print(corrmat)
f, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(corrmat, ax=ax, cmap="YlGnBu", linewidths=0.1)

# Phase 4 –Scatter PlotFind the relationship betweenschool_ratingandreduced_lunch, Plot a graph
# with the two variables on a scatter plot. Each dot represents a school. The placement of the
# dot represents that school's rating (Y-axis) and the percentageof its students on reduced
# lunch    (x-axis).    The    downward    trend    line    shows    the    negative
# correlation betweenschool_ratingandreduced_lunch(as one increases, the other decreases).
# The slope of the trend line indicates how muchschool_ratingdecreases asreduced_lunchincreases.
# A  steeper  slope  would  indicate  that  a  small  change inreduced_lunchhas  a  big  impact
# onschool_ratingwhile  a  more  horizontal  slope would  indicate  that  the  same  small  change
# inreduced_lunchhas  a  smaller  impact onschool_rating

plt.scatter(df_school_data["school_rating"], df_school_data["reduced_lunch"])
plt.grid()
plt.xlabel("Rating")
plt.ylabel("Reduced lunch")
plt.title("School rating vs Reduced lunch")
plt.show()
 
 
# Phase 5 –Correlation MatrixAn efficient graph for assessing relationships is the 
# correlation matrix, as seen below; its  color-coded  cells  make  it  easier  to 
# interpret  than  the  tabular  correlation  matrix above. Red cells indicate positive 
# correlation; blue cells indicate negative correlation; white cells indicate no correlation.
# The darker the colors, the stronger the correlation (positive or negative) between those 
# two variables. Draw a graph of correlation matrix having all important fields of data frame
 
  
 
import matplotlib.pyplot as plt

plt.matshow(df_school_data.corr())
plt.show()

''' 
rs = np.random.RandomState(0)
df = pd.DataFrame(rs.rand(10, 10))
corr = df.corr()
corr.style.background_gradient(cmap='coolwarm')
 '''
 
 
 
 
 
 
 
 
 
 
 
 
 
 