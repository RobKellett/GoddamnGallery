import os
from peewee import *

database = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = database

class Image(BaseModel):
    #color = CharField(null=True)
    path = CharField()
    thumb = CharField(null=True)
    gallery = CharField()
    parent = CharField(null=True)
    x = IntegerField(null=True)
    y = IntegerField(null=True)
    r = IntegerField(null=True)
    g = IntegerField(null=True)
    b = IntegerField(null=True)

    class Meta:
        db_table = 'images'

class Tag(BaseModel):
    name = CharField()
    slug = CharField()

    class Meta:
        db_table = 'tags'

class TagImage(BaseModel):
    tag = ForeignKeyField(Tag)
    image = ForeignKeyField(Image)

    class Meta:
        db_table = 'tag_image'

class User(BaseModel):
    name = CharField(unique=True)
    email = CharField()
    hash = CharField()

    class Meta:
        db_table = "users"

class GoddamnDatabase(object):
    def __init__(self, path, **connect_args):
        if path == None:
            path = os.path.dirname(__file__)
        self.dbname = os.path.join(path, 'gallery.db')
        self.connect_args = connect_args
    def __enter__(self):
        database.init(self.dbname, **self.connect_args)
        database.connect()
        return database
    def __exit__(self, t, v, tb):
        database.close()