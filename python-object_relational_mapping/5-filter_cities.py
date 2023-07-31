#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all
cities of that state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    v = sys.argv
    db = MySQLdb.connect(host="localhost", user=v[1],
                         passwd=v[2], db=v[3])
    cur = db.cursor()
    cur.execute("""
SELECT c.name FROM cities c
JOIN states s ON c.state_id = s.id
WHERE s.name = %s
ORDER BY c.id;""", (v[4], ))
    rows = cur.fetchall()
    string_output_list = []
    for row in rows:
        string_output_list.append(row[0])
    print(*string_output_list, sep=', ')
    cur.close()
    db.close()
