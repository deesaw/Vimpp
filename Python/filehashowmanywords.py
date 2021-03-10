# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:10:23 2019

@author: deesaw
"""

f=open("Ping.txt","r")
def get_word_count(fp):
    return len(fp.read().split())
print(get_word_count(f))
f.close()

    