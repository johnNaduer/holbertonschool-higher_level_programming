#!/usr/bin/python3
""" Script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument. But this time,
    write one that is safe from MySQL injections! """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    cur = db.cursor()

    query = """SELECT * FROM states
               WHERE name LIKE BINARY %(state_name)s
               ORDER BY id ASC"""

    cur.execute(query, {'state_name': state_name})

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
