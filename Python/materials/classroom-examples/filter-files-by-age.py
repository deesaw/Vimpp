import os
import time
AGE = 1 * 24 * 60 * 60

myfiles = os.listdir() #get all files

for myfile in myfiles:	#filter the required files
	if (time.time() - os.path.getctime(myfile)) < AGE:
		print(myfile)