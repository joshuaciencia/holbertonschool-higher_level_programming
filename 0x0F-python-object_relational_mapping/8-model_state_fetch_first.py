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
    query = s.query(State).filter(State.id)
    first = query.first()
    if first != None:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    s.close()

