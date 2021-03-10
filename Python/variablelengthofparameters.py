# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:14:16 2019

@author: deesaw
"""

def average(*num):
    print(type(num))
    print(num)
    print(float(sum(num))/len(num))
average(3,4)
average(3,4,8)
average(3,4,8,90,4.5,5.3,7.8)