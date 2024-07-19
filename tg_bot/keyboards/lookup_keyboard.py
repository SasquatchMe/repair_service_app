from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def lookup_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    row = [KeyboardButton('Создать заявку'), KeyboardButton('Что-то'), KeyboardButton('Еще что-то')]
    markup.add(*row)
    return markup
