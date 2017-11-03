from settings import *
from models import *


class Orgs:
    @staticmethod
    def create(name, register_year, description):
        item = ModelCreator.org(name, "", register_year, description)
        mongo.db.orgs.insert(item)

    @staticmethod
    def add_activity(org_name, name, datetime, activity):
        embedbed_activity = EmbeddedModelCreator.activity(name, datetime, activity)
        mongo.db.orgs.update(
            {"name": org_name},
            {
                "$push": {
                    "activities": embedbed_activity
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
