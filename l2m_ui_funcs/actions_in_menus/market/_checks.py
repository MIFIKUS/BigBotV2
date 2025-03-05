from general.funcs.checks import check, check_color
from general.funcs.string_work import delete_junk_symbols
from main_funcs import image


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


def all_items_opened() -> bool:
    """Проверка на то, что кнопка все в ауке нажата"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_all_items_opened.png'
    color = [245, 245, 245]
    area_of_screenshot = (49, 377, 50, 378)

    return check_color(color, screenshot_name, area_of_screenshot)


def search_area_opened() -> bool:
    """Проверка на то, что строка поиска открыта"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_search_area_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\search_area_opened.png'

    area_of_screenshot = (1600, 155, 1850, 240)

    return check(screenshot_name, template_name, area_of_screenshot)


def get_item_price() -> int or bool:
    """Получает цену шмотки по картинке в финальном меню покупки"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\item_price.png'
    area_of_screenshot = (1625, 450, 1720, 483)

    image.take_screenshot(screenshot_name, area_of_screenshot)

    item_price = image.image_to_string(screenshot_name, True)
    item_price = delete_junk_symbols(item_price)

    try:
        return int(item_price)
    except:
        return False


def get_item_price_after_set_sharp() -> int or bool:
    """Получает цену шмотки в меню после выбора заточки"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\item_price_after_set_sharp.png'
    area_of_screenshot = (1110, 445, 1200, 480)

    image.take_screenshot(screenshot_name, area_of_screenshot)

    item_price = image.image_to_string(screenshot_name, True)
    item_price = delete_junk_symbols(item_price)

    try:
        return int(item_price)
    except:
        return False


def no_item_on_market() -> bool:
    """Проверка на то, что на аукионе нет предметов"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_no_items_on_market.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\no_items_on_market.png'

    area_of_screenshot = (950, 605, 1185, 725)

    return check(screenshot_name, template_name, area_of_screenshot)


def buy_menu_opened() -> bool:
    """Проверка на то, что меню покупки открыто"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_buy_menu_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\buy_menu_opened.png'

    area_of_screenshot = (935, 880, 1235, 960)

    return check(screenshot_name, template_name, area_of_screenshot)


def bought_menu_opened() -> bool:
    """Проверка на то, что меню проверки купился ли предмет открыто"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_bought_menu_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\bought_menu_opened.png'

    area_of_screenshot = (795, 855, 1065, 935)

    return check(screenshot_name, template_name, area_of_screenshot)


def get_buy_statement() -> bool:
    """Проверка удалось ли купить шмотку, если удалось возвращает True, если нет, то False"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\buy_statement.png'
    area_of_screenshot = (1160, 295, 1280, 325)
    color = [10, 200, 80]

    while True:
        image.take_screenshot(screenshot_name, area_of_screenshot)
        image.delete_all_colors_except_one(screenshot_name, color)
        statement = image.image_to_string(screenshot_name, False)

        statement = delete_junk_symbols(statement).lower()

        if statement == 'успех':
            return True
        elif statement == 'неудача':
            return False


def price_for_1_piece_selected() -> bool:
    """Проверка на то, что выбрана цена за 1 штуку"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_price_for_1_piece_selected.png'
    color = [245, 245, 200]
    area_of_screenshot = (1760, 379, 1761, 380)

    return check_color(color, screenshot_name, area_of_screenshot)


def price_sorted_desc() -> bool:
    """Проверка на то, что выбрана цена по уменьшению(когда выбрана цена за 1 штуку)"""
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_price_sorted_desc.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\price_sorted_desc.png'

    area_of_screenshot = (1745, 365, 1775, 390)

    return check(screenshot_name, template_name, area_of_screenshot)
