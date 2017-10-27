from settings import *
from models import *
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template


@app.route('/')
def test():
    return render_template('test.html')

