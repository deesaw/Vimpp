# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:58:20 2019

@author: deesaw
"""

def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Division by zero is not allowed")


divide(5,2)
divide(5,0)

def divide1(a,b):
    try:
        print(a/b)
    except Exception as err:
        print(type(err),err)


divide1(5,2)
divide1(5,0)