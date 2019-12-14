#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb, sys
    db = MySQLdb.connect(host='localhost',
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(state)s\
            ORDER BY states.id", {'state': sys.argv[4]})
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
