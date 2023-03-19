#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {} username password database_name'.format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
