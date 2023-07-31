#!/usr/bin/python3
"""
python file that contains the class definition of a State
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

eng = create_engine("mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa")
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))


Base.metadata.create_all(eng)
