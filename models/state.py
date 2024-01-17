#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Defining the State class that inherits from BaseModel
    and Base
    """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete")
