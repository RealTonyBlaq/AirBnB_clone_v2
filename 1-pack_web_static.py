#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric.api import local


@task
def do_pack():
    """
    do_pack - Fab function to generate .tgz archives
    """
    with cd('~/AirBnB_clone_v2'):
        result = local('date +"%Y%m%d%H%M%S"')
        local('tar -czvf web_static{}.tgz ./web_static/'.format(result))
        local('mkdir -p versions/')
        local('mv web_static{}.tgz versions/'.format(result))
