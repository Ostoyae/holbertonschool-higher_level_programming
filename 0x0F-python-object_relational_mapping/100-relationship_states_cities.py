#!/usr/bin/python3

import sys
from relationship_city import Base, City
from relationship_state import State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        )
    )
    Base.metadata.create_all(engine)
    sf = City(name='San Francisco')
    ca = State(name='California', cities=[sf])

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(ca)
    session.commit()

    session.close()
    engine.dispose()
