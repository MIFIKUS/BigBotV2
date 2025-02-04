from general.funcs.checks import check, check_color


def locations_menu_opened() -> bool:
    """Проверка на то, что меню сохраненных локаций открыто"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_locations_menu_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\locations_menu_opened.png'
    area_of_screenshot = (350, 240, 465, 310)

    return check(screenshot_name, template_name, area_of_screenshot)


def location_opened() -> bool:
    """Проверка на то, что локация выбрана"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_location_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\location_opened.png'
    area_of_screenshot = (400, 395, 445, 450)

    return check(screenshot_name, template_name, area_of_screenshot)