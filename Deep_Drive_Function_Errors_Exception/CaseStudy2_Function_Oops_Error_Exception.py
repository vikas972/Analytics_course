# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:50:48 2021

@author: vikas.maurya
"""

import numpy as np
import pandas as pd

#Read The file Bank_data.csv
filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Deep_Drive_Function_Errors_Exception\\574_m3_datasets_v3.0\\bank-data.csv"
Bank_data=pd.read_csv(filePath)

Unique_job=Bank_data["job"].unique()

profession=str(input("Enter the profession to be found in data: "))

if profession in Unique_job:
    print("Client is eligible to be approached for marketing campaign")
else:
    print("Not eligible")
    
    
#Enhancement of code
    
Min_age=Bank_data['age'].min()
Max_age=Bank_data['age'].max()

criteria={"min_age_for_loan_eligibility":Min_age,"max_age_for_loan_eligibility":Max_age}

while True:
    input_p=str(input("Enter the Profession for checking: "))
    p=input_p.lower()
    if p in Unique_job:
        print("profession Exist")
    else:
        print("Do not Exist")
    if input_p=="end":
        break