#Way1:
import sqlite3    
conn = sqlite3.connect("newdatabase.db")
cursor = conn.cursor() ## file pointer to db

sql = """
SELECT * from books
"""

for row in cursor.execute(sql):
    print(row)
conn.close() 
    
"""
#Way2
###make it more readable
  
  
import sqlite3    
conn = sqlite3.connect("newdatabase.db")
cursor = conn.cursor() ## file pointer to db

sql = """
#SELECT *  from books
"""

for bid,title,author in cursor.execute(sql):
    print (bid,title,author)
    
conn.close()  
 
"""