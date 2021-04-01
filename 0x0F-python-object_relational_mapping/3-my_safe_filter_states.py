#!/usr/bin/python3
"""takes in arguments and displays all values in the states table
of pytn_0e_0_usa where name matches the argument
(safe from injections)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name=%s", (sys.argv[4],))
    q = c.fetchall()
    for state in q:
        print(state)
    c.close()
    db.close()
