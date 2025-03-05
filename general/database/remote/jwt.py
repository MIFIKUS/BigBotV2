from general.database.remote.config import *
from general.database.general.connection import get_cursor

from general.logs.logger import logger


def get_jwt_token() -> str:
    """Получает JWT токен из бд, для работы с пакетами"""
    cursor = get_cursor(IP, USER, PASSWORD)

    query = "SELECT * FROM l2m.bot_data;"

    logger.debug(f'query: {query}')

    cursor.execute(query)
    result = cursor.fetchall()[0][0]

    logger.debug(f'Запрос jwt токена вернул: {result}')
    return result
