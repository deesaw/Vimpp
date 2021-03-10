f=open("marks.csv","r")											#open the file
for line in f:													#read line by line
	name,math,physics,chemisty = line.strip().split(',')		#get the fields
	average = (int(math)+int(physics)+int(chemisty))/3			#compute average
	print("{}'s average is {}".format(name,round(average)))		#print out put
f.close()														#close the file