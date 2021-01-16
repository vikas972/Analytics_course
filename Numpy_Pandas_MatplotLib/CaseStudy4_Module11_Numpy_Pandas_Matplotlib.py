# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:53:44 2021

@author: vikas.maurya
"""

import pandas as pd
import matplotlib.pyplot as plt


filePath="C:\\Users\\vikas.maurya\\Desktop\\AanlyticsAssignment_Edureka\\Numpy_Pandas_MatplotLib\\DS_mod4_tcwlr\\DS_mod4\\BigMartSalesData.csv"

df = pd.read_csv(filePath)

'''
Approach to Solve

You have to use fundamentals of Matplotlib covered in module 5 and plot following 
4 chart/graph1.
'''


#1)Plot Total Sales Per Month for Year 2011. How the total sales have increased over months 
#in Year 2011. Which month has lowest Sales?
df_grouped_year = df.query("Year == 2011").filter(
    ["Month", "Amount"]).groupby(["Month"], as_index=False).sum()


# Plot Total Sales Per Month for Year 2011.
x = df_grouped_year["Month"]
y = df_grouped_year["Amount"]

plt.plot(x, y)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Month vs sales")
plt.grid()
plt.show()

print("AS we can see that from chart February Month has lowest sales")


#2.Plot Total Sales Per Month for Year 2011 as Bar Chart.  
#Is Bar Chart Better to visualize than Simple Plot?

import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = df_grouped_year["Month"]
y = df_grouped_year["Amount"]
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Month vs sales")
ax.bar(x,y)
plt.show()

print("Yes,Bar Chart Better to visulaize than simple Plot")

#3.Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards 
#sales?

df_grouped_country = df.query("Year == 2011").filter(
    ["Country", "Amount"]).groupby(["Country"], as_index=False).sum()

plt.pie(df_grouped_country["Amount"],
        labels=df_grouped_country["Country"],
        autopct='%1.1f%%',
        shadow=True)

plt.tight_layout()
plt.show()







#4.Plot Scatter Plot for the invoice amounts and see the concentration of amount.
#  In which range most of the invoice amounts are concentrated.

invoice_amounts = df.filter(["InvoiceDate", "Amount"]).groupby(
    "InvoiceDate", as_index=False).sum()

plt.scatter(invoice_amounts["InvoiceDate"], invoice_amounts["Amount"])
plt.ylim(20000, 100000)
plt.show()

  
 #Enhancements for codeYou can try these enhancements in code
 #1.Change the bar chart to show the value of bar 
 #2.In Pie Chart Play With Parameters shadow=True, startangle=90 and see how different
 #the chart looks 
 #3.In scatter plot change the color of Scatter Points




fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = df_grouped_year["Month"]
y = df_grouped_year["Amount"]

for index, value in enumerate(x):
    plt.text(value, index, str(value))
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.title("Month vs sales")
ax.bar(x,y)
plt.show()



df_grouped_country = df.query("Year == 2011").filter(
    ["Country", "Amount"]).groupby(["Country"], as_index=False).sum()

plt.pie(df_grouped_country["Amount"],
        labels=df_grouped_country["Country"],
        autopct='%1.1f%%',
        shadow=True,startangle=90)

plt.tight_layout()
plt.show()


invoice_amounts = df.filter(["InvoiceDate", "Amount"]).groupby(
    "InvoiceDate", as_index=False).sum()

plt.scatter(invoice_amounts["InvoiceDate"], invoice_amounts["Amount"],color="yellow")
plt.ylim(20000, 100000)
plt.show()