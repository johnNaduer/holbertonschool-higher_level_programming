from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creating a connection to the database
engine = create_engine("mysql+pymysql://root:root@localhost/NEW_TABLAS")

# Creating an instance of declarative_base
Base = declarative_base()

# Creating a State class that inherits from Base
class State(Base):
    # Naming the table
    __tablename__ = 'states'
    # Defining columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Creating the table
Base.metadata.create_all(engines)
