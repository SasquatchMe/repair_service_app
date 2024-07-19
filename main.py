from db.init_db import init_db
from tg_bot.message_handlers import *
from telebot import custom_filters

if __name__ == '__main__':
    init_db()
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()

