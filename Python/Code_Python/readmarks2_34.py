import csv
f=open("marks1.csv","r")											#open the file
csvreader = csv.reader(f)

for row in csvreader:													#read line by line
	#print(row)
	name = row[0]
	marks = []
	for x in row[1:]:
		marks.append(int(x))
	average = sum(marks)/len(marks)
	print("{}'s average is {}".format(name,round(average)))
f.close()