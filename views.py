from settings import *
from models import *
from flask import Flask
from flask import jsonify
from flask import request


class ClubsView:
    @staticmethod
    @app.route('/ajax/clubs/create/')
    def create_club():
        name = request.args.get('name')
        register_year = request.args.get('register_year')
        description = request.args.get('description')

        club = Clubs.create(name, register_year, description)
        club_id = mongo.db.clubs.insert_one(club).inserted_id
        return str(club_id)

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
        mongo.db.clubs.remove({"name": club_name})
        return 'OK'

    @staticmethod
    @app.route('/ajax/clubs/change_name')
    def change_club_name():
        club_name = request.args.get('name')
        club_new_name = request.args.get('new')

        mongo.db.clubs.update(
            {"name": club_name},
            {
                "$set": {
                    "name": club_new_name
                }
            }
        )
        return 'OK'
