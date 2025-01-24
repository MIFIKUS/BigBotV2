from bots.alchemy.funcs.forecast.memory import get_forecast_addresses
from bots.alchemy.funcs.forecast.memory import get_color, get_item_id, get_item_sharp

from bots.alchemy.extensions.check_method import *

from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import repeat_forecast_instant

var = {1: {'items': {'id': '123123', 'sharp': 2, 'item_name': 'sdfsdf'}, 'red': False, 'no_crystals': True, 'check_price': True}}


def get_data_from_memory(process_handle, item_id_addresses, sharp_addresses) -> dict:
    new_item_id_addresses = item_id_addresses
    new_sharp_addresses = sharp_addresses

    for item_id_address in item_id_addresses:
        item_id = get_item_id(process_handle, item_id_address)
        if not item_id:
            new_item_id_addresses.remove(item_id_address)
            continue
        else:
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

    return {'id': item_id, 'sharp': sharp}, new_item_id_addresses, new_sharp_addresses


def make_roll(process_handle, colors: list, slots: list, items_and_slots: dict, method: str, check_price: bool):
    """Основная функция для ролла"""
    if method == MEMORY:
        addresses = get_forecast_addresses(process_handle, slots)

        item_id_addresses = addresses['item_id_addresses']
        sharp_addresses = addresses['item_sharp_addresses']

        found = False

        while not found:
            data, item_id_addresses, sharp_addresses = get_data_from_memory(process_handle, item_id_addresses, sharp_addresses)

            print(data)
            for slot, slot_data in items_and_slots.items():
                if found:
                    break
                for item in slot_data['items']:
                    if item['id'] == data['id']:
                        if item['sharp'] == data['sharp']:
                            print('foundy')
                            found = True
                            break
            else:
                repeat_forecast_instant()
                continue
