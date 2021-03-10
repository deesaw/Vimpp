import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv('homeprices.csv')
print(df)

dummies=pd.get_dummies(df.town)
print(dummies)

merged=pd.concat([df,dummies],axis='columns')
print(merged)

final=merged.drop(['town','ww'],axis='columns')
print(final)

reg=linear_model.LinearRegression()
x=final.drop(['prices'],axis='columns')
y=final.prices
print('x')
print(x)
print('y')
print(y)

reg.fit(x,y)
print('Predict (r): '+ str(reg.predict([[2800,0,1]])))

print('Predict (ww): '+ str(reg.predict([[3400,0,0]])))


print('Accuracy:'+str(reg.score(x,y)))


#one hotencoder
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

dfle=df
dfle.town=le.fit_transform(dfle.town)
print(le.fit_transform(dfle.town))
print(dfle)
X=df[['town','sqft']].values# 2d array in stead of dataframe
print('X')
print(X)
Y=dfle.prices
print('Y')
print(Y)


from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[0])

X=ohe.fit_transform(X).toarray()
print(X)

X=X[:,1:]#drop first column
print(X)

reg.fit(X,Y)
print(reg.predict([[1,0,2800]]))
