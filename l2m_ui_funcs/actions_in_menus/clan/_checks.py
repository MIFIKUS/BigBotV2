from general.funcs.checks import check
from general.funcs.string_work import delete_junk_symbols
from main_funcs import image

import time


def character_in_clan() -> bool:
    """Проверка на то, что персонаж состоит в клане"""
    template_name = 'bots\\sbor\\imgs\\templates\\character_in_clan.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_character_in_clan.png'
    area_of_screenshot = (840, 915, 1165, 985)

    return check(screenshot_name, template_name, area_of_screenshot)


def contribution_menu_opened() -> bool:
    """Проверка на то, что меню взноса открыто"""
    template_name = 'bots\\sbor\\imgs\\templates\\contribution_menu_opened.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_contribution_menu_opened.png'
    area_of_screenshot = (275, 165, 462, 190)

    return check(screenshot_name, template_name, area_of_screenshot)


def no_more_contributions() -> bool:
    """Проверка на то, что больше не осталось взносов в клан"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\amount_of_contributions.png'
    area_of_screenshot = (425, 898, 450, 927)
    color_min = [160, 160, 160]
    color_max = [255, 255, 255]

    custom_config = '--psm 10 -c tessedit_char_whitelist=0123456789'

    time.sleep(1)

    image.take_screenshot(screenshot_name, area_of_screenshot)
    image.delete_all_colors_except_one(screenshot_name, None, color_min, color_max)

    amount_of_contributions = image.image_to_string(screenshot_name, True, custom_config)
    amount_of_contributions = delete_junk_symbols(amount_of_contributions)

    print(amount_of_contributions)

    try:
        if int(amount_of_contributions) == 0:
            return True
        return False
    except ValueError:
        print('Не удалось получить количество доступных взносов')
        return True


def accept_contribute_opened() -> bool:
    """Проверка на то, что меню подтверждения взноса открыто"""
    template_name = 'bots\\sbor\\imgs\\templates\\accept_contribute_button.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_accept_contribute_button_available.png'
    area_of_screenshot = (930, 665, 1220, 750)

    return check(screenshot_name, template_name, area_of_screenshot)