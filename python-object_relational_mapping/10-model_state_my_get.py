#!/usr/bin/python3
"""
Python file that contains the class definition of a State
"""

from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pw, db)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    search_item = sys.argv[4]
    states = session.query(State).filter(State.name == search_item)
    for state in states:
        if state:
            print(state.id)
        else:
            print("Not found")
    session.close()
