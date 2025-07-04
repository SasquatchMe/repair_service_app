from tg_bot.bot_instance import bot
from utils.convert_to_msg import *


def send_message_about_update_status(tg_id, order_id):
    msg = get_update_message_from_order_db(order_id)
    bot.send_message(tg_id, text=msg, parse_mode='Markdown')


def send_message_about_est_time(tg_id, order_id):
    msg = get_update_message_from_order_db_with_est_time(order_id)
    bot.send_message(tg_id, text=msg, parse_mode='Markdown')


def send_message_about_decline(tg_id, order_id):
    msg = get_decline_message(order_id)
    bot.send_message(tg_id, text=msg, parse_mode='Markdown')
