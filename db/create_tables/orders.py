import sqlite3
from config import (
    DATABASE_NAME,
    ENTITY_TABLE_NAME,
    COMPANY_TABLE_NAME,
    ORDERS_TABLE_NAME, SERVICES_TABLE_NAME, MASTERS_TABLE_NAME, STATUSES_TABLE_NAME, USERS_TABLE_NAME,
)


def create_table_order():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{ORDERS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                f"""
                CREATE TABLE `{ORDERS_TABLE_NAME}`(
                order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                date_create DATETIME,
                user_login VARCHAR(50) NOT NULL REFERENCES {USERS_TABLE_NAME}(login),
                company_id INTEGER NOT NULL REFERENCES {COMPANY_TABLE_NAME}(company_id),
                description VARCHAR(255),
                service_id INTEGER NOT NULL REFERENCES {SERVICES_TABLE_NAME}(service_id),
                master_id INTEGER NOT NULL REFERENCES {MASTERS_TABLE_NAME}(masters_id),
                status_id TEXT NOT NULL REFERENCES {STATUSES_TABLE_NAME}(status_id));
                
                """
            )
