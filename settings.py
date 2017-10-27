from flask import Flask
from flask_pymongo import PyMongo

app = Flask("clubsys")
mongo = PyMongo(app)
