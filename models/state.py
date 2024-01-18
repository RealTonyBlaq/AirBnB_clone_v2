#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """
    Defining the State class that inherits from BaseModel
    and Base

    class attributes:
    -----------------

    __tablename__ (str): Name of the table
    name (str): Column in the table with max 128 characters, non-null
    cities: Represents a relationship with the Class City (table -> cities)
            the reference is named (state) and if a State object is deleted
            so is its City object.
    """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete")

    @property
    def cities(self):
        """ Returns a list of City instances with state_id = current state.id """
        objects = storage.all()
        for key, value in objects.items():
            obj = key.split('.')[0]
            if obj == 'City"
