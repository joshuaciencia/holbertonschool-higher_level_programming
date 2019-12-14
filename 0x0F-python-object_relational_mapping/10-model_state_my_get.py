#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    s = Session()
    exists = False
    for instance in s.query(State).filter(State.name == sys.argv[4]).order_by(State.id):
        print("{}".format(instance.id))
        exists = True
    if not exists:
        print("Not found")
    s.close()
