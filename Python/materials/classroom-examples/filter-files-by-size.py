import os
SIZE = 5 * 1024 * 1024

myfiles = os.listdir() #get all files

for myfile in myfiles:	#filter the required files
	if os.path.getsize(myfile) > SIZE:
		print(myfile)