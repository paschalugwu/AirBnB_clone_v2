#!/usr/bin/python3
'''Fabric script that deploys an archive to web servers'''
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

    # Delete the existing directories if they exist
    res = run('rm -rf /data/web_static/releases/{}/images'
              .format(file_name))
    if res.failed:
        return False

    res = run('rm -rf /data/web_static/releases/{}/styles'
              .format(file_name))
    if res.failed:
        return False

    # Now you can move the new directories
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
