import sqlite3
from config import (
    DATABASE_NAME,
    ENTITY_TABLE_NAME,
)


def create_table_entity():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{ENTITY_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                f"""
                CREATE TABLE `{ENTITY_TABLE_NAME}`(
                entity_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(50) NOT NULL);
                """
            )
