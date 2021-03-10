import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv('home.csv')
print(df)

d=pd.read_csv('area.csv')
print(d.head)


#%matplotlib inline
plt.xlabel('sqft')
plt.ylabel('prices')
plt.scatter(df.sqft,df.prices,color='#202020',marker='*')

reg=linear_model.LinearRegression()
reg.fit(df[['sqft']],df.prices)

#reg.predict('3300')

print(reg.coef_)
print(reg.intercept_)
#print(reg.predict(3300))

p=reg.predict(d)
d['price']=p

d.to_csv("Outputpredict.csv")
d.to_csv("OutputpredictwithoutIndex.csv",index=False)

#plt.plot(df.sqft,reg.predict(df.sqft),color=blue)
plt.plot(d.area,p,color='green')
plt.plot(df.sqft,df.prices,color='black')

#save the model in file

from sklearn.externals import joblib
joblib.dump(reg,'model_joblib')
mj=joblib.load('model_joblib')
print('Predict 5000:'+str(mj.predict([[5000]])))
            




