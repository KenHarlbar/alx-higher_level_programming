#!/usr/bin/env python3
"""
A script prints the State object with the
name passed as argument from the database
hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def state_with_highest_len(username, password, db_name):
    """
    Returns the state with the highest length
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    session.close()
    max_len = 0
    for state in states:
        if len(state.name) > max_len:
            max_len = len(state.name)
    return max_len


def check_name(username, password, db_name, name):
    """
    Checks if the name is a valid string
    """
    max_len = state_with_highest_len(username, password, db_name)
    if len(name) > max_len:
        return False
    return True


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    if check_name(username, password, db_name, name):
        state = session.query(State).filter(State.name == name).first()
        session.close()
        if state:
            print("{}".format(state.id))
        else:
            print("Not found")
    else:
        print("Not found")
