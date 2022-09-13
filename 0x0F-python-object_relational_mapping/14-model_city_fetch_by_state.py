#!/usr/bin/python3
"""
A script that prints all City objects from
the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st_cty = session.query(State, City).filter(State.id == City.state_id).all()
    session.close()
    for state, city in st_cty:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
