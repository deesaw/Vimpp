# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:06:42 2019

@author: deesaw
"""

import os
import time


list=os.listdir()	
size=5

for l in list:
    if os.path.getsize(l) > size:
        print(l) 

age=1*24*60*60

for l in list:
    if (time.time()-os.path.getctime(l)<age):
        print(l) 
       		
    
 
    """for i in os.listdir():
    if os.path.getsize(i) > 1024:
        print ("{} Size of file more than one 1 MB".format(i))

"""
#for myfile in files2bzipped:
#	z.write(myfile)
#z.close()
