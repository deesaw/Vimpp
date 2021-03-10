# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:15:04 2020

@author: deesaw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import math


df=pd.read_csv("home2.csv")
print(df)

median_bedrooms=math.floor(df.bedrooms.median())
df.bedrooms=df.bedrooms.fillna(median_bedrooms)
print(df.bedrooms)
print(df)

reg=linear_model.LinearRegression()
reg.fit(df[['sqft','bedrooms','age']],df.prices)

print(reg.coef_)
print(reg.intercept_)

print(reg.predict([[3000,3,40]]))

