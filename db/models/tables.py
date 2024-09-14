import datetime

from peewee import Model, CharField, DateTimeField, SqliteDatabase, ForeignKeyField, \
    AutoField, BooleanField

from config import DATABASE_PATH, DEFAULT_STATUSES, DEFAULT_ORDER_TYPES, DEFAULT_BREAKING_TYPES, DEFAULT_ENTITIES

db = SqliteDatabase(DATABASE_PATH)
db.pragma('foreign_keys', 1, permanent=True)


class BaseModel(Model):
    class Meta:
        database = db


class Entity(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()


class Status(BaseModel):
    id = AutoField(primary_key=True)
    status = CharField()


class Object(BaseModel):
    id = AutoField(primary_key=True)
    address = CharField()
    login = CharField()
    entity_id = ForeignKeyField(Entity, on_delete='CASCADE')
    phone = CharField()


class User(BaseModel):
    id = AutoField(primary_key=True)
    phone = CharField()
    tg_id = CharField(null=True)
    object_id = ForeignKeyField(Object, on_delete='CASCADE')


class OrderType(BaseModel):
    id = AutoField(primary_key=True)
    order_type = CharField()


class BreakingType(BaseModel):
    id = AutoField(primary_key=True)
    breaking_type = CharField()


class Order(BaseModel):
    id = AutoField(primary_key=True)
    order_type_id = ForeignKeyField(OrderType)
    breaking_type_id = ForeignKeyField(BreakingType)
    user_id = ForeignKeyField(User, null=True)
    object_id = ForeignKeyField(Object, on_delete='CASCADE')
    status_id = ForeignKeyField(Status, default=1)
    date_create = DateTimeField(default=datetime.datetime.now)
    breaking_image_path = CharField(null=True)
    service_sticker_image_path = CharField(null=True)
    model_name = CharField()
    desc = CharField(null=True)
    phone = CharField()
    comment = CharField(null=True)
    decline_desc = CharField(null=True)
    worktime = CharField(null=True)
    est_date_complete = DateTimeField(null=True)
    date_complete = DateTimeField(null=True)
    confirm_from_client = BooleanField(default=False)


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

    if Entity.get_or_none() is None:
        for entity in DEFAULT_ENTITIES:
            Entity.create(name=entity)
