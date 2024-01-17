#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column


class State(BaseModel, Base):
    """ Defining the State class that inherits from BaseModel"""
    name = ""
