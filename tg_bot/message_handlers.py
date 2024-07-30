import datetime

from loguru import logger

from db.query_to_db.query_to_db import get_order_type_id, get_breaking_type_id
from tg_bot.bot_instance import bot
from telebot.types import Message

from tg_bot.keyboards.continue_keyboard import continue_keyboard
from tg_bot.states import CRMStates
from utils.authorization import check_object_exist, register_user_exist, tg_user_exist
from tg_bot.keyboards.lookup_keyboard import lookup_keyboard
from tg_bot.keyboards.order_type_keyboard import order_type_keyboard
from tg_bot.keyboards.breaking_type_keyboard import breaking_type_keyboard
from pathlib import Path
from tg_bot.messages_text.messages import *


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
    tg_id = message.from_user.id
    if check_object_exist(login):
        user_exist = register_user_exist(tg_id, login)
        logger.debug(user_exist)

        bot.set_state(message.from_user.id, CRMStates.lookup, message.chat.id)
        bot.send_message(message.chat.id, 'Вы успешно авторизовались!\nВыберите действие',
                         reply_markup=lookup_keyboard())

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['login'] = login

    else:
        bot.send_message(message.chat.id, 'Неверный логин. Проверьте корректность введенного логина!\n'
                                          'Если Вы не получили логин - обратитесь к Вашему менеджеру')


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
    bot.send_message(message.chat.id, text=description_of_breaking)
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
        path = f'../CRM_tg_bot/images/{message.chat.id}/{datetime.datetime.now().strftime("%Y%m%d")}/photo_of_breaking'
        Path(path).mkdir(parents=True, exist_ok=True)
        image_info = bot.get_file(message.photo[-1].file_id)
        downloaded_image = bot.download_file(image_info.file_path)
        src = path + image_info.file_path
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['breaking_image_path'] = src

        with open(src, 'wb') as new_image:
            new_image.write(downloaded_image)

        bot.set_state(message.from_user.id, CRMStates.model_name, message.chat.id)
        bot.send_message(message.chat.id, text=model_name)

    if message.content_type == 'text':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['breaking_image_path'] = None

        bot.set_state(message.from_user.id, CRMStates.model_name, message.chat.id)
        bot.send_message(message.chat.id, text=model_name)


        # bot.send_message(message.chat.id, 'Данные приняты. Формируем Ваш заказ, еще мгновение...')

        # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        #     login = data['login']
        #     brand_name = data['brand_name']
        #     model_title = data['model_title']
        #     desc = data['desc']
        #     img_path = data['model_image_path']
        #
        # photo = open(img_path, 'rb')
        # bot.send_photo(message.chat.id, photo, caption=f'1. Брэнд: {brand_name}\n'
        #                                                f'2. Модель: {model_title}\n'
        #                                                f'3. Описание: {desc}')
        #
        # bot.send_message(message.chat.id, 'Проверьте данные заявки! Нажмите "ОК", если все верно или '
        #                                   '"Отмена", если в заявке есть ошибка')
        # bot.set_state(message.from_user.id, CRMStates.confirm_order, message.chat.id)


@bot.message_handler(state=CRMStates.model_name)
def get_model_name(message: Message):
    bot.set_state(message.from_user.id, CRMStates.service_sticker_photo, message.chat.id)
    bot.send_message(message.chat.id, text=service_sticker_photo)



@bot.message_handler(state=CRMStates.confirm_order)
def confirm_order(message: Message):
    bot.send_message(message.chat.id, 'OK')


@bot.message_handler(state="*")
def undefined_message(message: Message):
    cur_state = bot.get_state(message.from_user.id, message.chat.id)
    print(cur_state)
