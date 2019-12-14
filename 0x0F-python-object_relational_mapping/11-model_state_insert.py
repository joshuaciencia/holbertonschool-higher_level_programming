#!/usr/bin/python3
"""
 adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    new_state = State(name="Louisiana")
    s.add(new_state)
    query = s.query(State).filter(State.name == "Louisiana").first()
    print(query.id)
    s.commit()
    s.close()
