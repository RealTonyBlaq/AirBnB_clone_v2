#!/usr/bin/python3

""" Module for Database storage """
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = [BaseModel, User, Place, State, City, Amenity, Review]

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
            objs = {}
            for row in instance:
                key = "{}.{}".format(cls.__name__, row.id)
                value = dict(row)
                objs[key] = value
        else:
            for clas in classes:
                ins = self.__session.query(clas)
                objs = {}
                for result in ins:
                    key = "{}.{}".format(clas.__name__, result.id)
                    value = dict(row)
                    objs[key] = value
        return objs

    def new(self, obj):
        """ Adds a new object to the current database session """
        if obj:
            new_obj = obj.__class__(obj.to_dict())
            self.__session.add(new_obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current database session """
        if obj:
            self.__session.delete(obj.__class__)

    def reload(self):
        """ """
