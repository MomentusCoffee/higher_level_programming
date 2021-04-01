#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session2 = session()

    state = session2.query(State, City).\
        filter(City.state_id == State.id)

    for states, cities in state:
        print("{}: ({}) {}".format(states.name,
                                   cities.id, cities.name))
    session2.close()
