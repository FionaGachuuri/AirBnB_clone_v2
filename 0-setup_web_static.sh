#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
