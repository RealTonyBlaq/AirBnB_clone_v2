#!/usr/bin/python3

""" Module for Database storage """
from sqlalchemy import create_engine
import os

user = os.environ.get


class DBStorage:
    """ Defining the class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing the attributes """
        self.__engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(),
                                      pool_pre_ping=True)
