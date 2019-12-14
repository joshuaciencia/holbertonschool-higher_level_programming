#!/usr/bin/python3
"""script to get data in a db """

if __name__ == '__main__':
    """ get data from db """
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
