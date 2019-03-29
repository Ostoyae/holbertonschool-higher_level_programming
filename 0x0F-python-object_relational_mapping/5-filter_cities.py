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
SELECT cities.name
FROM cities LEFT JOIN states
ON cities.state_id = states.id
WHERE states.name = %s
ORDER BY cities.id ASC'''

cur.execute(query, (args[4],))
rows = cur.fetchall()
for c in range(len(rows)):
    print("{}".format(
        rows[c][0]),
        end="{}".format(", " if c < len(rows) - 1 else "\n")
        )
    
cur.close()
db.close()

if __name__ == "__main__":
    pass
