# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:03:23 2019

@author: deesaw
"""

class Dog:
	def __init__(self,color,breed):
		self.color=color.capitalize()
		self.breed=breed.upper()
	def speak(self):
		print("bhou..bhou")
	def guard(self):
		print("I am guarding")

tommy = Dog("black","lab")
jimmy = Dog("brown","gs")

print(type(tommy))
print(isinstance(tommy,Dog))
tommy.speak()
jimmy.guard()
print(tommy.color)
print(jimmy.breed)