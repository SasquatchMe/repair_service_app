import sqlite3

from config import (
    DATABASE_NAME,
    SERVICES_TABLE_NAME,
)


def create_table_services():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{SERVICES_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                f"""
                CREATE TABLE `{SERVICES_TABLE_NAME}`(
                service_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(255) NOT NULL);
                """
            )
