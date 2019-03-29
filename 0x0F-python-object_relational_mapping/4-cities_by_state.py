/usr/bin/python3
"""script that list all cities form database hbtn_0e_4_usa
"""
import MySQLdb
import sys

args = sys.argv
db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        password=args[2],
        db=args[3]
        )
cur = db.cursor()

query = '''
SELECT cities.id, cities.name, states.name 
FROM cities LEFT JOIN states
ON cities.state_id = states.id'''

cur.execute(query)
rows = cur.fetchall()
for c in rows:
    print("({}, {}, {})".format(c[0], c[1], c[2]))

cur.close()
db.close()

if __name__ == "__main__":
    pass
