#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric.api import local


def do_pack():
    """
    do_pack - Fab function to generate .tgz archives
    """
    arch = "web_static_{}.tgz".format(local('date +"%Y%m%d%H%M%S"'))
    local('mkdir -p versions/')
    archive = local('tar -czvf versions/{} web_static'.format(arch))
    if archive.failed:
        return None
    else:
        return "versions/{}".format(arch)


if __name__ == "__main__":
    do_pack()
