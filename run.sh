#!/bin/bash
current_dir="$PWD"

gnome-terminal -- sqlmapapi -s -H 127.0.0.1 -p 7000
cd "$current_dir"/tool/back
gnome-terminal -- python3 server.py
sleep 10
cd "$current_dir"/tool
gnome-terminal -- bash -c "npm install && npm start"

