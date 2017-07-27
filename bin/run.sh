#!/bin/bash
export OPENMINED_DB_LOC=$1
export FLASK_APP=./mine/server.py
flask run
