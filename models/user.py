#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column("email", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    first_name = Column("first_name", String(128))
    last_name = Column("last_name", String(128))
    places = relationship("Place", back_populates="users",
                          cascade="all, delete")
    reviews = relationship("Review", back_populates="user",
                           cascade="all, delete")
