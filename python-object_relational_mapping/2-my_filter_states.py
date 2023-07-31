#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    v = sys.argv
    db = MySQLdb.connect(host="localhost", user=v[1],
                         passwd=v[2], db=v[3])
    cur = db.cursor()
    q = "SELECT * FROM states ORDER BY id;"
    if v[4]:
        q = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id;"\
            .format(v[4])
    cur.execute(q)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
