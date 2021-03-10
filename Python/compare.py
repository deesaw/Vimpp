# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:40:43 2019

@author: deesaw
"""

import sys
import filecmp
file1= sys.argv[1]
file2= sys.argv[2]

print(filecmp.cmp(file1,file2,shallow=False))

#python compare.py global.py global.py