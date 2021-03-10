import pandas as pd
df=pd.read_csv("BMWW.csv")
print("Dataframe df")
print(df)

import matplotlib.pyplot as plt
plt.xlabel('Mileage/Age( in years)')
plt.ylabel('SellPrice')
plt.scatter(df['Mileage'],df['SellPrice'],color='green')
plt.scatter(df['Age'],df['SellPrice'],color='red')

x=df[['Mileage','Age']]
y=df['SellPrice']


print(df[['Mileage','Age']])
print(df['SellPrice'])


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)

print("X Training")
print(x_train)

print("Y Training")
print(y_train)

print("X Test")
print(x_test)

print("Y Test")
print(y_test)

print(len(x_train))

from sklearn.linear_model import LinearRegression
clf=LinearRegression()

clf.fit(x_train,y_train)
ud=clf.predict(x_test)

print(ud)

print(clf.score(x_train,y_train))
print(clf.score(x_test,y_test))



