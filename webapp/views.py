#!/usr/bin/python
# coding: utf-8
""" 
    Filename:     views.py
    Description:  This file is one of the views file that can contain the
                  routes for the application
    Requirements: 
    Author:       MakerBro
"""
import os
import csv
import json
import flask
from application import app
from settings import APP_STATIC, APP_DATA

# importing application wide parameters and global variables that have been
# defined in application.py
message = app.config['HELLO_WORLD']

@app.route('/')
def webapp():
    with open(os.path.join(APP_DATA, 'data.txt')) as f:
        data = f.readlines()
        fieldnames = ('city','county','url')
        reader = csv.DictReader(data, fieldnames)
        json_str = json.dumps( list(reader) )
    return flask.render_template('main.html', data=json.loads(json_str))

