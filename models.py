from settings import *
import mongoengine as db

def model_init():
    db.connect('clubsys')

class Club(db.Document):
    name = db.StringField()
    members = db.EmbeddedDocumentListField(EmbeddedMember)
    activities = db.EmbeddedDocumentListField(EmbeddedActivity)

class Member(db.Document):
    student_name = db.StringField()
    student_id = db.StringField()
    password = db.StringField()
    role = db.StringField()
    clubs = db.EmbeddedDocumentListField(EmbeddedMember)


class Activity(db.Document):
    name = db.StringField()
    datetime = db.DateTimeField()
    club = db.EmbeddedDocumentField(EmbeddedClub)
    members = db.EmbeddedDocument(EmbeddedMember)

class EmbeddedClub(db.EmbeddedDocument):
    name = db.StringField()
    club = db.ReferenceField(Club)

class EmbeddedMember(db.EmbeddedDocument):
    name = db.StringField()
    role = db.StringField()
    member = db.ReferenceField(Member)

class EmbeddedActivity(db.EmbeddedDocument):
    name = db.StringField()
    datetime = db.DateTimeField()
    activity = db.ReferenceField(Activity)
    club = db.ReferenceField(Club)


