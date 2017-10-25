from settings import *
import mongoengine as db


def model_init():
    db.connect('clubsys')


class EmbeddedClub(db.DynamicEmbeddedDocument):
    name = db.StringField()
    club = db.ReferenceField(Club)


class EmbeddedMember(db.DynamicEmbeddedDocument):
    name = db.StringField()
    role = db.StringField()
    member = db.ReferenceField(Member)


class EmbeddedActivity(db.DynamicEmbeddedDocument):
    name = db.StringField()
    datetime = db.DateTimeField()
    activity = db.ReferenceField()


class Club(db.DynamicDocument):
    name = db.StringField()
    members = db.EmbeddedDocumentListField(EmbeddedMember)
    activities = db.EmbeddedDocumentListField(EmbeddedActivity)


class Member(db.DynamicDocument):
    student_name = db.StringField()
    student_id = db.StringField()
    password = db.StringField()
    role = db.StringField()
    clubs = db.EmbeddedDocumentListField(EmbeddedMember)


class Activity(db.DynamicDocument):
    name = db.StringField()
    datetime = db.DateTimeField()
    club = db.EmbeddedDocumentField(EmbeddedClub)
    members = db.EmbeddedDocument(EmbeddedMember)
