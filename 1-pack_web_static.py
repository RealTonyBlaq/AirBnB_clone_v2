#!/usr/bin/python3
""" Script generates a .tgz archive using fabric """

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    do_pack - Fab function to generate .tgz archives
    """
    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    arch = "web_static_{}.tgz".format(time)
    local('mkdir -p versions/')
    archive = local('tar -czvf versions/{} web_static'.format(arch))
    if archive.failed:
        return None
    else:
        return "versions/{}".format(arch)


if __name__ == "__main__":
    do_pack()
