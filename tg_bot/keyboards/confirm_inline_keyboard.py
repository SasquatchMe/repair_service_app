from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def cb_inline_keyboard(order_id):
    markup = InlineKeyboardMarkup(row_width=2)
    button_yes = InlineKeyboardButton(text='✅Принимаю', callback_data=f'cb_confirm_yes_{order_id}')
    button_no = InlineKeyboardButton(text='❌Отказываюсь', callback_data=f'cb_confirm_no_{order_id}')
    markup.add(button_yes, button_no)
    return markup
