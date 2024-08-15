import os

from dotenv import find_dotenv, load_dotenv

if not find_dotenv():
    print('Не найден .env файл')
else:
    load_dotenv()


# BASE_PATH = os.path.abspath('/Users/Androidnek/PycharmProjects/CRM_tg_bot')
BOT_TOKEN = os.getenv('BOT_TOKEN')
SECRET_KEY = os.getenv('SECRET_KEY')
WEB_APP_PATH = os.path.abspath('web_app/')
# DATABASE_PATH = os.path.abspath(BASE_PATH + '/database.db')
DATABASE_PATH = os.path.abspath('/database.db')


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
    'Сантехника',
    'Холодильное оборудование',
    'Мебель',
    'Барное оборудование',
    'Другое',
]

DEFAULT_ENTITIES = [
    'ИП Горев Андраник Куркенович',
    'ИП Найденова Алина Вячеславовна',

]