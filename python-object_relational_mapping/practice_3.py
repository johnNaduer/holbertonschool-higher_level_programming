import MySWLdb
import sys
#librerias que necesitaremos

#conexion al servidor
try:
    db = MySQLdb.connect(
            host = '127.0.0.1'.
            user = 'root'.
            passwd = 'capitanaso123'.
            db = 'universidad'
            )
except exception as e:
    sys.exit('no podemos entrar a la base de datos')
#estos datos los tienen que acomodar dependiendo del usuario y contraseña
# de su servidor mysql

#ahora haremos las funciones para msotrar e insertar los datos en la base de datos

def mostrardatos():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM categoria') #esta es la tabla que veremos e insertaremos
    #loop para acomodar la informacion
    if datos:
        for z in datos:
            print str(z[0]) + '.-' + z[1]
#z[0] es un numero entero, por eso le estoy convirtiendo a string

def insertardatos():
    print('cual es la descripcion')
    texto = raw_input()
    cursor = db.cursor()
    stringquery = "INSERT INTO" + "categoria" + "(descripcion)" + "VALUES("+ "\"" + texto + "\")";
    cursor.execute(stringquery)
    db.commit() #muy importante, esto es para que se manden todos los cambios a la base de datos

#ya tenemos las funciones. hagamos el menu main

if __name__ == "__main__":
    opc = 0
    #para la seleccion del menu
    while opc != '3':
        print ("\n1.- mostrar datos")
        print ("2.- agregar datos")
        print ("3.-salir")
        opc = raw_input()

        if opc == '1':
            mostrardatos()
        elif opc == '2':
            insertardatos()
        else:
            print("hasta luego!")
            exit
