#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric import task


@task
def do_pack(cc):
	"""
	do_pack - Fab function to generate .tgz archives
	"""
	with cc.cd('~/AirBnB_clone_v2'):
		result = cc.local('date +"%Y%m%d%H%M%S"')
		cc.local('tar -czvf web_static{}.tgz ./web_static/'.format(result))
		cc.local('mkdir -p versions/')
		cc.local('mv web_static{}.tgz versions/'.format(result))
