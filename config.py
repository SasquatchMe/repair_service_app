from dotenv import find_dotenv, load_dotenv
import os

if not find_dotenv():
    print('Не найден .env файл')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

DATABASE_PATH = os.path.abspath('/Users/Androidnek/PycharmProjects/CRM_tg_bot/CRM_SERVICE.db')

DATABASE_NAME = 'CRM_SERVICE.db'
ENTITY_TABLE_NAME = 'legal_entities'
COMPANY_TABLE_NAME = 'companies'
USERS_TABLE_NAME = 'users'
ORDERS_TABLE_NAME = 'orders'
SERVICES_TABLE_NAME = 'services'
MASTERS_TABLE_NAME = 'masters'
STATUSES_TABLE_NAME = 'statuses'
