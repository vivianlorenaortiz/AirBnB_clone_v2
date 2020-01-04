#!/usr/bin/python3
"""
Compress before sending
"""
from fabric.api import *
from time import strftime


def do_pack():
    """
    """
    datetime = time.strftime("%Y%m%d%H%M%S")
    new_file = "web_static_" + datatime + ".tgz"
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(new_file))
        return ("version/{}".format(new_file))
    except:
        return None
