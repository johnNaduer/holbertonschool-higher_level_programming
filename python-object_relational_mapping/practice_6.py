#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(
        port = 3306,
        user = "johnnaduer",
        passwd = "polares",
        db = "NEW_TABLAS"
        )

cursor = db.cursor()
cursor.execute("SELECT * FROM johnzito3")

resultados = cursor.fetchall()

for row in resultados:
    print(row)

db.close()
