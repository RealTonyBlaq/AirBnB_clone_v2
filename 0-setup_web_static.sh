#!/usr/bin/env bash
# Script sets up my web servers for deployment of web_static

# Checking if Nginx is installed, else
if ! [ -x "$(command -v nginx)" ]; then
		sudo apt update
		sudo apt -y install nginx
fi

# Creating directories if they don't exist already
sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creating a fake HTML file to test my nginx configuration
sudo echo "Testing my Nginx congiguration" > /data/web_static/releases/test/index.html

# Checks if a sy,
if [ -L "/data/web_static/current" ]; then
		rm /data/web_static/current
		sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

chown -hR ubuntu:ubuntu /data/

