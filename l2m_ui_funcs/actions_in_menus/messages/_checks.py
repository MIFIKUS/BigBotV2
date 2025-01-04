from general.funcs.checks import check, check_color


def collect_button_available() -> bool:
    """Проверка на то, что кнопка Получить все доступна"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_collect_button_available.png'
    color = [215, 105, 10]
    area_of_screenshot = (1695, 925, 1696, 926)

    return check_color(color, screenshot_name, area_of_screenshot)


def energy_collect_available() -> bool:
    """Проверка на то, что Энергия Эйнсхад превышена"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\energy_collect_available.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_energy_collect_opened.png'
    area_of_screenshot = (635, 435, 1230, 550)

    return check(screenshot_name, template_name, area_of_screenshot)

