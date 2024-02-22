#!/usr/bin/python3
"""
Script distributes an archive to my web servers,
using a function.
"""

from fabric.api import put, run, env
import os

env.hosts = ['54.152.133.156', '54.165.176.3']


def do_deploy(archive_path):
    """ Puts an archive to my web servers and uncompresses it """
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        file_no_ext = filename.split('.')[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/current/")
        run("mkdir -p /data/web_static/releases/{}/".format(file_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            filename, file_no_ext))
        run("rm /tmp/{}".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(filename))
        return True
    except Exception:
        return False
