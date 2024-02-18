#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric import task
from datetime import date


@task
def do_pack(cc):
	"""
	do_pack - Fab function to generate .tgz archives
	"""
	with cc.cd('~/AirBnB_clone_v2'):
		cc.local('tar -czvf web_static{}'.format())
