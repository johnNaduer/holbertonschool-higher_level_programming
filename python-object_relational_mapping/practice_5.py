#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="root",
        db="new_database"
        )
cursor = db.cursor()

cursor.execute("SELECT * FROM departamentos")

resultados = cursor.fetchall()

#imprimir resultados

for resultado in resultados:
    print(resultado)
    print("ID:", resultado[0], "Nombre:", resultado[1])

db.close()
