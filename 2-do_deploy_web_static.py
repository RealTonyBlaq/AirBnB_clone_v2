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
    env.host = "54.152.133.156"
    filename = archive_path.split(".")[0]
    with cd("/"):
        put(archive_path, "tmp/")
        run("tar -xzf {} /data/web_static/releases/{}".format())
