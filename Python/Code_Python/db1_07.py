import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
CREATE TABLE books(
bid INTEGER PRIMARY KEY,
title TEXT,
author TEXT
)
"""
cursor.execute(sql)
print("Table created")
conn.close()