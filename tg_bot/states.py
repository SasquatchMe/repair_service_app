from telebot.handler_backends import State, StatesGroup
from telebot import custom_filters


class CRMStates(StatesGroup):
    login = State()
    lookup = State()
    brand_name = State()
    model_title = State()
    desc = State()
    model_image = State()
    confirm_order = State()
