#!/usr/bin/python3
""" Script deploys an archive to my servers """

from fabric.api import env



env.hosts = ['54.152.133.156', '54.165.176.3']


def deploy():
    """ Performs the do_deploy and do_pack functions """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
