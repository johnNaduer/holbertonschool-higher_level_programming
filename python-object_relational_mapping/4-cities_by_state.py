#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    i = "SELECT cities.id, cities.name, states.name FROM cities JOIN\
        states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(i)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.cursor()
