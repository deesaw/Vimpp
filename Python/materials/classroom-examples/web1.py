import sqlite3
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hi():
    return "hi from flask"

@app.route("/")
def hi2():
    return "Welcome to my home page"

@app.route("/wish/<name>")
def wish(name):
    return "hi <b>{}</b>".format(name)

@app.route("/book/<bid>")
def book(bid):
    conn =sqlite3.connect("mydatabase.db")
    sql ="select * from books where bid = {}".format(bid)
    result = conn.cursor().execute(sql).fetchone()
    conn.close()
    return str(result)
app.run()