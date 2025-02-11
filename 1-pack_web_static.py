#!/usr/bin/python3
# Fabric script to generate a .tgz archive from web_static

from fabric import task
from datetime import datetime

@task
def do_pack(c):  # 'c' is required in Fabric 2+
    """Generate a .tgz archive from web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)

    c.run("mkdir -p versions")  # Use 'c.run()' instead of 'local'
    result = c.run(f"tar -czvf {path} web_static", warn=True)

    if result.ok:
        return path
    return None
