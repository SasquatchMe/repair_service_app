import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    print('Не найден .env файл')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEB_APP_PATH = os.path.abspath('web_app/')
DATABASE_PATH = os.path.abspath('/Users/Androidnek/PycharmProjects/CRM_tg_bot/CRM_SERVICE.db')

DEAFAULT_COMMANDS = (
    ['neworder', 'Создать новую заявку'],
    ['info', 'Справка о работе бота'],
    ['contacts', 'Связаться с нами'],
    ['cancel', 'Выйти в главное меню'],
)

DEFAULT_STATUSES = [
    'Заявка сформирована',
    'Заявка принята',
    'Назначен исполнитель',
    'Заявка исполнена',
    'Отказано',
]

DEFAULT_ORDER_TYPES = [
    'Авария',
    'Поломка',
    'Плановое обслуживание',
]

DEFAULT_BREAKING_TYPES = [
    'Электрика',
    'Сантенхника',
    'Холодильное оборудование',
    'Мебель',
    'Барное оборудование',
    'Другое',
]

DEFAULT_ENTITIES = [
    'ИП Горев Андраник Куркенович',
    'ИП Найденова Алина Вячеславовна'
]
