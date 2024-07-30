from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from db.query_to_db.query_to_db import get_order_types


def order_type_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    order_types = get_order_types()
    buttons = [KeyboardButton(order_type.order_type) for order_type in order_types]
    markup.add(*buttons)
    return markup
