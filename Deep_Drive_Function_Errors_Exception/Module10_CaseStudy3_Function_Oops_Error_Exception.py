# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 11:52:49 2021

@author: vikas.maurya
"""
import pandas as pd

filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Deep_Drive_Function_Errors_Exception\\574_m3_datasets_v3.0\\FairDealCustomerData.csv"

FairDeal=pd.read_csv(filePath)


df = pd.read_csv(filePath,header=None)


df[1] = df[1]+df[0]
del df[0]
#str.strip() is similar to trim
fairCustList = list(df[df[2]==0][1].str.strip())
blockcustlist= list(df[df[2]==1][1].str.strip())
fairCustList



'''
class Customer:
    title = ""
    fname = ""
    lname = ""
    isblacklisted = 0;

    def __init__(self):
        self.title = ""

    def __str__(self):
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted

    def setIsblacklisted(self,isblacklisted):
        self.isblacklisted = isblacklisted

    def isblacklisted(self):
        return self.isblacklisted

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setFname(self,fname):
        self.fname = fname

    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname = lname

    def getLname(self):
        return self.lname

'''
import re
title,fname,lname=map(str,fairCustList[0].split())

l=list(map(str,re.split('[ ]',fairCustList[0])))

class customer:
    customers = []
    def __init__(self,custlst):
        self.customers = custlst
    def __del__(self):
        self.customers =[]
    def IsFair(self,name):
        if name in self.customers:
            print('{0} is a fair customer'.format(name))
        else:
            raise Exception
    def createOrder(self,name,productName,productCode):
        if name in self.customers:
            print('{0} is a fair customer'.format(name))
            order1=Order(productName,productCode)
            order1.eligibleOrder(name)
        else:
            raise Exception


class Order:
 
    def __init__(self,productName,productCode):
        self.productName=productName
        self.productCode=productCode
    def eligibleOrder(self,name):
        if name in self.customers:
            print('{0} is a fair order'.format(name))
        else:
            raise Exception
    
try:
    fr = customer(fairCustList)
    fr.IsFair(input('Enter Customer Name for an Order:'))
#     print(fr.customers)

except:
    print('Sorry!!Input Customer is a blacklisted.')



