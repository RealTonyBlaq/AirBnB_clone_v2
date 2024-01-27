#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Defining the city class

    Class attributes:
    ----------------

    ___tablename__ (str): Name of the table
    state_id (str): Column with 60 chars, not null and is a
                    foreign key to states.id
    name (str): Column with 128 chars, not null
    states: Represents a relationship with the State class
    """
    __tablename__ = "cities"
    state_id = Column("state_id", String(60), ForeignKey('states.id'),
                      nullable=False)
    name = Column("name", String(128), nullable=False)
    places = relationship("Place", back_populates="cities", cascade="all, delete")
