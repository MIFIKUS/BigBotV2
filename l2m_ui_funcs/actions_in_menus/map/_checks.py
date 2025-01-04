from general.funcs.checks import check, check_color


def favorites_opened() -> bool:
    """Проверка на то, что избранное открыто"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_favorites_opened.png'
    color = [245, 100, 10]
    area_of_screenshot = (170, 205, 171, 206)

    return check_color(color, screenshot_name, area_of_screenshot)


def town_opened() -> bool:
    """Проверка на то, что нажалось на нужный город"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_town_opened.png'
    color = [215, 100, 10]
    area_of_screenshot = (1610, 695, 1611, 696)

    return check_color(color, screenshot_name, area_of_screenshot)


def teleport_confirm_menu_opened() -> bool:
    """Проверка на то, что меню подтверждения телепортации открыто"""
    template_name = 'bots\\sbor\\imgs\\templates\\teleport_confirm_button.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_there_teleport_confirm_button.png'
    area_of_screenshot = (935, 670, 1220, 745)

    return check(screenshot_name, template_name, area_of_screenshot)
