#!/usr/bin/python3

""" Module for Database storage """
import MySQLdb

class DBStorage:
    """ Defining the class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializing the attributes """
        self.__engine = create_engine("mysql://")
