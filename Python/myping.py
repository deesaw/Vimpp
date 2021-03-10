# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:04:50 2019

@author: deesaw
"""

import os
def myping(ip):
	command = "ping -n 1  {} > NUL".format(ip)
	respose = os.system(command)
	if respose == 0:
		return True
	else:
		return False