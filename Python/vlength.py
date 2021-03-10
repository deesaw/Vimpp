# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:21:15 2019

@author: deesaw
"""

def polygon(**kwds):
    print(type(kwds))
    print (kwds)
polygon(width=10,length=20)
polygon(width=10,length=20,height=5)
polygon(width=10,length=20,height=5,units='cm')