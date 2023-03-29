#!/usr/bin/python3

import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="root",
    db="NEW_TABLAS"
)

# Create a cursor object to execute queries
cur = db.cursor()

# Execute the query
cur.execute("SELECT * FROM johnzito3")

# Fetch all the results
results = cur.fetchall()

# Print out the results
for row in results:
    print(row)

# Close the database connection
db.close()
