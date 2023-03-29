from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine

Base = declarative_base()

#con engine establecemos la coneccionn
engine = create_engine("mysql+mysqldb://root:root@localhost/JHON_SALCHICHON")



#modelo es la representacion de nuestra tabla en una base de datos

class User(Base):
    __tablename__ = 'users'

#vendrian ser los atributos de nuestra clase

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
       return self.username 

#estableceemos la relacion entre la conexion y el modelo
Session = sessionmaker(engine)
session = Session()


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine) crea las tablas en una base de datos que ya existe. Si la base de datos aún no existe, es necesario crearla antes de llamar a esta función.
    Base.metadata.create_all(engine)
