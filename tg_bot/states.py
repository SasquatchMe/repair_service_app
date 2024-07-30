from telebot.handler_backends import State, StatesGroup
from telebot import custom_filters


class CRMStates(StatesGroup):
    login = State()
    get_phone = State()
    lookup = State()
    order_type = State()
    breaking_type = State()
    desc = State()
    breaking_image = State()
    model_name = State()
    service_sticker_photo = State()
    contact = State()
    comment = State()
    confirm_order = State()
