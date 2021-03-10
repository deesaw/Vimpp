# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:56:28 2019

@author: deesaw
"""

class Dog:
	def speak(self):
		print("bhou..bhou")
	def guard(self):
		print("I am guarding")
    

tommy = Dog()
jimmy = Dog()

print(type(tommy))
print(isinstance(tommy,Dog))
tommy.speak()
jimmy.guard()
