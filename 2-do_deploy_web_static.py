#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.161.251.141', '54.237.108.159']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[-1]
            no_ext = file_name.split(".")[0]
            run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
                format(file_name, no_ext))
            run("rm /tmp/{}".format(file_name))
            run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(no_ext, no_ext))
            run("rm -rf /data/web_static/releases/{}/web_static".
                format(no_ext))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
                format(no_ext))
            return True
        except Exception as e:
            print("Exception occurred: {}".format(e))
    return False
