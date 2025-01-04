from general.funcs.checks import check, check_color
from main_funcs import image


def there_is_cross() -> bool:
    """Проверка на то, что есть крестик"""
    template_name = 'bots\\sbor\\imgs\\templates\\cross_adena_shop.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_there_cross_adena_shop.png'
    area_of_screenshot = (1510, 765, 1555, 815)

    return check(screenshot_name, template_name, area_of_screenshot)


def adena_opened() -> bool:
    """Проверка на то, что вкладка Адены открыта"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_adena_opened.png'
    color = [255, 255, 255]
    area_of_screenshot = (375, 188, 376, 189)

    return check_color(color, screenshot_name, area_of_screenshot)


def inner_shop_opened() -> bool:
    """Проверка на то, что внутренний магазин открыт"""
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_inner_shop_opened.png'
    color = [215, 100, 10]
    color_1 = [105, 50, 10]
    area_of_screenshot = (1105, 865, 1106, 866)

    if check_color(color, screenshot_name, area_of_screenshot) or check_color(color_1, screenshot_name, area_of_screenshot):
        return True
    return False


def nothing_to_buy() -> bool:
    """Проверка на то, что ничего не выбрано во внутреннем магазине"""
    template_name = 'bots\\sbor\\imgs\\templates\\nothing_to_buy.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_nothing_to_buy.png'
    area_of_screenshot = (845, 800, 1015, 840)

    return check(screenshot_name, template_name, area_of_screenshot)
