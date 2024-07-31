import datetime

import telebot.types
from loguru import logger

from db.query_to_db.create_order_in_db import create_order
from db.query_to_db.query_to_db import get_order_type_id, get_breaking_type_id, get_order_by_order_id
from tg_bot.bot_instance import bot
from telebot.types import Message

from tg_bot.keyboards.continue_keyboard import continue_keyboard
from tg_bot.states import CRMStates
from utils.authorization import check_object_exist, register_user_exist, tg_user_exist
from tg_bot.keyboards.lookup_keyboard import lookup_keyboard
from tg_bot.keyboards.order_type_keyboard import order_type_keyboard
from tg_bot.keyboards.breaking_type_keyboard import breaking_type_keyboard
from tg_bot.keyboards.phone_num_keyboard import phone_num_keyboard
from pathlib import Path
from tg_bot.messages_text.messages import *
from utils.convert_to_msg import get_message_from_order_db
from telebot.types import InputMediaPhoto
from config import WORKDIR, WEB_APP_PATH


@bot.message_handler(commands=['start'])
def send_welcome_message(message: Message):
    tg_id = message.from_user.id
    if not tg_user_exist(tg_id):
        bot.set_state(message.from_user.id, CRMStates.login, message.chat.id)
        bot.send_message(message.chat.id, 'Привет!\nОтправьте логин Вашего предприятия, выданный менеджером')
    else:
        bot.set_state(message.from_user.id, CRMStates.lookup, message.chat.id)
        bot.send_message(message.chat.id, 'Добрый день! Рады снова видеть Вас!\nВыберите действие',
                         reply_markup=lookup_keyboard())


@bot.message_handler(state="*", commands=['cancel'])
def cancel_state(message: Message):
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=CRMStates.login)
def login_get(message: Message):
    login = message.text
    if check_object_exist(login):
        bot.set_state(message.from_user.id, CRMStates.get_phone, message.chat.id)
        bot.send_message(message.chat.id, 'Введите Ваш контактный номер телефона:')

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['login'] = login

    else:
        bot.send_message(message.chat.id, 'Неверный логин. Проверьте корректность введенного логина!\n'
                                          'Если Вы не получили логин - обратитесь к Вашему менеджеру')


