from db.models.tables import *


def get_order_types():
    order_types = OrderType.select()
    return order_types


def get_breaking_types():
    breaking_types = BreakingType.select()
    return breaking_types


def get_order_type_id(order_type_text):
    order_type: OrderType = OrderType.get(OrderType.order_type == order_type_text)
    return order_type.id


def get_breaking_type_id(breaking_type_text):
    breaking_type = BreakingType.get(BreakingType.breaking_type == breaking_type_text)
    return breaking_type.id


def get_user_phone_by_tg_id(tg_id):
    user = User.get(User.tg_id == tg_id)
    return user.phone


def get_user_id_by_tg_id(tg_id):
    user = User.get(User.tg_id == tg_id)
    return user.id


def get_order_by_order_id(order_id):
    order = Order.get(Order.id == order_id)
    return order


def get_object_id_by_tg_id(tg_id):
    user = User.get(User.tg_id == tg_id)
    return user.object_id


def get_object_phone_by_tg_id(tg_id):
    user = User.get(User.tg_id == tg_id)
    object = Object.get(Object.id == user.object_id)
    return object.phone
