# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:36:21 2019

@author: deesaw
"""

import sys
filename = sys.argv[1]
pattern  =  sys.argv[2]

f=open(filename,"r")
for lineno,line in enumerate(f):
	if pattern.lower() in line.lower():
		print(lineno+1,line.rstrip())
f.close()

#python  Fileneme.py arv1 agrv2
