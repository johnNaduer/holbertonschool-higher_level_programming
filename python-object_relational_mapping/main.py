import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='NEW_TABLAS'
            )
        self.cursor = self.connection.cursor()

database = Database()
