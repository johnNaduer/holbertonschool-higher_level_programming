#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":

    i = 'mysql+mysqldb://{}:{}@localhost/{}'
    n = pool_pre_ping=True
    engine = create_engine(i.format(argv[1], argv[2], argv[3]), n)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for row in states:
        print("{}: {}".format(row.id, row.name))
