import os
import glob
import zipfile

home    = "/Users/sr/Desktop/deloitte"
pattern = "*.py"
target  = "/Users/sr/Desktop/day2.zip"

os.chdir(home)						#go to home dir
files2bzipped = glob.glob(pattern)	#select the files
z=zipfile.ZipFile(target,"w",zipfile.ZIP_DEFLATED)

for myfile in files2bzipped:
	z.write(myfile)
z.close()
