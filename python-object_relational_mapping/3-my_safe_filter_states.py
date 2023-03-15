#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. This script is
safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) == 5:
        # Get command line arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        # Connect to MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name)

        # Create a cursor object to execute queries
        cur = conn.cursor()

        # Execute the query (safe from SQL injection)
        cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (state_name,))

        # Fetch all the rows as a list of tuples
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close cursor and connection
        cur.close()
        conn.close()
    else:
        return
