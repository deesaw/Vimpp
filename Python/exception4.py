# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:28:05 2019

@author: deesaw
"""

#custom exceptions
class DeloitteMath(Exception):
	def __init__(self,args):
		super().__init__(args)

e = DeloitteMath("I do not know math")

raise e

myexp = ValueError("pl. check the values")

raise myexp