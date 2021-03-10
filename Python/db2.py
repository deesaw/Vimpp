import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
INSERT INTO  books(title,author)
values ('wings','Deepa')
"""
cursor.execute(sql)

conn.commit()

print("inserted {} number of rows".format(cursor.rowcount))
conn.close()