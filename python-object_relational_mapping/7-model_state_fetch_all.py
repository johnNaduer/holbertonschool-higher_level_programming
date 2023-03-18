#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    i = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(i.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for row in states:
        print("{}: {}".format(row.id, row.name))
