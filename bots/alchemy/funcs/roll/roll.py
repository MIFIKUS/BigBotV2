import time

from bots.alchemy.funcs.forecast.memory import get_forecast_addresses
from bots.alchemy.funcs.forecast.memory import get_item_id, get_item_sharp

from bots.alchemy.funcs.forecast.circle import get_forecast_color

from bots.alchemy.funcs.forecast.items import collect_items_info

from bots.alchemy.funcs.forecast.prices import get_prices_for_each_slot

from bots.alchemy.extensions.check_method import *
from bots.alchemy.extensions.forecast_color_chances import CHANCES

from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import repeat_forecast_instant, open_forecast, forecast_opened, close_forecast

var = {1: {'items': {'id': '123123', 'sharp': 2, 'item_name': 'sdfsdf'}, 'red': False, 'no_crystals': True, 'check_price': True, 'min_price': False}}


def get_data_from_memory(process_handle, item_id_addresses, sharp_addresses) -> dict:
    new_item_id_addresses = item_id_addresses
    new_sharp_addresses = sharp_addresses

    item_id_found_address = None

    for item_id_address in item_id_addresses:
        item_id = get_item_id(process_handle, item_id_address)
        if not item_id:
            new_item_id_addresses.remove(item_id_address)
            continue
        else:
            item_id_found_address = item_id_address
            break
    else:
        raise Exception('Адреса для ID предмета закончились. Среди них нет нужного')

    for sharp_address in sharp_addresses:
        sharp = get_item_sharp(process_handle, sharp_address)

        if sharp is False:
            new_sharp_addresses.remove(sharp_address)
            continue
        else:
            break
    else:
        raise Exception('Адреса для заточки предмета закончились. Среди них нет нужного')

    return {'id': item_id, 'sharp': sharp}, new_item_id_addresses, new_sharp_addresses, item_id_found_address


def make_roll(process_handle, server_id: str, colors: list, slots: list, items: list, method: str, check_price: bool, min_price: int):
    """Основная функция для ролла"""
    if method == MEMORY:
        addresses = get_forecast_addresses(process_handle, slots)

        item_id_addresses = addresses['item_id_addresses']
        sharp_addresses = addresses['item_sharp_addresses']

        found = False

        prev_found_item_id = None

        while not found:
            time.sleep(0.1)
            data, item_id_addresses, sharp_addresses, item_id_found_address = get_data_from_memory(process_handle, item_id_addresses, sharp_addresses)

            for item in items:
                if found:
                    break
                else:
                    if int(item['id']) == (data['id']):
                        if int(item['sharp']) == int(data['sharp']):
                            print(data['id'], data['sharp'])

                            time.sleep(1)
                            if forecast_opened():
                                close_forecast()
                            color = get_forecast_color()
                            if not forecast_opened():
                                open_forecast()
                            if color in colors:

                                items_info = collect_items_info()

                                print(f'items info {items_info}')
                                prices = get_prices_for_each_slot(server_id, items_info)
                                print(prices)
                                chances = CHANCES.get(color)

                                avg_roll_price = 0

                                for item_info in items_info.items():
                                    if not item_info[1]:
                                        continue

                                    price = prices.get(item_info[1])
                                for item_info in items_info.items():
                                    if not item_info[1]:
                                        continue
                                    if not price:
                                        continue
                                    chance_price = chances.get(item_info[0])

                                    avg_roll_price += price * chance_price

                                print(f'Авг цена ролла: {avg_roll_price}')
                                if check_price:
                                    if avg_roll_price >= min_price:
                                        found = True
                                        break
                                    else:
                                        close_forecast()
                                else:
                                    found = True
                                    break
                if found:
                    break
            else:
                repeat_forecast_instant()
                continue

            if forecast_opened():
                close_forecast()
