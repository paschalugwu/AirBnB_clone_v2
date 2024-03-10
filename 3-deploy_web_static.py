#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy
"""
from fabric.api import env
from os.path import exists
from fabric.api import local
from datetime import datetime
from fabric.api import put, run

env.hosts = ['54.161.251.141', '54.237.108.159']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".
                   format(date))

    if result.failed:
        return None
    return "versions/web_static_{}.tgz".format(date)


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
    return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
