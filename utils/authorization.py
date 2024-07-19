import sqlite3
from config import DATABASE_PATH


def check_user_exist(login: str):
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * 
            FROM users
            WHERE login = ?
            """, [login]
        )
        check = cursor.fetchone()
        return True if check else False


