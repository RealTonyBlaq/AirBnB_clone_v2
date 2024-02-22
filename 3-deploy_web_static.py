#!/usr/bin/python3
""" Script deploys an archive to my servers """

from fabric.api import env, run, put, local
from datetime import datetime
import os

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


def do_deploy(archive_path):
    """ Puts an archive to my web servers and uncompresses it """
    if not os.path.exists(archive_path):
        return False
    try:
        fileN = archive_path.split("/")[-1]
        wtht_ext = fileN.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, wtht_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(fileN, path, wtht_ext))
        run('rm /tmp/{}'.format(fileN))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, wtht_ext))
        run('rm -rf {}{}/web_static'.format(path, wtht_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, wtht_ext))
        return True
    except Exception:
        return False


def deploy():
    """ Performs the do_deploy and do_pack functions """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
