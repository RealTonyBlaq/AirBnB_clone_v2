#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ Defines the class Amenity """
    __tablename__ = "amenities"
    name = ""
