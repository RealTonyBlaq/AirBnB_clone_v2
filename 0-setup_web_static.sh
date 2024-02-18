#!/usr/bin/env bash
# Script sets up my web servers for deployment of web_static

if [ -x "$(command -v nginx)" ]; then
		sudo apt update
		sudo apt -y install nginx
fi

# Creating directories if th
sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo "Testing my Nginx congiguration" > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]; then
		rm /data/web_static/current
		sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

chown -hR ubuntu:ubuntu /data/

