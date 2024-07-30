import telebot.types

from tg_bot.bot_instance import bot
from telebot.types import Message
from tg_bot.states import CRMStates
from utils.authorization import check_user_exist
from tg_bot.keyboards.lookup_keyboard import lookup_keyboard
from pathlib import Path


@bot.message_handler(commands=['start'])
def send_welcome_message(message: Message):
    bot.set_state(message.from_user.id, CRMStates.login, message.chat.id)
    bot.send_message(message.chat.id, 'Привет!\nОтправьте логин, выданный Вашим менеджером')


@bot.message_handler(state="*", commands=['cancel'])
def cancel_state(message: Message):
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state=CRMStates.login)
def login_get(message: Message):
    login = message.text
    if check_user_exist(login):
        bot.set_state(message.from_user.id, CRMStates.lookup, message.chat.id)
        bot.send_message(message.chat.id, 'Вы успешно авторизовались!\nВыберите действие',
                         reply_markup=lookup_keyboard())
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['login'] = login
    else:
        bot.send_message(message.chat.id, 'Неверный логин. Проверьте корректность введенного логина!\n'
                                          'Если Вы не получили логин - обратитесь к нашему менеджеру')


@bot.message_handler(state=CRMStates.lookup)
def lookup(message: Message):
    if message.text == 'Создать заявку':
        bot.set_state(message.from_user.id, CRMStates.brand_name, message.chat.id)
        bot.send_message(message.chat.id, 'Пожалуйста, внимательно следуйте инструкциям для создания заявок!\n'
                                          '1. Напишите бренд устройства без модели, например: "Sony" или "Бирюса"',
                         reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(state=CRMStates.brand_name)
def get_brand_name(message: Message):
    bot.send_message(message.chat.id, '2.Напишите модель устройства (без названия), например: "wh-1000xm4"')
    bot.set_state(message.from_user.id, CRMStates.model_title, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['brand_name'] = message.text


@bot.message_handler(state=CRMStates.model_title)
def get_model(message: Message):
    bot.send_message(message.chat.id, '3.Подробно опишите поломку')
    bot.set_state(message.from_user.id, CRMStates.desc, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['model_title'] = message.text


@bot.message_handler(state=CRMStates.desc)
def get_desc(message: Message):
    bot.send_message(message.chat.id, '4.Отправьте фото заводской наклейки устройства')
    bot.set_state(message.from_user.id, CRMStates.model_image, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['desc'] = message.text


@bot.message_handler(state=CRMStates.model_image, content_types=['photo'])
def get_model_image(message: Message):
    Path(f'/Users/Androidnek/PycharmProjects/CRM_tg_bot/images/{message.chat.id}/photos').mkdir(parents=True,
                                                                                                exist_ok=True)

    image_info = bot.get_file(message.photo[-1].file_id)
    downloaded_image = bot.download_file(image_info.file_path)
    src = f'/Users/Androidnek/PycharmProjects/CRM_tg_bot/images/{message.chat.id}/' + image_info.file_path
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['model_image_path'] = src

    with open(src, 'wb') as new_image:
        new_image.write(downloaded_image)

    bot.send_message(message.chat.id, 'Данные приняты. Формируем Ваш заказ, еще мгновение...')

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        login = data['login']
        brand_name = data['brand_name']
        model_title = data['model_title']
        desc = data['desc']
        img_path = data['model_image_path']

    photo = open(img_path, 'rb')
    bot.send_photo(message.chat.id, photo, caption=f'1. Брэнд: {brand_name}\n'
                                                   f'2. Модель: {model_title}\n'
                                                   f'3. Описание: {desc}')

    bot.send_message(message.chat.id, 'Проверьте данные заявки! Нажмите "ОК", если все верно или '
                                      '"Отмена", если в заявке есть ошибка')
    bot.set_state(message.from_user.id, CRMStates.confirm_order, message.chat.id)


@bot.message_handler(state=CRMStates.confirm_order)
def confirm_order(message: Message):
    bot.send_message(message.chat.id, 'OK')


@bot.message_handler(state="*")
def undefined_message(message: Message):
    cur_state = bot.get_state(message.from_user.id, message.chat.id)
    print(cur_state)
