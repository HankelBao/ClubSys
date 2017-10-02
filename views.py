from settings import *
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from models import *


@app.route('/ajax/create_club/')
def create_club():
    name = request.args.get('name')
    register_year = request.args.get('register_year')
    description = request.args.get('description')

    doc = {
        "name": name,
        "register_year": register_year,
        "description": description,
        "doc2": {
            "aaaa": "bbb"
        }
    }
    mongo.db.clubs.insert(doc)

    #club = Clubs.create(name, register_year, description)
    #created_club_id = Clubs.insert(club)

    return str(created_club_id)


@app.route('/ajax/show_clubs/')
def show_clubs():
    names = []
    for club in mongo.db.clubs.find():
        names.append(club['name'])
    return jsonify(names)


@app.route('/ajax/create_member')
def create_member():
    id = request.args.get('id')
    name = request.args.get('name')
    password = request.args.post('password')


@app.route('/test/')
def test_ajax():
    names = []
    for club in mongo.db.clubs.find():
        try:
            names.append(club['english_name'])
        except:
            names.append(club['name'])
    return jsonify(names)
