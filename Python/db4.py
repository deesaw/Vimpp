import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
INSERT INTO  books(title,author)
values ('wings','Deepa')
"""

try:
    cursor.execute(sql)
except:
    conn.rollback()
    print("Error occured, rolling back")
    
else:
    conn.commit()
    print("inserted {} number of rows".format(cursor.rowcount))
finally:
    conn.close()
    print("Closing connection")