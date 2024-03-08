#!/usr/bin/python3
'''Fabric script that deploys an archive to my web servers'''
from fabric.api import local, put, run, env
from fabric.decorators import runs_once
from datetime import datetime
import re
from os import path

# Define the list of web servers
env.hosts = [
    '54.161.251.141',
    '54.237.108.159'
]


@runs_once
def do_pack():
    '''Generates a .tgz archive from the contents of the web_static folder'''
    # Create a directory to store the generated archive
    local("mkdir -p versions")
    # Create the archive file using the current date and time
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)

    # Check if the archive creation was successful
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    '''Distribute an archive to web servers'''
    # Check if the archive file exists
    if not path.exists(archive_path):
        return False

    # Extract the filename from the archive path
    file_name = re.search(r'versions/(\S+).tgz', archive_path)
    if file_name is None:
        return False
    file_name = file_name.group(1)

    # Upload the archive to the remote /tmp directory
    res = put(local_path=archive_path, remote_path="/tmp/{}.tgz"
              .format(file_name))
    if res.failed:
        return False

    # Create a directory to extract the archive contents on the server
    res = run("mkdir -p /data/web_static/releases/{}".format(file_name))
    if res.failed:
        return False

    # Extract the archive contents to the specified directory
    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(file_name, file_name))
    if res.failed:
        return False

    # Remove the uploaded archive file from the server
    res = run('rm -rf /tmp/{}.tgz'.format(file_name))
    if res.failed:
        return False

    # Move the extracted contents to the appropriate directory
    res = run(('mv /data/web_static/releases/{}/web_static/* ' +
              '/data/web_static/releases/{}/')
              .format(file_name, file_name))
    if res.failed:
        return False

    # Remove the obsolete web_static directory
    res = run('rm -rf /data/web_static/releases/{}/web_static'
              .format(file_name))
    if res.failed:
        return False

    # Remove the symbolic link to the current release
    res = run('rm -rf /data/web_static/current')
    if res.failed:
        return False

    # Create a new symbolic link to the current release
    res = run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
              .format(file_name))
    if res.failed:
        return False

    # Print confirmation message if deployment was successful
    print('New version deployed!')
    return True
