/usr/bin/python3
"""Query all states in a table in db hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=args[1],
            password=args[2],
            db=args[3]
            )

    cur = db.cursor()

    try:
        cur.execute('SELECT * FROM states ORDER BY id ASC')
        rows = cur.fetchall()
    except MySQLdb.error as e:
        try:
            print("MySQL Error [{:d}]: {:s}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Erro: {}".format(e))

    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    db.close()
