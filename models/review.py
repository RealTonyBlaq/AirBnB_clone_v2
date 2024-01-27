#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = ""
    user_id = ""
    text = Column("text", String(1024), nullable=False)
