# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:50:57 2019

@author: deesaw
"""

while True:
    try:
        amount=int(input("Enter the amount to be withdrawn"))
        print("Collect Cash")
        break
    except ValueError:
        print("Enter a valid amount")