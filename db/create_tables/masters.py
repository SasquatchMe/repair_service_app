import sqlite3

from config import (
    DATABASE_NAME,
    MASTERS_TABLE_NAME,
)


def create_table_master():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{MASTERS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                f"""
                CREATE TABLE `{MASTERS_TABLE_NAME}`(
                masters_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                phone INT NOT NULL);
                """
            )
