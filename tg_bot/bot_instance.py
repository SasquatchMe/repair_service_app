import telebot
from telebot.storage import StateMemoryStorage

from config import BOT_TOKEN

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)
