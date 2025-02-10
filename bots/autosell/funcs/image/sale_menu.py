from general.funcs import string_work
from general.funcs.checks import check
from general.funcs.string_work import delete_junk_symbols

from main_funcs import image, mouse

import time


def get_old_price() -> int or bool:
    """Получает предыдущую цену шмотки, при неудаче возвращает False"""
    image_name = 'bots\\autosell\\imgs\\screenshots\\previous_price.png'
    area_of_screenshot = (1011, 325, 1150, 365)
    color_min = [70, 80, 80]
    color_max = [255, 255, 255]

    image.take_screenshot(image_name, area_of_screenshot)
    image.delete_all_colors_except_one(image_name, None, color_min, color_max)

    price = image.image_to_string(image_name, True)
    price = string_work.delete_junk_symbols(price)

    try:
        return int(price)
    except ValueError:
        return False


def get_item_name() -> str:
    """Возвращает название предмета из меню продажи"""
    image_name = 'bots\\autosell\\imgs\\screenshots\\item_name.png'
    area_of_screenshot = (605, 170, 1375, 200)

    image.take_screenshot(image_name, area_of_screenshot)

    item_name = image.image_to_string(image_name, False)
    item_name = string_work.delete_junk_symbols(item_name)

    return item_name


def no_items_to_replace(is_global: bool) -> bool:
    """Проверяет есть ли шмотки чтобы их переставить"""
    if not is_global:
        template_name = 'bots\\autosell\\imgs\\templates\\no_items_to_autosell.png'
    else:
        template_name = 'bots\\autosell\\imgs\\templates\\no_items_to_autosell_in_global_market.png'

    screenshot_name = 'bots\\autosell\\imgs\\screenshots\\are_there_items_to_autosell.png'
    area_of_screenshot = (235, 615, 1135, 655)

    return check(screenshot_name, template_name, area_of_screenshot)


def check_if_all_items_are_replaced() -> bool:
    """Проверяет что все предметы переставлены, путем проверки на слово Продается"""
    template_name = 'bots\\autosell\\imgs\\templates\\item_is_replaced.png'
    screenshot_name = 'bots\\autosell\\imgs\\screenshots\\is_item_replaced.png'
    area_of_screenshot = (1200, 305, 1330, 340)

    return check(screenshot_name, template_name, area_of_screenshot)


def get_equiped_item_cords() -> tuple or bool:
    """Получает координаты экипированной шмотки, если не находит, возвращает False"""
    template_name = 'general\\imgs\\templates\\item_is_equiped.png'
    screenshot_name = 'bots\\autosell\\imgs\\screenshots\\inventory.png'
    area_of_screenshot = (1400, 325, 1805, 890)

    image.take_screenshot(screenshot_name, area_of_screenshot)

    cords = None
    while not cords:
        mouse.move(1600, 520)
        mouse.wheel_down(17)
        time.sleep(2)

        image.take_screenshot(screenshot_name, area_of_screenshot)
        cords = image.get_matching_image_cords(screenshot_name, template_name)


    if not cords:
        return False

    x = cords[0] + 1450
    y = cords[1] + 355

    return x, y


def get_set_price() -> int or bool:
    """Получает введенную цену, если не удалось, возвращает False"""
    screenshot_name = 'bots\\autosell\\imgs\\screenshots\\set_price.png'
    area_of_screenshot = (1085, 630, 1270, 680)

    color_min = [180, 70, 0]
    color_max = [255, 110, 10]

    image.take_screenshot(screenshot_name, area_of_screenshot)
    image.delete_all_colors_except_one(screenshot_name, None, color_min, color_max)

    price = image.image_to_string(screenshot_name, True)

    price = delete_junk_symbols(price)

    try:
        return int(price)
    except ValueError:
        return False
