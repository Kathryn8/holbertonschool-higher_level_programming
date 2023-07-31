#!/usr/bin/python3
"""
Python file that contains the class definition of a State
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Definition of the State class inherited from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://root:root@localhost:3306/hb\
tn_0e_6_usa")
    Base.metadata.create_all(engine)
