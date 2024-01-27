#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base


class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = ""
    user_id = ""
    text = ""
