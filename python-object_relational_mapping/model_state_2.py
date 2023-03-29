from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'john_naduer'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

def create_states_table(user, password, host, database):
    from sqlalchemy import create_engine
    engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}')
    Base.metadata.create_all(engine)
