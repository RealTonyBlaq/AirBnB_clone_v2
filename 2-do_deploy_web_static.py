#!/usr/bin/python3
"""
Script distributes an archive to my web servers,
using the function do_deploy()
"""

from fabric.api import *
import os


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    env.user = "ubuntu"
    env.hosts = ["54.152.133.156", ]
    filename = archive_path.split(".")[0]
    with cd("/"):
        put(archive_path, "tmp/")
        run("tar -xzf {} /data/web_static/releases/{}".format(archive_path, filename))
        sudo("rm {}".format(archive_path))
        sudo("rm /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_static/current".format(filename))
