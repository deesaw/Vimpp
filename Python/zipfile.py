# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:36:32 2019

@author: deesaw
"""
import os
import glob
import zipfile

home    = 'C:/Users/deesaw/Desktop/Python/'
pattern = '*.txt'
target  = 'C:/Users/deesaw/Desktop/'

os.chdir(home)						#go to home dir
files2bzipped = glob.glob(pattern)	#select the files
z=zipfile.ZipFile(target,"w",zipfile.ZIP_DEFLATED)

for myfile in files2bzipped:
	z.write(myfile)
z.close()
