from main_funcs import image

from general.funcs.string_work import delete_junk_symbols
from general.funcs.item_name_work import get_item_id, get_item_grade, get_item_sharp
from general.packets.price import get_minimal_price_for_item

from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import click_on_item

from bots.alchemy.extensions.items_colors import *
from bots.alchemy.config import MAX_PRICE_FOR_BLUE

import time


def get_item_info_from_inventory(row: int, server_id: str) -> tuple or bool:
    """Получает ID шмотки на которую нажал"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\item_name.png'
    new_screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\item_name_fixed_colors.png'
    area_of_screenshot = (1400, 190 + (100 * row), 1800, 255 + (100 * row))
    image.take_screenshot(screenshot_name, area_of_screenshot)

    colors = (GREEN, BLUE, RED)
    colors_str = ('green', 'blue', 'red')

    for color, color_str in zip(colors, colors_str):
        image.delete_all_colors_except_one(screenshot_name, color, new_image_name=new_screenshot_name)

        item_name = image.image_to_string(new_screenshot_name, False)
        item_name = delete_junk_symbols(item_name)
        item_name = item_name.replace('(привяз.)', '')

        item_id = get_item_id(item_name)
        item_grade = get_item_grade(item_name, color_str)
        item_sharp = get_item_sharp(item_name)

        if item_id:
            price = get_minimal_price_for_item(server_id, item_id, item_sharp)
            return item_id, item_grade, price

    return False


def set_rolls_items(items: dict, server_id):
    """Выбирает из инвентаря шмотки нужные для ролла"""
    for _ in range(2): #1 прокрутка вниз инвентаря при необходимости
        for table in range(6):
            for row in range(4):
                all_amount = 0
                for _, amount in items.items():
                    all_amount += amount

                if all_amount == 0:
                    return

                click_on_item(table, row)
                time.sleep(0.3)
                item_info = get_item_info_from_inventory(table, server_id)

                print(item_info)

                if not item_info:
                    continue

                item_id, item_grade, price = item_info

                if item_grade in items.keys() and items.get(item_grade) and price <= MAX_PRICE_FOR_BLUE:
                    click_on_item(table, row)
                    items[item_grade] -= 1






