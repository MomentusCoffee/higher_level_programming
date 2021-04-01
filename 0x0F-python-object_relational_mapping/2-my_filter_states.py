#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
of pytn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name REGEXP '{}'"
              .format(sys.argv[4]))
    q = c.fetchall()
    for state in q:
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    db.close()