@bot.message_handler(state=CRMStates.get_phone)
def get_phone(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        login = data['login']
    phone = message.text
    tg_id = message.from_user.id
    reg_user = register_user_exist(tg_id, login, phone)
    logger.debug(reg_user)
    bot.set_state(message.from_user.id, CRMStates.lookup, message.chat.id)
    bot.send_message(message.chat.id, text='Вы зарегистрированы!\nВыберите действие',
                     reply_markup=lookup_keyboard())


@bot.message_handler(state=CRMStates.lookup)
def lookup(message: Message):
    if message.text == 'Создать заявку':
        bot.set_state(message.from_user.id, CRMStates.order_type, message.chat.id)
        bot.send_message(message.chat.id, text=type_order, reply_markup=order_type_keyboard())


@bot.message_handler(state=CRMStates.order_type)
def get_brand_name(message: Message):
    bot.send_message(message.chat.id, text=type_breaking, reply_markup=breaking_type_keyboard())
    bot.set_state(message.from_user.id, CRMStates.breaking_type, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['order_type_id'] = get_order_type_id(message.text)


@bot.message_handler(state=CRMStates.breaking_type)
def get_model(message: Message):
    bot.send_message(message.chat.id, text=description_of_breaking, reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, CRMStates.desc, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['breaking_type_id'] = get_breaking_type_id(message.text)


@bot.message_handler(state=CRMStates.desc)
def get_desc(message: Message):
    bot.send_message(message.chat.id, text=photo_of_breaking, reply_markup=continue_keyboard())
    bot.set_state(message.from_user.id, CRMStates.breaking_image, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['desc'] = message.text


@bot.message_handler(state=CRMStates.breaking_image, content_types=['photo', 'text'])
def get_model_image(message: Message):
    if message.content_type == 'photo':
        path = f'{WORKDIR}/web_app/static/images/{message.chat.id}/{datetime.datetime.now().strftime("%Y%m%d")}/breaking_photo/'
        Path(path).mkdir(parents=True, exist_ok=True)
        image_info = bot.get_file(message.photo[-1].file_id)
        downloaded_image = bot.download_file(image_info.file_path)
        src = path + image_info.file_path.split('/')[1]
        logger.debug(src)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['breaking_image_path'] = src.split('web_app')[1]

        with open(src, 'wb') as new_image:
            new_image.write(downloaded_image)

        bot.set_state(message.from_user.id, CRMStates.model_name, message.chat.id)
        bot.send_message(message.chat.id, text=model_name, reply_markup=telebot.types.ReplyKeyboardRemove())

    if message.content_type == 'text':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['breaking_image_path'] = None

        bot.set_state(message.from_user.id, CRMStates.model_name, message.chat.id)
        bot.send_message(message.chat.id, text=model_name)


@bot.message_handler(state=CRMStates.model_name)
def get_model_name(message: Message):
    bot.set_state(message.from_user.id, CRMStates.service_sticker_photo, message.chat.id)
    bot.send_message(message.chat.id, text=service_sticker_photo, reply_markup=continue_keyboard())

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['model_name'] = message.text


@bot.message_handler(state=CRMStates.service_sticker_photo, content_types=['photo', 'text'])
def get_service_sticker_photo(message: Message):
    if message.content_type == 'photo':
        path = f'{WORKDIR}/web_app/static/images/{message.chat.id}/{datetime.datetime.now().strftime("%Y%m%d")}/service_sticker_photo/'
        Path(path).mkdir(parents=True, exist_ok=True)
        image_info = bot.get_file(message.photo[-1].file_id)
        downloaded_image = bot.download_file(image_info.file_path)
        src = path + image_info.file_path.split('/')[1]
        logger.debug(src)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['service_sticker_image_path'] = src.split('web_app')[1]

        with open(src, 'wb') as new_image:
            new_image.write(downloaded_image)

        bot.set_state(message.from_user.id, CRMStates.contact, message.chat.id)
        bot.send_message(message.chat.id, text=contact, reply_markup=phone_num_keyboard(message.from_user.id))

    if message.content_type == 'text':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['service_sticker_image_path'] = None

        bot.set_state(message.from_user.id, CRMStates.contact, message.chat.id)
        bot.send_message(message.chat.id, text=contact, reply_markup=phone_num_keyboard(message.from_user.id))


@bot.message_handler(state=CRMStates.contact)
def choice_contact_num(message: Message):
    bot.set_state(message.from_user.id, CRMStates.comment, message.chat.id)
    bot.send_message(message.chat.id, text=comment, reply_markup=continue_keyboard())
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.text


@bot.message_handler(state=CRMStates.comment)
def get_a_comment(message: Message):
    bot.send_message(message.chat.id, text=confirm_text, reply_markup=telebot.types.ReplyKeyboardRemove())
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['comment'] = message.text if message.text.lower() != 'пропустить' else None

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        order_id = create_order(data, message.from_user.id)

    sub_res = get_message_from_order_db(order_id)
    breaking_image_path, service_image_path, msg = sub_res[0], sub_res[1], sub_res[2]
    logger.debug(breaking_image_path)
    logger.debug(service_image_path)
    if breaking_image_path is not None and service_image_path is not None:
        breaking_photo = open(WEB_APP_PATH + breaking_image_path, 'rb')
        service_sticker_photo = open(WEB_APP_PATH + service_image_path, 'rb')

        media = [InputMediaPhoto(breaking_photo, caption=msg), InputMediaPhoto(service_sticker_photo)]
        bot.send_media_group(message.chat.id, media)

    elif breaking_image_path is None and service_image_path is not None:
        service_sticker_photo = open(WEB_APP_PATH + service_image_path, 'rb')
        bot.send_photo(message.chat.id, photo=service_sticker_photo, caption=msg)

    elif breaking_image_path is not None and service_image_path is None:
        breaking_image_photo = open(WEB_APP_PATH + breaking_image_path, 'rb')
        bot.send_photo(message.chat.id, photo=breaking_image_photo, caption=msg)
    else:
        bot.send_message(message.chat.id, text=msg)

    bot.set_state(message.from_user.id, CRMStates.lookup, message.chat.id)
    bot.send_message(message.chat.id, text=return_to_menu, reply_markup=lookup_keyboard())


@bot.message_handler(state="*")
def undefined_message(message: Message):
    bot.send_message(message.chat.id, 'Мне не удается понять, что ты отправил.'
                                      ' Пожалуйста, отправь то, что просят в инстуркции')
