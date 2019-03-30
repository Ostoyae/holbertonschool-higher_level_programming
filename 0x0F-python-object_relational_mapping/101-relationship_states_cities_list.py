#!/usr/bin/usr python3
'''print out all State and cities using SQLAlchemy relationships
'''
import sys
from relationship_city import Base, City
from relationship_state import State
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    sess = Session()

    state_list = sess.query(State).join(City).order_by(State.id, City.id)
    if state_list is not None:
        for s in state_list:
            print('{}: {}'.format(s.id, s.name))
            for c in s.cities:
                print('    {}: {}'.format(c.id, c.name))
    else:
        print()
    sess.close()
    engine.dispose()
