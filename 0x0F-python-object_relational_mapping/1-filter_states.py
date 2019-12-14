#!/usr/bin/python3
"""
list data from db starting with 'N'
"""
if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    states = cur.fetchall()
    for state in states:
        if state[1][0] != 'N':
            continue
        print(state)
    cur.close()
    db.close()
