#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb, sys
    db = MySQLdb.connect(host='localhost',
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states\
            LEFT JOIN cities ON states.id = cities.state_id\
            WHERE states.name = %(state)s\
            ORDER BY cities.id", {'state': sys.argv[4]})
    states = cur.fetchall()
    for i in range(len(states)):
        print(states[i][0], end="")
        if (i != len(states) - 1):
            print(', ', end="")
    print()
    cur.close()
    db.close()
