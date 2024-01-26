#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class Place(BaseModel, Base):
    """ Defining the class Place:
    ---------------
    A place to stay
    ---------------
    """
    __tablename__ = "places"
    city_id = Column("city_id", String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column("user_id", String(60), ForeignKey("users.id"), nullable=False)
    name = Column("name", String(128), nullable=False)
    description = Column("description", String(1024))
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
