from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import open_forecast, close_forecast, reset_forecast, repeat_forecast, click_on_item_in_forecast, exit_from_alchemy
from l2m_ui_funcs.main_screen import open_alchemy, open_menu

from bots.alchemy.funcs.forecast.items import get_item_info_by_text

from bots.alchemy.extensions.forecast_colors_names import FORECAST_COLORS_NAMES

from general.memory import search
from general.lists.all_items_ids import ALL_ITEMS

import time


def get_forecast_addresses(process_handle, slots: list) -> dict:
    """Получает адреса памяти круга"""
    found = False
    found_addresses = {}

    addresses = None
    counter = 0
    while not found:
        necessary_values = []

        open_forecast()

        for i in slots:
            while True:
                try:
                    click_on_item_in_forecast(i)
                    time.sleep(0.3)
                    item_id, item_sharp = get_item_info_by_text()
                    print(item_id, item_sharp)
                    if item_sharp > 1 or counter > 0:
                        break
                    raise
                except Exception:
                    reset_forecast()
                    open_forecast()

            necessary_values.append(int(item_id))
            necessary_values.append(item_sharp)

        item_id_found = False
        sharp_found = False

        if not addresses:
            addresses = search.find_addresses(process_handle, necessary_values)
            print("Список адресов получен")

            found_addresses['item_id_addresses'] = addresses.get(int(item_id))
            found_addresses['item_sharp_addresses'] = addresses.get(item_sharp)

        if counter != 0:
            print(f'{len(found_addresses['item_id_addresses'])} адресов ID предмета найдено')
            if len(found_addresses['item_id_addresses']) > 5:
                found_addresses['item_id_addresses'] = search.sort_addresses(process_handle, {int(item_id): found_addresses['item_id_addresses']})
            else:
                item_id_found = True

            print(f'{len(found_addresses['item_sharp_addresses'])} адресов заточки предмета найдено')
            if len(found_addresses['item_sharp_addresses']) > 4:
                found_addresses['item_sharp_addresses'] = search.sort_addresses(process_handle, {item_sharp: found_addresses['item_sharp_addresses']})
                #if len(found_addresses['item_sharp_addresses']) < 100:
                #    close_forecast()
                #    exit_from_alchemy()
                #    open_menu()
                #    open_alchemy()
                #    open_forecast()
            else:
                sharp_found = True

        counter += 1

        if item_id_found and sharp_found:
            return found_addresses

        reset_forecast()


def get_color(process_handle, address: int) -> str or bool:
    """Получает цвет по адресу памяти"""
    color_raw = search.get_value(process_handle, address, '')

    print(color_raw)

    for color_name, color in FORECAST_COLORS_NAMES.items():
        if color_name in color_raw:
            return color
    return False


def get_item_id(process_handle, address: int) -> int:
    """Получает ID предмета из адреса памяти"""
    item_id = search.get_value(process_handle, address, 0)
    if ALL_ITEMS.get(str(item_id)):
        return item_id
    elif len(str(item_id)) == 9:
        return item_id
    else:
        return False


def get_item_sharp(process_handle, address: int) -> int:
    """Получает заточку предмету из адреса памяти"""
    sharp = search.get_value(process_handle, address, 0, True)
    print(f'sharp {sharp}')
    if 0 <= sharp <= 11:
        return sharp
    else:
        return False
