from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from db.query_to_db.query_to_db import get_user_phone_by_tg_id, get_object_phone_by_tg_id


def phone_num_keyboard(tg_id):
    user_phone = get_user_phone_by_tg_id(tg_id)
    object_phone = get_object_phone_by_tg_id(tg_id)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton(user_phone), KeyboardButton(object_phone))
    return markup
