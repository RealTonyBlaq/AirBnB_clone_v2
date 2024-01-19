#!/usr/bin/python3

""" Module for Database storage """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, Amenity, Review
        }

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
            instance = self.__session.query(cls)
            cls_dict = {}
            for row in instance:
                key = "{}.{}".format(cls.__name__, row.id)
                value = dict(row)
                cls_dict[key] = value
        else:


