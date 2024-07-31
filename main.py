from telebot import custom_filters
from loguru import logger
from telebot.types import BotCommand

from db.models.tables import create_models
from tg_bot.message_handlers import *
from config import DEAFAULT_COMMANDS

if __name__ == '__main__':
    create_models()
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands([BotCommand(command, desc) for command, desc in DEAFAULT_COMMANDS])
    logger.debug('Start polling')
    bot.infinity_polling()
