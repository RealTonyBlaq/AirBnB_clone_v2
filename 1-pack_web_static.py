#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric.api import local


def do_pack():
    """
    do_pack - Fab function to generate .tgz archives
    """
    time = local('date +"%Y%m%d%H%M%S"')
    local('mkdir -p versions/')
    local('tar -czvf versions/web_static{}.tgz ./web_static/'.format(time))
