# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:44:41 2019

@author: deesaw
"""

from oops3 import Dog
class GuardDog(Dog):
    scientific_name= "Cannis Famliaris"
    _password="kkkkkkksss"#private varibale
    
    def __init__(self,color,breed,weight):
        super().__init__(color,breed)#super().__init__(color,None)
        self.weight=weight
    def speak(self):print("grrr.grrr")
    def pspeak(self):super().speak()

tiger = GuardDog("Brown","Doberman",35)
tiger.speak()
tiger.guard()
tiger.pspeak()
print(tiger.weight)
print(tiger.scientific_name)
print(tiger._password)#cannot be called outside the class

"""
from oops3 import Dog


class GuardDog(Dog):
	def speak(self):
            print("grrrr")
            def pspeak(self):
                super.speak()

tiger = GuardDog("Brown","Doberman")
tiger.speak()
tiger.pspeak()
tiger.guard()
"""