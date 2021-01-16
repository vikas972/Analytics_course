
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model, metrics


# In[6]:


# load the boston dataset 
boston = datasets.load_boston(return_X_y=False)


# In[4]:


boston


# In[7]:


# defining feature matrix(X) and response vector(y) 
X = boston.data 
y = boston.target 


# In[8]:


# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, 
                                                    random_state=1) 


# In[9]:


# create linear regression object 
reg = linear_model.LinearRegression()


# In[10]:


# train the model using the training sets 
reg.fit(X_train, y_train) 


# In[11]:


# regression coefficients 
print('Coefficients: \n', reg.coef_) 


# In[12]:


# variance score: 1 means perfect prediction 
print('Variance score: {}'.format(reg.score(X_test, y_test))) 


# In[13]:


# plot for residual error 
  
## setting plot style 
plt.style.use('fivethirtyeight')

## plotting residual errors in training data 
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
            color = "green", s = 10, label = 'Train data') 

## plotting residual errors in test data 
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
            color = "blue", s = 10, label = 'Test data')

## plotting line for zero residual error 
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2) 

## plotting legend 
plt.legend(loc = 'upper right') 

## plot title 
plt.title("Residual errors") 
  
## function to show plot 
plt.show() 

