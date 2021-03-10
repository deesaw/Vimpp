# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:00:25 2019

@author: deesaw
"""

age=19 #global

def grow():
    global age
    print(age)
    age=age+1#local
    print(age)
    
print(age)
grow()