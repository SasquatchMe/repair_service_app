import datetime

from peewee import Model, CharField, IntegerField, PrimaryKeyField, DateTimeField, SqliteDatabase, ForeignKeyField, \
    AutoField
from config import DATABASE_PATH

db = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class Entity(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(null=False)


class Status(BaseModel):
    id = AutoField(primary_key=True)
    status = CharField(null=False)


class User(BaseModel):
    id = AutoField(primary_key=True)
    login = CharField()
    address = CharField(null=False)
    entity_id = ForeignKeyField(Entity, backref='users')


class Order(BaseModel):
    id = AutoField(primary_key=True)
    login_id = ForeignKeyField(User)
    status_id = ForeignKeyField(Status)
    date_create = DateTimeField(default=datetime.datetime.now())


def create_models():
    db.create_tables(BaseModel.__subclasses__())



