#!/usr/bin/python3

"""
Defines the State class and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Links to the MySQL table states
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    """Start link class to table in database"""
    import sys
    from sqlalchemy import create_engine
    
    engine = create_engine('mysql+mysqldb://root:root@localhost/JHON_SALCHICHON', pool_pre_ping=True)
    Base.metadata.create_all(engine)
