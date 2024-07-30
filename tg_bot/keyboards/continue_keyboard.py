from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def continue_keyboard():
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(KeyboardButton('Пропустить'))
    return markup