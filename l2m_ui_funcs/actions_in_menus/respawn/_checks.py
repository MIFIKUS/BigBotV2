from general.funcs.checks import check, check_color
from main_funcs import image


def dead() -> bool:
    """Проверка на то, мертв ли персонаж"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\dead.png'
    template_name_1 = 'l2m_ui_funcs\\imgs\\templates\\dead2.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_dead.png'

    area_of_screenshot = None

    if check(screenshot_name, template_name, area_of_screenshot) or check(screenshot_name, template_name_1, area_of_screenshot):
        return True
    return False


def respawn_menu_opened() -> bool:
    """Проверка на то, что меню возвращения шмоток и опыта после смерти открыто"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\respawn_menu_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_respawn_menu_opened.png'
    area_of_screenshot = (510, 155, 550, 195)

    return check(screenshot_name, template_name, area_of_screenshot)


def exp_confirm_button_available() -> bool:
    """Проверяет доступна ли кнопка подтверждения при получении опыта"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_exp_confirm_button_available.png'
    color = [215, 105, 10]
    area_of_screenshot = (1125, 690, 1126, 691)

    return check_color(color, screenshot_name, area_of_screenshot)


def adena_chosen() -> bool:
    """Проверяет что в меню снаряжения выбрана адена"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\adena_chosen.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_adena_chosen.png'
    area_of_screenshot = (445, 610, 477, 645)

    return check(screenshot_name, template_name, area_of_screenshot)


def nothing_to_revive() -> bool:
    """Проверка на то, есть ли вещи или опыт который нужно восстановить"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\nothing_to_revive.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_nothing_to_revive.png'
    area_of_screenshot = (135, 350, 475, 475)

    return check(screenshot_name, template_name, area_of_screenshot)

