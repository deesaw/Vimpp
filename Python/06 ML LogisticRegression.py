#LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split

df=pd.read_csv("LogisticRegression.csv")
print(df)
x=df.Age
y=df.Has_I
plt.scatter(x,y,color='red',marker='*')
x_train,x_test,y_train,y_test=train_test_split(df[['Age']],df.Has_I,test_size=0.2,random_state=10)
print(x_train)
print(x_test)
slt=LogisticRegression()
slt.fit(x_train,y_train)
print(slt.predict(x_test))
print(slt.score(x_test,y_test))
print(slt.predict_proba(x_test))




