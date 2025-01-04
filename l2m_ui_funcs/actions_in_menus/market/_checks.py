from general.funcs.checks import check, check_color


def loading_complete() -> bool:
    """Проверка на то, что загрузка в аукционе завершена"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_loading_complete.png'
    color = [255, 255, 255]
    area_of_screenshot = (50, 275, 51, 276)

    return check_color(color, screenshot_name, area_of_screenshot)


def global_market_opened() -> bool:
    """Проверка на то, что мировой аукцион открыт"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_global_market_opened.png'
    color = [255, 255, 255]
    area_of_screenshot = (1335, 93, 1336, 94)

    return check_color(color, screenshot_name, area_of_screenshot)


def sell_menu_opened() -> bool:
    """Проверка на то, что вкладка Продажа открыта"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_sell_menu_opened.png'
    color = [255, 255, 255]
    area_of_screenshot = (355, 175, 356, 176)

    return check_color(color, screenshot_name, area_of_screenshot)


def sold_menu_opened() -> bool:
    """Проверка на то, что вкладка Продано открыта"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_sold_menu_opened.png'
    color = [255, 255, 255]
    area_of_screenshot = (603, 175, 604, 176)

    return check_color(color, screenshot_name, area_of_screenshot)


def sell_item_menu_opened() -> bool:
    """Проверка на то, что меню выставления шмотки на продажу открыто"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_sell_item_menu_opened.png'
    color = [215, 105, 10]
    area_of_screenshot = (1150, 905, 1151, 906)

    return check_color(color, screenshot_name, area_of_screenshot)


def item_taking_off() -> bool:
    """Проверка на то, нажалась ли кнопка снятия с продажи у предмета"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_item_taking_off.png'
    color = [215, 105, 10]
    area_of_screenshot = (1110, 745, 1111, 746)

    return check_color(color, screenshot_name, area_of_screenshot)


def there_is_ok_button_in_sell_menu() -> bool:
    """Проверка на то, что есть кнопка ок при выставлении на аукцион"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_ok_button.png'
    color = [215, 105, 10]
    area_of_screenshot = (1120, 905, 1121, 906)

    return check_color(color, screenshot_name, area_of_screenshot)


def there_is_add_button() -> bool:
    """Проверка на то, что есть кнопка добавить при выставлении на аукцион"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_add_button.png'
    color = [215, 105, 10]
    area_of_screenshot = (1110, 745, 1111, 746)

    return check_color(color, screenshot_name, area_of_screenshot)


def there_is_income() -> bool:
    """Проверка на то, что есть доход в списке продано"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_income.png'
    color = [30, 35, 45]
    area_of_screenshot = (1580, 960, 1581, 961)

    return check_color(color, screenshot_name, area_of_screenshot)


def there_is_cancel_button() -> bool:
    """Проверка на то, что есть кнопка отмена"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_there_cancel_button.png'
    color = [70, 75, 90]
    area_of_screenshot = (700, 900, 701, 901)

    return check_color(color, screenshot_name, area_of_screenshot)


def inventory_overflow() -> bool:
    """Проверка на то, что инвентарь переполнен"""
    screenshot_name = 'bots\\autosell\\imgs\\screenshots\\is_inventory_overflow.png'
    template_name = 'bots\\autosell\\imgs\\templates\\inventory_is_overflow.png'
    template_name_2 = 'bots\\autosell\\imgs\\templates\\inventory_is_overflow_2.png'

    area_of_screenshot = None

    return check(screenshot_name, template_name, area_of_screenshot) or check(screenshot_name, template_name_2, area_of_screenshot)
