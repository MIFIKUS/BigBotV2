from main_funcs import image

from general.funcs.string_work import delete_junk_symbols
from general.funcs.item_name_work import get_item_id, get_item_grade, get_item_sharp
from general.packets.price import get_minimal_price_for_item, get_cheapest_blue_item

from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import click_on_item, exit_from_alchemy, scroll_inventory, item_equiped
from l2m_ui_funcs.actions_in_menus.market.market import buy_item_by_id, exit_from_market
from l2m_ui_funcs.actions_in_menus.craft_menu.craft_menu import craft_green_item, exit_craft_menu


from l2m_ui_funcs.main_screen import open_menu, open_alchemy, open_market, open_craft_menu

from bots.alchemy.extensions.items_colors import *
from bots.alchemy.extensions import items_grade

from bots.alchemy.config import MAX_PRICE_FOR_BLUE

import time
import asyncio


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

        item_name = item_name.split('(')[0]

        item_id = get_item_id(item_name)
        item_grade = get_item_grade(item_name, color_str)
        item_sharp = get_item_sharp(item_name)

        if item_id:
            price = get_minimal_price_for_item(server_id, item_id, item_sharp)
            return item_id, item_grade, price

    return False


def set_rolls_items(items: dict, server_id):
    """Выбирает из инвентаря шмотки нужные для ролла"""
    roll_set = False
    items_copy = items
    while not roll_set:
        scrolls = 0
        items = items_copy.copy()
        inventory_end = False
        while not inventory_end and not roll_set:
            for table in range(scrolls, 6):
                if inventory_end:
                    break
                for row in range(4):
                    print(f'items: {items}')
                    all_amount = 0
                    for _, amount in items.items():
                        all_amount += amount

                    if all_amount == 0:
                        return

                    if item_equiped(row, table):
                        inventory_end = True
                        break

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

            if not inventory_end:
                scroll_inventory()
                scrolls += 1

        if sum(items.values()):
            exit_from_alchemy()

            if items.get(items_grade.BLUE):
                if items[items_grade.BLUE]:
                    open_menu()
                    open_market()

                    loop = asyncio.get_event_loop()

                    for _ in range(items[items_grade.BLUE]):
                        buy_item_id, buy_item_price = loop.run_until_complete(get_cheapest_blue_item(server_id))
                        buy_item_by_id(buy_item_id, 0, buy_item_price)

                    exit_from_market()

            if items.get(items_grade.GREEN):
                open_menu()
                open_craft_menu()
                craft_green_item()
                exit_craft_menu()

            open_menu()
            open_alchemy()



