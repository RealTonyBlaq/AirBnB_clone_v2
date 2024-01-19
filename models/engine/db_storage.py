#!/usr/bin/python3

""" Module for Database storage """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
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
        Session = sessionmaker(self.__engine)
        self.__session = Session()
        if os.environ.get("HBNB_ENV") == "test":
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ Queries the current database session """
        if cls:
            
