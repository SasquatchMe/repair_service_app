from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from db.query_to_db.query_to_db import get_breaking_types


def breaking_type_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    breaking_types = get_breaking_types()
    buttons = [KeyboardButton(breaking_type.breaking_type) for breaking_type in breaking_types]
    markup.add(*buttons)
    return markup
