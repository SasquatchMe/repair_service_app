import sqlite3

from config import (
    DATABASE_NAME,
    COMPANY_TABLE_NAME,
    USERS_TABLE_NAME, ENTITY_TABLE_NAME,
)


def create_table_user():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{USERS_TABLE_NAME}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.executescript(
                f"""
                CREATE TABLE `{USERS_TABLE_NAME}`( 
                login VARCHAR(255) PRIMARY KEY,
                entity_id INTEGER NOT NULL REFERENCES {ENTITY_TABLE_NAME}(entity_id));
                """
            )
