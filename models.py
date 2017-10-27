from settings import *


class Clubs(object):
    def __init__(self, name, register_year, description):
        item = {
            "name": name,
            "register_year": register_year,
            "description": description,
            "activities": [],
            "members": []
        }
        self.item = item

    def save(self):
        mongo.db.clubs.insert(self.item)

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
