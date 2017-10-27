from settings import *
from models import *
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template


class ClubsView:
    @staticmethod
    @app.route('/ajax/clubs/create/')
    def create_club():
        name = request.args.get('name')
        register_year = request.args.get('register_year')
        description = request.args.get('description')

        Clubs.create(name, register_year, description)
        return "OK"

    @staticmethod
    @app.route('/ajax/clubs/show/')
    def show_clubs():
        clubs = []
        for club in mongo.db.clubs.find():
            item = {
                "_id": str(club['_id']),
                "name": club['name']
            }
            clubs.append(item)


        return jsonify(clubs)

    @staticmethod
    @app.route('/ajax/clubs/delete')
    def delete_club_by_name():
        club_name = request.args.get('name')
        Clubs.delete(club_name)
        return 'OK'

    @staticmethod
    @app.route('/ajax/clubs/change_name')
    def change_club_name():
        club_name = request.args.get('name')
        club_new_name = request.args.get('new')
        Clubs.change_name(club_name, club_new_name)
        return 'OK'
