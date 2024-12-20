import mysql.connector

connection = None


def get_cursor(ip: str, user: str, password: str) -> mysql.connector.connect().cursor:
    """Возвращает курсор для работы с MySQL"""
    global connection
    if connection is None or not connection.is_connected():
        connection = mysql.connector.connect(
            host=ip,
            user=user,
            password=password)

    return connection.cursor()
