#!/usr/bin/python3
"""
A script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.

Args:
    username (str): The MySQL username
    password (str): The MySQL password
    database (str): The database name
    name (str): The state name to search
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}'".format(name)
    cur.execute(query)
    states = cur.fetchall()
    cur.close()
    db.close()

    for state in states:
        print(state)
