#!/usr/bin/env python3
"""
A script that lists all cities from the database hbtn_0e_4_usa

Args:
    username (str): The MySQL username
    password (str): The MySQL password
    database (str): The database name
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")
    cities = cur.fetchall()
    cur.close()
    db.close()

    for city in cities:
        print(city)
