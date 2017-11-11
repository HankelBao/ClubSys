import orm as mongodb

class EmbeddedOrg(mongodb.EmbeddedDocument):
    name = mongodb.Field()

class EmbeddedMember(mongodb.EmbeddedDocument):
    name = mongodb.Field()
    role = mongodb.Field()

class EmbeddedActivity(mongodb.EmbeddedDocument):
    name = mongodb.Field()
    datetime = mongodb.Field()

class Org(mongodb.Document):
    name = mongodb.Field()
    mode = mongodb.Field()
    register_year = mongodb.Field()
    description = mongodb.Field()
    activities = mongodb.ListField()
    members = mongodb.ListField()

class Member(mongodb.Document):
    name = mongodb.Field()
    sys_id = mongodb.Field()
    password = mongodb.Field()
    orgs = mongodb.ListField()
    activities = mongodb.ListField()

class Acitivity(mongodb.Document):
    name = mongodb.Field()
    datetime = mongodb.Field()
    members = mongodb.ListField()
    orgs = mongodb.ListField()

class User(mongodb.Document):
    name = mongodb.Field()


class EmbeddedUser(mongodb.EmbeddedDocument):
    name = mongodb.Field()
