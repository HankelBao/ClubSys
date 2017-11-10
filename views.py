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
    Me = User(pwd=10, name=2)
    Me['sa']=[]
    Me['sa'].append(1)
    Me['sa'].append("asjdkflll")
    Me.save()
    New = Me.find(2)
    return str(New['sa'])
