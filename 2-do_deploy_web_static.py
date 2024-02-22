#!/usr/bin/python3
"""
Script distributes an archive to my web servers,
using the function do_deploy().
"""

from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
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
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[1]
        file_no_ext = filename.split('.')[0]
        with cd("/"):
            put(archive_path, "tmp/")
            run("mkdir -p /data/web_static/current/")
            run("mkdir -p /data/web_static/releases/{}/".format(file_no_ext))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(filename,
                                                                file_no_ext))
            run("rm tmp/{}".format(filename))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{} /data/web_static/current"
                .format(filename))
            return True
    except Exception:
        return False
