#!/usr/bin/python3
""" list cities from db
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            LEFT JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
