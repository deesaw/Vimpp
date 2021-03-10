# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:01:17 2019

@author: deesaw
"""

f=open('Setting.txt','r')
settings = {}
for line in f:
	if "=" in line:
		key ,value = line.strip().split('=')
		settings[key.strip()] =value.strip()
f.close()
print(settings)

print(settings.get('tmp_table_size'))