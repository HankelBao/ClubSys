from settings import *

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Document(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Document, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        mongo.db.__getattr__(self.__table__).insert(self)

    @classmethod
    def find(cls, pk):
        rs = mongo.db.__getattr__(cls.__table__).find({"name": pk})
        return cls(**rs[0])

class Field(object):
    def __init__(self):
        pass

class User(Document):
    name = Field()