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
