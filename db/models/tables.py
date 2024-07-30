import datetime

from peewee import Model, CharField, IntegerField, PrimaryKeyField, DateTimeField, SqliteDatabase, ForeignKeyField, \
    AutoField
from config import DATABASE_PATH, DEFAULT_STATUSES, DEFAULT_ORDER_TYPES, DEFAULT_BREAKING_TYPES

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


class Object(BaseModel):
    id = AutoField(primary_key=True)
    address = CharField()
    login = CharField()
    entity_id = ForeignKeyField(Entity)


class User(BaseModel):
    id = AutoField(primary_key=True)
    tg_id = CharField()
    object_id = ForeignKeyField(Object)


class OrderType(BaseModel):
    id = AutoField(primary_key=True)
    order_type = CharField(null=False)


class BreakingType(BaseModel):
    id = AutoField(primary_key=True)
    breaking_type = CharField(null=False)


class Order(BaseModel):
    id = AutoField(primary_key=True)
    order_type_id = ForeignKeyField(OrderType)
    breaking_type_id = ForeignKeyField(BreakingType)
    user_id = ForeignKeyField(User)
    status_id = ForeignKeyField(Status)
    date_create = DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    overall_image_path = CharField()
    service_sticker_image_path = CharField()


def create_models():
    db.create_tables(BaseModel.__subclasses__())
    if Status.get_or_none() is None:
        for status in DEFAULT_STATUSES:
            Status.create(status=status)

    if OrderType.get_or_none() is None:
        for order_type in DEFAULT_ORDER_TYPES:
            OrderType.create(order_type=order_type)

    if BreakingType.get_or_none() is None:
        for breaking_type in DEFAULT_BREAKING_TYPES:
            BreakingType.create(breaking_type=breaking_type)
