#Logistic Regression
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits=load_digits()

print(dir(digits))
print(digits.data[0])

plt.gray()
for i in range(5):
    print(digits.data[i])
    print(digits.target[i])
    print(digits.target_names[i])
    print(digits.DESCR[i])
    plt.matshow(digits.images[i])
    
print(digits.target[0:5])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.2,random_state=10)

#print(x_test)
print(len(x_test))

from sklearn.linear_model import LogisticRegression

slt=LogisticRegression()
slt.fit(x_train,y_train)

print(slt.predict(x_test))
print(slt.score(x_test,y_test))

plt.matshow(digits.images[67])
print(digits.target[67])

print(slt.predict([digits.data[67]]))
#print(slt.predict(digits.data[0:5]))

y_predicted= slt.predict(x_test)
from sklearn.metrics import confusion_matrix

cm=confusion_matrix(y_test,y_predicted)
print(cm)

import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

