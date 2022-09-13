#!/usr/bin/env python3
"""
A script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!

Args:
    username (str): The MySQL username
    password (str): The MySQL password
    database (str): The database name
    name (str): The state name to search
"""
import sys
import MySQLdb


def create_db(username, password, db_name):
    """
    Calls the database and executes the query
    """
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    return db


def state_with_highest_len():
    """
    Returns the state with the highest length
    """
    db = create_db(sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states"
    cur.execute(query)
    states = cur.fetchall()
    cur.close()
    db.close()

    max_len = 0
    for state in states:
        if len(state[1]) > max_len:
            max_len = len(state[1])
    return max_len


def check_name(name):
    """
    Checks if the name is a valid string
    """
    max_len = state_with_highest_len()
    if len(name) > max_len:
        return False
    return True
    

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    if check_name(name):
        db = create_db(username, password, db_name)
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = '{}'".format(name)
        cur.execute(query)
        states = cur.fetchall()
        cur.close()
        db.close()

        for state in states:
            print(state)
