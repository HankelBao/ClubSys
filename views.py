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
    Me['sa'].append(2)
    Me['sa'].append("asjdkflll")
    Me['sa'].append(EmbeddedUser(name=2, se=1))
    Me.save()
    return str(1)
