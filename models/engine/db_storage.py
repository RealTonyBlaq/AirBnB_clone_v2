#!/usr/bin/python3

""" Module for Database storage """
from sqlalchemy import create_engine, MetaData
import os

user = os.environ.get("HBNB_MYSQL_USER")
host = os.environ.get("HBNB_MYSQL_HOST")
passwd = os.environ.get("HBNB_MYSQL_PWD")
database = os.environ.get("HBNB_MYSQL_DB")


class DBStorage:
    """ Defining the class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing the attributes """
        self.__engine = create_engine("mysql://{}:{}@{}:3306/{}"
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            with self.__engine.connect() as connection:
                statement = delete()
