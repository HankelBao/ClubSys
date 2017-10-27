from settings import *

class EmeddedModelCreator():
    @staticmethod
    def org(name, org):
        return {
            "name": name,
            "org": org,
        }

    @staticmethod
    def member(name, role, member):
        return {
            "name": name,
            "role": role,
            "member": member,
        }

    @staticmethod
    def activity(name, datetime, activity):
        return {
            "name": name,
            "datetiem": datetime,
            "activity": activity,
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
            "student_name": student_name,
            "student_id": student_id,
            "password": password,
        }

    @staticmethod
    def activity(name, datetime):
        return {
            "name": name,
            "datetime": datetime,
        }
