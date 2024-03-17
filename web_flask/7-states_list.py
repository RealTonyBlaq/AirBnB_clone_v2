#!/usr/bin/python3
""" Web Flask app that returns list of states from DB """

from flask import abort, Flask
from models import storage
from models.state import State
