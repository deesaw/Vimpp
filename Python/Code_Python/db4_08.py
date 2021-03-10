import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
INSERT INTO books(title,author)
VAlUES(?,?)
"""

books =[
        ("My experiments with truth","MK Gandhi"),
        ("Greatness Guide","Robin Sharma")
]

cursor.executemany(sql,books)
conn.commit()
print("Inserted {} rows".format(cursor.rowcount))
conn.close()