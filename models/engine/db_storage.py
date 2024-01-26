#!/usr/bin/python3

""" Module for Database storage """
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = [State, City, User, Place]

user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
passwd = getenv("HBNB_MYSQL_PWD")
database = getenv("HBNB_MYSQL_DB")


class DBStorage:
    """ Defining the class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing the attributes """
        self.__engine = create_engine("mysql://{}:{}@{}:3306/{}"
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
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
                objs[key] = row
        else:
            objs = {}
            for clas in classes:
                ins = self.__session.query(clas)
                for result in ins:
                    key = "{}.{}".format(clas.__name__, result.id)
                    objs[key] = result
        return objs

    def new(self, obj):
        """ Adds a new object to the current database session """
        """if '_sa_instance_state' in obj.__dict__.keys():
            del obj.__dict__['_sa_instance_state']"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
