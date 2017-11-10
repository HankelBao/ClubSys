# TODO: rewrite the model using my new ORM
from settings import *


class EmbeddedModelCreator():
    @staticmethod
    def org(name):
        return {
            "name": name,
        }

    @staticmethod
    def member(name, role):
        return {
            "name": name,
            "role": role,
        }

    @staticmethod
    def activity(name, datetime):
        return {
            "name": name,
            "datetime": datetime,
        }


class ModelCreator():
    @staticmethod
    def org(name, mode, register_year, description):
        return {
            "name": name,
            "type": mode,
            "register_year": register_year,
            "description": description,
            "activities": [],
            "members": []
        }

    @staticmethod
    def member(student_name, student_id, password):
        return {
            "name": student_name,
            "sys_id": student_id,
            "password": password,
            "orgs": [],
            "activities": [],
        }

    @staticmethod
    def activity(name, datetime):
        return {
            "name": name,
            "datetime": datetime,
            "members": [],
            "orgs": [],
        }
