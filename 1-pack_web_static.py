#!/usr/bin/python3
"""
This module creates a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the timestamp for the archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        # Create the .tgz archive
        print(f"Packing web_static to {archive_path}")
        c.run(f"tar -cvzf {archive_path} web_static")

        # Check if the archive was created successfully
        if os.path.exists(archive_path):
            print(f"web_static packed: {archive_path}
                  -> {os.path.getsize(archive_path)}Bytes")
            return archive_path
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
