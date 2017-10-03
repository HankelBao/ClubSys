from settings import *


class Clubs:
    @staticmethod
    def create(name, register_year="2016", description=None):
        return {
            "name": name,
            "register_year": register_year,
            "description": description,
            "activities": [],
            "members": []
        }

    @staticmethod
    def create_activity_embeded(activity_id, name):
        return {
            "id": activity_id,
            "name": name
        }

    @staticmethod
    def add_activity(club_name, activity_id, activity_name):
        mongo.db.clubs.update(
            {"name": club_name},
            {
                "$push": {
                    "activities": Clubs.create_activity_embeded(activity_id, activity_name)
                }
            }
        )


class Members():
    @staticmethod
    def create(sys_id, name):
        return {
            "sys_id": sys_id,
            "name": name,
        }

    @staticmethod
    def insert(item):
        created_member_id = mongo.db.members.insert_one(item).inserted_id
        return created_member_id
