/usr/bin/python3
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
    la = State(name='Louisiana')
    session.add(la)
    try:
        instance = session.query(State).filter_by(name='Louisiana').first()
        print("{}".format(instance.id))
    except:
        print("failed to add")
    session.commit()
    session.close()
    engine.dispose()
