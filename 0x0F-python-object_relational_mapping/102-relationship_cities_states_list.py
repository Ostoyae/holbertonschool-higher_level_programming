#!/usr/bin/python3
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

    city_list = sess.query(City).order_by(City.id)
    if city_list is not None:
        for c in city_list:
            print('{}: {} -> {}'.format(c.id, c.name, c.state.name))
    else:
        print()
    sess.close()
    engine.dispose()
