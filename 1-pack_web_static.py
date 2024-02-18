#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric import task


@task
def do_pack(cc):
	"""
	do_pack - Fab function to generate .tgz archives
	"""
	c = cc.local('')
