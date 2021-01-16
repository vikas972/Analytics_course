# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:39:32 2021

@author: vikas.maurya
"""
'''
Module 4–Introduction to NumPy, Pandas& Matplotlib
Case StudyDomain –
Educationfocus –Data analysisBusiness challenge/requirementYou are a data analyst with
University of Cal USA (Not a machine learning expert yet as you still have not completed
 ML with Python Course :-)).
 The University has data of Math, Physics and Data Structure  score of sophomore students.
 This data is stored indifferent files. The University has hired a data science company to
 do analysis of scores and find if there is any correlation ofscore with age, ethnicity etc.
 Before the data is given to the company you have to do data wrangling.
 Key issuesEnsure students identify is not revealed   to the agency and only relevant data
 is sharedConsiderationsNONEData volume-In thousands, but only around 1800 records are shared
 in files MathScoreTerm1.csv DSScoreTerm1.csv, PhysicsScoreTerm1.csvAdditional 
 information-NABusiness benefitsUniversity can get more students enrollment by improving its 
 international ranking throughpersonalized course/curriculum for students.
 Approach to Solve
 You have to use fundamentals of Numpy and Pandas covered in module4. 
 1.Read the three csv files which contains the score of same students in term1 for each 
 Subject.
 2.Remove the name and ethnicity column (to ensure confidentiality)
 3.Fill missing score data with zero
 4.Merge the three files
 5.Change Sex(M/F) Columnto 1/2 for further analysis
 6.Store the data in new file –ScoreFinal.csv
 
 Enhancements for codeYou can try these enhancements in code
 1.Convert ethnicity to numericalvalue
 2.Fill the missing score for a student tothe
 average of the class
 
 '''
 
import pandas as pd
import numpy as np
 
filePath1="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\DS_mod4_tcwlr\\DS_mod4\\MathScoreTerm1.csv"
filePath2="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\DS_mod4_tcwlr\\DS_mod4\\PhysicsScoreTerm1.csv"
filePath3="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\DS_mod4_tcwlr\\DS_mod4\\DSScoreTerm1.csv"


mathsdf=pd.read_csv(filePath1)
physicsdf=pd.read_csv(filePath2)
Dssdf=pd.read_csv(filePath3)



col_rem=["Name","Ethinicity"]
rmmathsdf=mathsdf.drop(col_rem,axis=1)

df = mathsdf.replace(np.nan, 0)



import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the three csv files which contains the score of same students in term1 for each Subject
df_math_scores = pd.read_csv(filePath1)
df_ds_score = pd.read_csv(filePath2)
df_physics_score = pd.read_csv(filePath3)

print(df_math_scores.head())
print(df_ds_score.head())
print(df_physics_score.head())


# 2. Remove the name and ethnicity column (to ensure confidentiality)
del df_math_scores["Name"]
del df_math_scores["Ethinicity"]

del df_ds_score["Name"]
del df_ds_score["Ethinicity"]

del df_physics_score["Name"]
del df_physics_score["Ethinicity"]

print(df_math_scores.head())
print(df_ds_score.head())
print(df_physics_score.head())


# 3. Fill missing score data with zero
df_math_scores.fillna(0)
df_ds_score.fillna(0)
df_physics_score.fillna(0)

print(df_math_scores.head())
print(df_ds_score.head())
print(df_physics_score.head())


# 4. Merge the three files
merged_df = df_math_scores.merge(df_ds_score, on="ID", suffixes=(
    '_math', '_ds')).merge(df_physics_score, on="ID", suffixes=('_ds', '_physics'))

merged_df_filter_cols = merged_df.filter(["ID", "Score_math", "Score_ds", "Score", "Age_math"]).rename(
    columns={"Score": "Score_physics", "Age_math": "Age"})

print(merged_df_filter_cols)


# 5. Change Sex(M/F) Columnto 1/2 for further analysis

merged_df["Sex"] = [1 if sex ==
                                "M" else 2 for sex in merged_df["Sex"]]
print(merged_df)


# 6. Store the data in new file –ScoreFinal.csv
merged_df.to_csv("ScoreFinal.csv")



 #Enhancements for codeYou can try these enhancements in code
 #1.Convert ethnicity to numerical value
mathsdf=pd.read_csv(filePath1)
physicsdf=pd.read_csv(filePath2)
Dssdf=pd.read_csv(filePath3)

#mathsdf['Ethinicity'] = [1 if ethi == "White American" else  2 for ethi in mathsdf['Ethinicity']]
 

change_m=mathsdf.Ethinicity.astype("category").cat.codes
change_p=physicsdf.Ethinicity.astype("category").cat.codes
change_d=Dssdf.Ethinicity.astype("category").cat.codes

#2.Fill the missing score for a student to the average of the class

avgM=df_math_scores["Score"].mean()
avgd=df_ds_score["Score"].mean()
avgp=df_physics_score["Score"].mean()

avg_Maths=df_math_scores.fillna(avgM)
avg_ds=df_ds_score.fillna(avgd)
avg_ph=df_physics_score.fillna(avgp)


