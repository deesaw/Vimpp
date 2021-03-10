import csv
import sqlite3    
conn = sqlite3.connect("newdatabase.db")
cursor = conn.cursor() ## file pointer to dbk
f=open("marks.csv","r")										#open the file
csvreader = csv.reader(f)

sql1 = """
CREATE TABLE marks2(
sname TEXT ,
marks1 INTEGER,
marks2 INTEGER,
marks3 INTEGER
)
"""
#cursor.execute(sql1)
sql = """
INSERT INTO marks2(sname,marks1, marks2,marks3)
VALUES(?,?,?,?) """


markslist = []
for row in csvreader:													#read line by line
   markslist.append(tuple(row))    
   
cursor.executemany(sql,markslist)


sql2 = """
SELECT *  from marks2
"""

for bid,title,author in cursor.execute(sql2):print (sname,marks1,marks2,marks3,marks4)

conn.commit()  
conn.close()  
print("Inserted {} rows".format(cursor.rowcount))
conn.close() 
f.close()
