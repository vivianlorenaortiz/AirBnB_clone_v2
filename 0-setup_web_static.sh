#!/usr/bin/env bash
# Prepare your web servers
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "testing." | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static {\n\t\talias\/data\/web_static\/current\/;\n\t}/" /etc/nginx/sites-available/default
sudo service nginx restart
