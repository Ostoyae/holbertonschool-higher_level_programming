#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    to_del = session.query(State).filter(State.name.like('%a%'))
    for d in to_del:
        session.delete(d)
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
    session.commit()
    session.close()
    engine.dispose()
