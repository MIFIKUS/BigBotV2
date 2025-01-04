from general.packets.request_consts import HEADERS, GET_PRICE_URL
from general.database.remote.jwt import get_jwt_token

import requests


def get_minimal_price_for_item(server_id: str, item_id: str, sharp: int) -> int or bool:
    """Получает минимальную цену для предмета по пакетам"""

    HEADERS['Authorization'] = get_jwt_token()

    request_data = {"game_server_id": server_id,
               "game_items":
                   {'game_item_key': item_id,
                    'top': '1',
               "search": [
                   {"key": "Enchant",
                    "from": sharp,
                    "to": sharp}]
                    }
               }

    answer = requests.post(GET_PRICE_URL, json=request_data, headers=HEADERS).json()

    if not isinstance(answer, str):
        if answer.get('list') and len(answer.get('list')) > 0:
            return int(answer.get('list')[0].get('sale_price'))
    return False

