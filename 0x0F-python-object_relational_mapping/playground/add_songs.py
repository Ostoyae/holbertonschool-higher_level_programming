#!/usr/bin/env python3
import MySQLdb

db = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        password="docker",
        db="playground"
        )

cur = db.cursor()

songs = ("meow", "woof", "meow go woof")

data = 'suzu and raven'
cur.execute('INSERT INTO song (`title`) VALUES ("woof")')
print("Auto increament ID: {}".format(cur.lastrowid))
