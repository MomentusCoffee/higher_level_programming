#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the
database pytn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name REGEXP '^[N]'")
    q = c.fetchall()
    for state in q:
        if state[1][0] == 'N':
            print(state)
    c.close()
    db.close()
