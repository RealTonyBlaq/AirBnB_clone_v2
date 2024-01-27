#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = Column("place_id", String(60), ForeignKey("places.id"))
    user_id = ""
    text = Column("text", String(1024), nullable=False)
