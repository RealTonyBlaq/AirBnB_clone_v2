#!/usr/bin/env bash
# Script sets up my web servers for deployment of web_static

if [ "$(nginx -v && echo $?)" -ne 0 ]; then
		
