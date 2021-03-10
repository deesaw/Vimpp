
import sqlite3
import csv

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

ipfile = open('marks.csv','r')											

csvreader = csv.reader(ipfile)
outerlist=[]
for line in ipfile:
    values1 = line.strip().split(",") #['Akbar', '90', '45', '76']
    outerlist.append(values1)
    #print(values1) #None

sql = """
create table marks(NAME text,SUB1 text,SUB2 text,SUB3 text)
"""

sql1 = """
INSERT INTO marks(NAME,SUB1,SUB2,SUB3)
VAlUES(?,?,?,?)
"""

marks = tuple(outerlist)
cursor.execute(sql)
cursor.executemany(sql1,marks)
print("Inserted {} rows".format(cursor.rowcount))
conn.commit()
conn.close()
ipfile.close()
