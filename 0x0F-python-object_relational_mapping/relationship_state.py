#!/usr/bin/python3
"""Modules that declare a class states
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from relationship_city import Base


class State(Base):
    """Defines a class State
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

# one to many relationship
    cities = relationship(
        'City',
        backref='state',
        cascade='all, delete'
        )


if __name__ == "__main__":
    pass
