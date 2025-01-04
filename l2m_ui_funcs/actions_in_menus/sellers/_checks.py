from general.funcs.checks import check, check_color


def get_amount_of_events() -> int:
    """Получает количество ивентов"""
    template_name = 'bots\\sbor\\imgs\\templates\\sellers_event_1.png'
    template_name_1 = 'bots\\sbor\\imgs\\templates\\sellers_event_2.png'

    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_sellers_event_1.png'
    screenshot_name_1 = 'bots\\sbor\\imgs\\screenshots\\is_sellers_event_2.png'

    area_of_screenshot = (65, 160, 180, 195)
    area_of_screenshot_1 = (65, 225, 180, 260)

    amount_of_events = 0

    if check(screenshot_name, template_name, area_of_screenshot) or check(screenshot_name, template_name_1, area_of_screenshot):
        amount_of_events += 1
    else:
        return 0

    if check(screenshot_name_1, template_name, area_of_screenshot_1) or check(screenshot_name_1, template_name_1, area_of_screenshot_1):
        amount_of_events += 1

    return amount_of_events


def came_to_seller() -> bool:
    """Проверка на то, что персонаж пришел к торговцу"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_came_to_seller.png'
    color = [65, 75, 90]
    area_of_screenshot = (1470, 920, 1471, 921)

    return check_color(color, screenshot_name, area_of_screenshot)


def came_to_event() -> bool:
    """Проверка на то, что персонаж пришел к ивенту"""
    template_name = 'bots\\sbor\\imgs\\templates\\came_to_event.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_came_to_event.png'
    area_of_screenshot = (930, 665, 1225, 750)

    return check(screenshot_name, template_name, area_of_screenshot)


def came_to_event_seller() -> bool:
    """Проверка на то, что персонаж пришел к ивентовому торговцу"""
    template_name = 'bots\\sbor\\imgs\\templates\\came_to_event_seller.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_came_to_event_seller.png'
    area_of_screenshot = (1380, 905, 1600, 990)

    return check(screenshot_name, template_name, area_of_screenshot)


def buy_available() -> bool:
    """Проверка на то, что кнопка купить доступна"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_sellers_buy_available.png'
    color = [215, 105, 10]
    area_of_screenshot = (1700, 925, 1701, 926)

    return check_color(color, screenshot_name, area_of_screenshot)


def confirm_buy_available() -> bool:
    """Проверка на то, что кнопка подтверждения покупки доступна"""
    template_name = 'bots\\sbor\\imgs\\templates\\sellers_confirm_button.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_sellers_confirm_button_available.png'
    area_of_screenshot = (935, 670, 1220, 745)

    return check(screenshot_name, template_name, area_of_screenshot)