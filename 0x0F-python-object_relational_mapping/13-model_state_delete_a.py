#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    s = Session()
    instances = s.query(State).filter(State.name.like('%a%'))
    for inst in instances:
        s.delete(inst)
    s.commit()
    s.close()
