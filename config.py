from dotenv import find_dotenv, load_dotenv
import os

if not find_dotenv():
    print('Не найден .env файл')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_PATH = os.path.abspath('/Users/Androidnek/PycharmProjects')
DATABASE_PATH = os.path.abspath('/Users/Androidnek/PycharmProjects/CRM_tg_bot/CRM_SERVICE.db')


DEFAULT_STATUSES = [
    'Заявка сформирована',
    'Заявка принята',
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
]