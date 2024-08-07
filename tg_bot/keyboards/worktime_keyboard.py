from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def worktime_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    worktime = [
        '8:00-12:00',
        '12:00-16:00',
        '16:00-20:00',
        'Любое'
    ]
    buttons = [KeyboardButton(time) for time in worktime]
    markup.add(*buttons)
    return markup
