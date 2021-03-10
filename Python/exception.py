# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:11:20 2019

@author: deesaw
"""


def divide1(a,b):
    try:
        result=a/b
    except ZeroDivisionError :
        print("Check denominator")
    else:
        print(result)
    finally:
        print("Final block")


divide1(5,2)
divide1(5,0)
divide1(a,0)