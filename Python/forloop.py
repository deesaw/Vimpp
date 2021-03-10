# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:05:16 2019

@author: deesaw
"""

for x in range(5):
    print("hello")

for x in range(5):
    print(x,"hello")

for x in range(5,10):
    print(x)

for x in range(5,100,20):
    print(x)

name ="Ramesh"
friends = ["hari","lahari","sita","pavan"]
marks = (56,89,34,25,67)

for x in name:
    print(x)

for friend in friends:
    print(friend)

for index,friend in enumerate(friends):
    print(index,friend)
print("bye")