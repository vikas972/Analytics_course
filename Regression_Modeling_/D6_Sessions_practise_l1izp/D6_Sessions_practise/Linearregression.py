# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 06:34:18 2018

@author: NAEEN REDDY
"""

    "# Import libraries necessary for this project
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    bos1 = pd.read_csv('E:\\Larning\\Ed\\DataSciencewithPython\\py\\D6\\BostonHousing.csv')
    print(bos1)
    
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test =train_test_split(x,y, test_size = 0.33, random_state =5)
    
    
    
        "from sklearn.linear_model import LinearRegression
    "#fitting our model to train and test
    "lm = LinearRegression()
    "model = lm.fit(x_train,y_train)"
    
    
        "pred_y = lm.predict(x_test)"
        
        
        
            "plt.scatter(y_test,pred_y)
    "plt.xlabel('Y Test')
    "plt.ylabel('Predicted Y')"