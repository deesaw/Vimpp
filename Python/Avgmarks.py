"""f=open("C:/Users/deesaw/Desktop/Python/marks.csv","r")			#open the file
for line in f:													#read line by line
	name,math,physics,chemisty = line.strip().split(',')		#get the fields
	average = (int(math)+int(physics)+int(chemisty))/3			#compute average
	print("{}'s average is {}".format(name,round(average)))		#print out put
f.close()	
"""

import csv
f=open("marks.csv","r")											#open the file
csvreader = csv.reader(f)

for row in csvreader:													#read line by line
	#print(row)
	name = row[0]
	marks = []
	for x in row[1:]:
		marks.append(int(x))
	average = sum(marks)/len(marks)
	print("{}'s average is {}".format(name,round(average)))
f.close()													#close the file