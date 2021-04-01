#!/usr/bin/python3
"""lists all states from the database pytn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    q = c.fetchall()
    for state in q:
        print(state)
    c.close()
    db.close()
