#!/usr/bin/python3
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
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
    for s, c in session.query(State, City).\
            filter(State.id == City.state_id)\
            .order_by(City.id):
        print('{}: ({}) {}'.format(
            s.name,
            c.id,
            c.name
        )
        )
    session.close()
    engine.dispose()
