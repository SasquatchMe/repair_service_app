from telebot import custom_filters

from db.models.tables import create_models
from tg_bot.message_handlers import *

if __name__ == '__main__':
    create_models()
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()
