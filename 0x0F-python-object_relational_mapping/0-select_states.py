#!/usr/bin/env python3

"""
    A script that lists all states from the database hbtn_0e_0_usa

    Args:
        username (str): The MySQL username
        password (str): The MySQL password
        database (str): The database name
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    cur.close()
    for state in states:
        print(state)
