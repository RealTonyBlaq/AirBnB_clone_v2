#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from 


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = ""
    name = ""
