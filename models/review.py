#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    Defining the Review class to store review information

    class attributes:
    =================

    __tablename__ (str): Name of the table
    place_id (str): Foreign key to table places.id, cannot be null
    user_id (str): Foreign key to the table users.id, cannot be null
    text (str): The review text of 1024 chars max, cannot be null
    user: A relationship between the Class User and Review, if
            a User instance is deleted, all Review instances are
            deleted as well.
    """
    __tablename__ = "reviews"
    place_id = Column("place_id", String(60), ForeignKey("places.id"),
                      nullable=False)
    user_id = Column("user_id", String(60), ForeignKey("users.id"),
                     nullable=False)
    text = Column("text", String(1024), nullable=False)
    user = relationship("User", back_populates="reviews",
                        cascade="all, delete")
