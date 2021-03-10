# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:03:51 2019

@author: deesaw
"""

# Write a function to add two lists element wise.
a = [6, 7, 8]
b = [7, 4, 5]


def add_lists(list1, list2):
    tmp = []
    for index in range(len(list1)):
        tmp.append(list1[index] + list2[index])
    return tmp


print(add_lists(a, b))
print(add_lists([1, 2, 3], [1, 2, 3]) == [2, 4, 6])

