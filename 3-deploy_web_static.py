#!/usr/bin/python3
""" Script deploys an archive to my servers """

from fabric.api import env, run, put, local
from datetime import datetime

env.hosts = ['54.152.133.156', '54.165.176.3']

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

def deploy():
    """ Performs the do_deploy and do_pack functions """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
