# import sqlite3
# from config import (
#     DATABASE_NAME,
#     ENTITY_TABLE_NAME,
#     COMPANY_TABLE_NAME,
# )
#
#
# def create_table_company():
#     with sqlite3.connect(DATABASE_NAME) as conn:
#         cursor = conn.cursor()
#         cursor.execute(
#             f"""
#             SELECT name FROM sqlite_master
#             WHERE type='table' AND name='{COMPANY_TABLE_NAME}';
#             """
#         )
#         exists = cursor.fetchone()
#         if not exists:
#             cursor.executescript(
#                 f"""
#                 CREATE TABLE `{COMPANY_TABLE_NAME}`(
#                 company_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 address VARCHAR(255) NOT NULL,
#                 entity_id INTEGER NOT NULL REFERENCES {ENTITY_TABLE_NAME}(entity_id));
#                 """
#             )
