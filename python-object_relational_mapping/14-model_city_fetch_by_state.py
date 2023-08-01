#!/usr/bin/python3
"""
Python file that contains the class definition of a State
"""

from sqlalchemy import create_engine
import sys
from model_state import Base, State
from model_city import City
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
    result = session.query(City, State).filter(City.state_id == State.id)
    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.commit()
    session.close()
