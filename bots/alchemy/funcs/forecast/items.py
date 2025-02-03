from general.funcs.string_work import delete_junk_symbols
from general.funcs.item_name_work import get_item_id, get_item_sharp

from bots.alchemy.extensions.items_colors import *

from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import click_on_item_in_forecast

from main_funcs import image

import time


def get_item_info_by_text() -> tuple:
    """Получает информацию о предмете в меню прогноза, путем просмотра текста"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\item_name_in_forecast.png'
    new_screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\item_name_in_forecast_fixed_colors.png'
    area_of_screenshot = (735, 375, 1130, 450)

    image.take_screenshot(screenshot_name, area_of_screenshot)

    for color in (WHITE, BLUE, GREEN, RED):
        image.delete_all_colors_except_one(screenshot_name, color, new_image_name=new_screenshot_name)

        item_name = image.image_to_string(new_screenshot_name, False)
        item_name = delete_junk_symbols(item_name)

        item_id = get_item_id(item_name)
        item_sharp = get_item_sharp(item_name)

        if item_id:
            return item_id, item_sharp


def collect_items_info() -> dict:
    """Прокликивает все слоты в меню предсказания чтобы получить ID и заточки предметов"""
    items_info = {}
    for i in range(5):
        click_on_item_in_forecast(i)
        time.sleep(0.3)
        items_info[i] = get_item_info_by_text()

    return items_info
