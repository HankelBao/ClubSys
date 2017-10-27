from settings import *


class Clubs:
    @staticmethod
    def get_id_by_name(name):
        for club in mongo.db.clubs.find({"name": name}):
            return club["_id"]

    @staticmethod
    def create(name, register_year="2016", description=None):
        item = {
            "name": name,
            "register_year": register_year,
            "description": description,
            "activities": [],
            "members": []
        }
        try:
            mongo.db.clubs.insert(item)
        except:
            return False
        else:
            return True

    @staticmethod
    def delete(club_name):
        mongo.db.clubs.remove({"name": club_name})

    @staticmethod
    def change_name(club_name, club_new_name):
        mongo.db.clubs.update(
            {"name": club_name},
            {
                "$set": {
                    "name": club_new_name
                }
            }
        )

    @staticmethod
    def add_activity(club_name, activity_id, activity_name):
        embeded_activity = {
            "id": activity_id,
            "name": activity_name
        }
        mongo.db.clubs.update(
            {"name": club_name},
            {
                "$push": {
                    "activities": embeded_activity
                }
            }
        )

    @staticmethod
    def add_member(club_name, member_id, member_name, member_role):
        embeded_member = {
            "id": member_id,
            "name": member_name,
            "role": member_role
        }
        mongo.db.clubs.update(
            {"name": club_name},
            {
                "$push": {
                    "members": embeded_member
                }
            }
        )


class Members:
    @staticmethod
    def create(sys_id, name):
        return {
            "sys_id": sys_id,
            "name": name,
            "clubs": [],
        }

    @staticmethod
    def insert(item):
        created_member_id = mongo.db.members.insert_one(item).inserted_id
        return created_member_id

    @staticmethod
    def add_club(member_name, club_id, club_name):
        embeded_club = {
            "id": club_id,
            "name": club_name,
        }
        mongo.db.clubs.update(
            {"name": member_name},
            {
                "$push": {
                    "activities": embeded_club
                }
            }
        )


class Activities:
    @staticmethod
    def create(club_id, activity_name, activity_date, members):
        return {
            "club_id": club_id,
            "activity_name": activity_name,
            "activity_date": activity_date,
            "members": members
        }
