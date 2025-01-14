from main_funcs import image

from general.funcs.string_work import delete_junk_symbols
from general.funcs.item_name_work import get_item_id, get_item_grade
from general.packets.price import get_minimal_price_for_item

from bots.alchemy.extensions.items_colors import *


def get_item_info_from_inventory(row: int) -> tuple or bool:
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

        if item_id:
            return item_id, item_grade

    return False



