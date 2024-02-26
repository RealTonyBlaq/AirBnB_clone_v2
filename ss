#!/usr/bin/env bash

prev="$(cat ~/.bashrc | grep COMMIT | cut -d '=' -f2)"
((new = 4441 + prev))
echo "$new"
