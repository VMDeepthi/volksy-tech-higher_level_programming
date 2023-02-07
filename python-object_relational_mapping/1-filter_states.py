#!/usr/bin/python3
"""Filter States"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(username=sys.argv[1], passwordd=sys.argv[2], databasename=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(states) for states in c.fetchall() if states[1][0] == "N"]
