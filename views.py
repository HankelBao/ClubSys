from settings import *
from models import *
import command
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from orm import *

@app.route('/')
def index():
    Me = Member(name="Hankel", sys_id="20164001", password="pwd")
    return str(Me['name'])
