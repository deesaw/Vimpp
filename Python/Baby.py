# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:13:08 2019

@author: deesaw
"""

class Baby:
    def __init__(self,name):
        self.name=name.capitalize()
    def cry(self):print("cry")
    def laugh(self):print("laugh")
    def hi(self):print("Hello!! My name is {}".format(self.name)) 
    
