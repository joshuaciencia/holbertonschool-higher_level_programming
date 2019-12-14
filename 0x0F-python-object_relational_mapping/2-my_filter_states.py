#!/usr/bin/python3
"""
list data from db according to a name passed
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = '{}' ORDER BY id"
            .format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
