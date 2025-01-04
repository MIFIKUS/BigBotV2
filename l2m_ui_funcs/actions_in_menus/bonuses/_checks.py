from general.funcs.checks import check, check_color


def bonus_for_diamonds() -> bool:
    """Проверка на то, что бонус покупается за кристаллы"""
    template_name = 'bots\\sbor\\imgs\\templates\\bonuses_diamond.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_bonuses_diamond.png'
    area_of_screenshot = (1255, 530, 1575, 595)

    return check(screenshot_name, template_name, area_of_screenshot)


def bonus_for_compas() -> bool:
    """Проверка на то, что бонус за компасы"""
    template_name = 'bots\\sbor\\imgs\\templates\\bonuses_compas.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_bonuses_compas.png'
    area_of_screenshot = (1255, 530, 1575, 595)

    return check(screenshot_name, template_name, area_of_screenshot)

def bonus_unavailable() -> bool:
    """Проверка на то, что бонус не доступен"""
    template_name = 'bots\\sbor\\imgs\\templates\\bonus_unavailable.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_bonus_unavailable.png'
    area_of_screenshot = (630, 460, 990, 505)

    return check(screenshot_name, template_name, area_of_screenshot)


def no_more_bonuses(bonus_pos: int) -> bool:
    """Проверка на то, что больше не осталось бонусов"""
    template_name = 'bots\\sbor\\imgs\\templates\\no_more_bonuses.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_no_more_bonuses.png'
    area_of_screenshot = (1600, 200 + (bonus_pos * 110), 1830, 310 + (bonus_pos * 110))

    return check(screenshot_name, template_name, area_of_screenshot)


def bonus_unused() -> bool:
    """Проверка на то, что бонус не собран"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_bonus_unused.png'
    color = [215, 105, 10]
    area_of_screenshot = (1375, 535, 1376, 536)

    return check_color(color, screenshot_name, area_of_screenshot)


def need_to_confirm() -> bool:
    """Проверка на то, нужно ли подтвердить получение бонуса"""
    template_name = 'bots\\sbor\\imgs\\templates\\need_to_confirm_bonus.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_need_to_confirm_bonus.png'
    area_of_screenshot = (935, 670, 1220, 745)

    return check(screenshot_name, template_name, area_of_screenshot)
