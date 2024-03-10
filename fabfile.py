#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""
from fabric.api import env, local, run

env.hosts = ['54.161.251.141', '54.237.108.159']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number == 0 or number == 1:
        local('ls -1t versions | tail -n +2 | xargs rm -f --')
        run('ls -1t /data/web_static/releases | tail -n +2 | xargs rm -rf --')
    else:
        number += 1
        local('ls -1t versions | tail -n +{} | xargs rm -f --'.format(number))
        run('ls -1t /data/web_static/releases | tail -n +{} | xargs rm -rf --'.
            format(number))
