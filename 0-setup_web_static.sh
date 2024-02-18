#!/usr/bin/env bash
# Script sets up my web servers for deployment of web_static

if [ "$(nginx -v && echo $?)" -ne 0 ]; then
		sudo apt update
		sudo apt -y install nginx
fi

sudo mkdir -p /data
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

