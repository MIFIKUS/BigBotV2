from general.funcs.checks import check, check_color


def attack_menu_opened() -> bool:
    """Проверяет открыта ли вкладка боя"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\attack_menu_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_attack_menu_opened.png'
    area_of_screenshot = (80, 265, 290, 525)

    return check(screenshot_name, template_name, area_of_screenshot)


def collect_menu_opened() -> bool:
    """Проверяет открыта ли вкладка подбор"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_collect_opened.png'
    color = [255, 255, 255]
    area_of_screenshot = (134, 385, 135, 386)

    return check_color(color, screenshot_name, area_of_screenshot)


def equipment_auto_collect_off() -> bool:
    """Проверка на то, что автоподбор снаряжения выключен"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_equipment_auto_collect_off.png'
    color = [60, 70, 85]
    area_of_screenshot = (1750, 349, 1751, 350)

    return check_color(color, screenshot_name, area_of_screenshot)


def items_auto_collect_off() -> bool:
    """Проверка на то, что автоподбор предметов выключен"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_items_auto_collect_off.png'
    color = [60, 70, 85]
    area_of_screenshot = (1775, 505, 1776, 506)

    return check_color(color, screenshot_name, area_of_screenshot)


def information_menu_opened() -> bool:
    """Проверка на то, что вкладка информация открыта"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_information_menu_opened.png'
    color = [215, 105, 10]
    area_of_screenshot = (980, 873, 981, 874)

    return check_color(color, screenshot_name, area_of_screenshot)
