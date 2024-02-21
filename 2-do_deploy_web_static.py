#!/usr/bin/python3
"""
Script distributes an archive to my web servers,
using the function do_deploy()
"""

from fabric.api import run
import os


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
