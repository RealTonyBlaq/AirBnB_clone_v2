#!/usr/bin/python3
"""
Script distributes an archive to my web servers,
using the function do_deploy()
"""

from fabric.api import run


def do_deploy(archive_path):
