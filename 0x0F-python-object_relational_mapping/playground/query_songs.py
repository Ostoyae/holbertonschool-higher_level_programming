#!/usr/bin/env python3
import MySQLdb

db = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        password="docker",
        db="playground"
        )

cur = db.cursor()

cur.execute("SELECT * FROM song")
rows = cur.fetchall()

for row in rows:
    for col in row:
        print("{}".format(col), end=",")
    print()
