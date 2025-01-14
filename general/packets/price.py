from general.packets.request_consts import HEADERS, GET_PRICE_URL
from general.database.remote.jwt import get_jwt_token

from general.lists.blue_items import BLUE_ITEMS

import requests

import asyncio
import aiohttp


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
    print(answer)
    if answer.get('list') and len(answer.get('list')) > 0 and answer.get('list') != ['']:
        return int(answer.get('list')[0].get('sale_price'))
    return False


async def get_cheapest_blue_item(server_id: str) -> str:
    """Получает самую дешевую синюю шмотку на ауке"""
    def _prepare_request_data() -> list:
        """Подготавливает данные для запроса, чтобы получалось по 20 шмоток за 1 запрос"""
        items_list = []
        for item_id, item_name in BLUE_ITEMS.items():
            data = {"game_item_key": item_id, "top": "1", "search": [{"key": "Enchant", "from": 0, "to": 0}]}
            items_list.append(data)

        request = [items_list[i:i + 20] for i in range(0, len(items_list), 20)]
        return request

    async def _fetch(data: dict, session: aiohttp.ClientSession) -> dict:
        """Получает данные с сервера по шмоткам"""
        data_for_request = {"game_server_id": server_id, "game_items": data}

        async with session.post(GET_PRICE_URL, json=data_for_request, headers=HEADERS) as response:
            return await response.json()

    def _get_ids_and_prices(answer_data: list) -> dict:
        """Ответ сервера преобразует в словарь с ID предмета и его ценой"""
        ids_and_prices = {}
        for i in answer_data:
            info = i.get('list')
            for j in info:
                if j:
                    ids_and_prices[j['game_item_key']] = j['sale_price']
        return ids_and_prices

    HEADERS['Authorization'] = get_jwt_token()

    items_list = _prepare_request_data()
    tasks = []

    async with aiohttp.ClientSession() as session:
        for data in items_list:
            tasks.append(_fetch(data, session))

        result = await asyncio.gather(*tasks)

    ids_and_prices = _get_ids_and_prices(result)

    cheapest_item =  next(iter(sorted(ids_and_prices.items(), key=lambda item: item[1])))
    cheapest_item_id = cheapest_item[0]

    return cheapest_item_id
