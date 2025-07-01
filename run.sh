#!/bin/bash

read -p "Install Python3 if not found? (yes/no): " reply

if ! command -v python3 >/dev/null; then
  if [ "$reply" = "yes" ]; then
    sudo apt update
    sudo apt install -y python3 python3-pip
  else
    echo "Python3 is required. Exiting."
    exit 1
  fi
fi

pip3 install flask
python3 app.py
