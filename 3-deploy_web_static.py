#!/usr/bin/python3
""" Script deploys an archive to my servers """

from fabric.api import env
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack

env.hosts = ['54.152.133.156', '54.165.176.3']

def deploy():
    """ Performs the do_deploy and do_pack functions """
    archive_path = do_pack()
    if archive_path is None:
        return False
    
