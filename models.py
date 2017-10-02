from settings import *


class BaseModel():
    @staticmethod
    def create_item():
        item = {}
        return item

    @staticmethod
    def create():
        pass


class Clubs(BaseModel):
    @staticmethod
    def create(name, register_year="2016", description=None):
        item = {
            "name": name,
            "register_year": register_year,
            "description": description
        }
        return item

    @staticmethod
    def insert(item):
        created_club_id = mongo.db.clubs.insert_one(item).inserted_id
        return created_club_id


class Members(BaseModel):
    @staticmethod
    def create_item(id, name):
        item = {
            "id": id,
            "name": name,
        }
        return item

    @staticmethod
    def create(id, name):
        item = Members.create_item(id, name)
        created_member_id = mongo.db.members.insert_one(item).inserted_id
        return created_member_id


class Activities():
    @staticmethod
    def create_activity(name, club_id, datetime=None, room=None):
        item = {
            "name": name,
            "datetime": datetime,
            "room": room,
            "club_id": club_id
        }
        created_activity_id = mongo.db.activity.insert_one(item).inserted_id
        return created_activity_id
