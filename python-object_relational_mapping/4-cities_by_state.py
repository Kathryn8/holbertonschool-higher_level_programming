#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    v = sys.argv
    db = MySQLdb.connect(host="localhost", user=v[1],
                         passwd=v[2], db=v[3])
    cur = db.cursor()
    cur.execute("""
SELECT a.id, a.name, b.name FROM cities a
JOIN states b ON a.state_id = b.id ORDER BY id;
""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
