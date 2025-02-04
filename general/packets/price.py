from general.packets.request_consts import HEADERS, GET_PRICE_URL
from general.database.remote.jwt import get_jwt_token

from general.lists.blue_items import BLUE_ITEMS
from general.lists.servers import ALL_SERVERS_IDS

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


async def async_get_minimal_price_for_item(server_id: str, item_id: str, sharp: int) -> int or bool:
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


async def get_avg_price(item_id: str, item_sharp: int) -> float or int:
    """Получает среднюю цену среди всех серверов для шмотки"""
    tasks = []
    for server_id in ALL_SERVERS_IDS.values():
        tasks.append(async_get_minimal_price_for_item(server_id, item_id, item_sharp))

    all_prices = await asyncio.gather(*tasks)

    return sum(all_prices) / len(all_prices)


def get_prices_for_list_of_items(server_id: str, items_list: list[tuple], need_to_search_avg: bool) -> dict:
    """Получает цены для указанного списка шмоток\need_to_search_avg значит, что нужно ли искать avg цену если шмотки нет на ауке"""
    if len(items_list) > 20:
        raise Exception("Длина списка шмоток не должна превышать 20")

    HEADERS['Authorization'] = get_jwt_token()
    request_data = []
    for item in items_list:
        if not item:
            continue
        item_id = item[0]
        item_sharp = item[1]

        data = {"game_item_key": item_id, "top": "1", "search": [{"key": "Enchant", "from": item_sharp, "to": item_sharp}]}
        request_data.append(data)

    full_request_data = {"game_server_id": server_id, "game_items": request_data}
    result = requests.post(GET_PRICE_URL, json=full_request_data, headers=HEADERS).json()

    prices = {}

    for item_market_info, item_info in zip(result['list'], items_list):
        if not item_info:
            continue

        item_id = item_info[0]
        item_sharp = item_info[1]

        if not item_market_info:
            if need_to_search_avg:
                loop = asyncio.get_event_loop()
                price = loop.run_until_complete(get_avg_price(item_id, item_sharp))
                print(f'avg price {price}')

            else:
                price = 0

        else:
            price = int(item_market_info['sale_price'])

        prices[(item_id, item_sharp)] = price

    return prices


