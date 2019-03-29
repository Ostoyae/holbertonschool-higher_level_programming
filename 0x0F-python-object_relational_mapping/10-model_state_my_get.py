#!/usr/bin/python3
'''List all state in a table via SQLAlchemy
'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        instance = session.query(State)\
                .filter(State.name == sys.argv[4])\
                .first()
        print("{}".format(instance.id))
    except:
        print("Not found")
    session.close()
    engine.dispose()
