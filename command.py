"""
Command.py
List all the commands for each modules
"""
from settings import *
from models import *


class Orgs:
    @staticmethod
    def create(name, register_year, description):
        item = ModelCreator.org(name, "asdjkfl", register_year, description)
        mongo.db.orgs.insert(item)

    @staticmethod
    def add_activity(org_name, name, datetime):
        embedbed_activity = EmbeddedModelCreator.activity(name, datetime)
        mongo.db.orgs.update(
            {"name": org_name},
            {
                "$push": {
                    "activities": embedbed_activity
                }
            }
        )

    @staticmethod
    def add_member(org_name, member_name, member_role):
        embedded_member = EmbeddedModelCreator.member(member_name, member_role)
        mongo.db.orgs.update(
            {"name": org_name},
            {
                "$push": {
                    "members": embedded_member
                }
            }
        )


class Members:
    @staticmethod
    def create(student_name, student_id, password):
        item = ModelCreator.member(student_name, student_id, password)
        mongo.db.members.insert(item)

    @staticmethod
    def add_org(member_name, name):
        embedded_org = EmbeddedModelCreator.org(name)
        mongo.db.members.update(
            {"name": member_name},
            {
                "$push": {
                    "orgs": embedded_org
                }
            }
        )

    @staticmethod
    def add_activity(member_name, activity_name, activity_datetime):
        embedded_activity = EmbeddedModelCreator.activity(activity_name, activity_datetime)
        mongo.db.members.update(
            {"name": member_name},
            {
                "$push": {
                    "activities": embedded_activity
                }
            }
        )

class Activities:
    @staticmethod
    def create(name, datetime):
        item = ModelCreator.activity(name, datetime)
        mongo.db.activities.insert(item)

    @staticmethod
    def add_org(activity_name, org_name):
        item = EmbeddedModelCreator.org(org_name)
        mongo.db.activities.update(
            {"name": activity_name},
            {
                "$push": {
                    "orgs": item
                }
            }
        )

    @staticmethod
    def add_member(activity_name, name, role):
        item = EmbeddedModelCreator.member(name, role)
        mongo.db.activities.update(
            {"name": activity_name},
            {
                "$push": {
                    "members": item
                }
            }
        )
