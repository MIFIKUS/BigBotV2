from general.database.remote.config import *
from general.database.general.connection import get_cursor


def get_jwt_token() -> str:
    """Получает JWT токен из бд, для работы с пакетами"""
    cursor = get_cursor(IP, USER, PASSWORD)

    query = "SELECT * FROM l2m.bot_data;"
    cursor.execute(query)
    return cursor.fetchall()[0][0]

