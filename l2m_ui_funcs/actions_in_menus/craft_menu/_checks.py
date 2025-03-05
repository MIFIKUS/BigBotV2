from general.funcs.checks import check, check_color


def search_area_opened() -> bool:
    """Проверка на то, что меню аксессуаров открыто"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_craft_search_area_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\craft_search_area_opened.png'
    area_of_screenshot = (1350, 155, 1600, 240)

    return check(screenshot_name, template_name, area_of_screenshot)


def necklace_opened() -> bool:
    """Проверка на то, что меню крафта шмотки открыто"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_necklace_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\necklace_opened.png'
    area_of_screenshot = (955, 440, 1165, 665)

    return check(screenshot_name, template_name, area_of_screenshot)


def craft_available() -> bool:
    """Проверка на то, что крафт доступен"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_craft_available.png'
    color = [105, 50, 10]
    area_of_screenshot = (1580, 925, 1581, 926)

    return not check_color(color, screenshot_name, area_of_screenshot)


def cristal_craft_button_available() -> bool:
    """Проверка на то, что есть кнопка создать улучшенного драгоценного камня"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_cristal_craft_button.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\cristal_craft_button.png'
    area_of_screenshot = (1730, 365, 1820, 440)

    return check(screenshot_name, template_name, area_of_screenshot)


def cristal_opened() -> bool:
    """Проверка на то, что открыто меню крафта улучшенного драгоценного камня"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_craft_menu_cristal.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\craft_menu_cristal.png'
    area_of_screenshot = (975, 450, 1120, 665)

    return check(screenshot_name, template_name, area_of_screenshot)


def cristal_buy_button_available() -> bool:
    """Проверка на то, что доступна кнопка аукцион в меню крафта драгоценного камня"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_buy_craft_menu_button.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\cristal_buy_button.png'
    area_of_screenshot = (1730, 415, 1820, 490)

    return check(screenshot_name, template_name, area_of_screenshot)
