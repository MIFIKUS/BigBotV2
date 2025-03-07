from bots.alchemy.extensions import forecast_colors, forecast_colors_names
from general.funcs.checks import check, check_color
from main_funcs import image


def forecast_opened() -> bool:
    """Проверка на то, что предсказание открыто"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\is_forecast_opened.png'
    color = [210, 95, 10]
    area_of_screenshot = (1150, 795, 1151, 796)

    return check_color(color, screenshot_name, area_of_screenshot)


def get_forecast_color() -> str or bool:
    """Получает цвет круга"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\forecast_color.png'
    area_of_screenshot = (940, 555, 941, 556)

    forecast_colors_list = (forecast_colors.WHITE, forecast_colors.BLUE, forecast_colors.GOLD)
    forecast_colors_names_list = (forecast_colors_names.WHITE, forecast_colors_names.BLUE, forecast_colors_names.GOLD)

    for color, color_name in zip(forecast_colors_list, forecast_colors_names_list):
        if check_color(color, screenshot_name, area_of_screenshot):
            print(color_name)
            return color_name

    return False


def need_to_reset_forecast_items() -> bool:
    """Проверка на то, нужно ли сбрасывать предметы"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\need_to_reset_items.png'
    color = [70, 75, 90]
    area_of_screenshot = (170, 925, 171, 926)

    return check_color(color, screenshot_name, area_of_screenshot)


def reset_items_menu_opened() -> bool:
    """Проверка на то, что меню сброса предметов открыто"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\is_reset_items_menu_opened.png'
    template_name = 'l2m_ui_funcs\\imgs\\templates\\reset_items_button.png'
    area_of_screenshot = (935, 660, 1220, 735)

    return check(screenshot_name, template_name, area_of_screenshot)


def start_roll_menu_opened() -> bool:
    """Проверка на то, что меню старта ролла открыто"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\is_start_roll_menu_opened.png'
    template_name = 'bots\\alchemy\\imgs\\templates\\start_roll_menu_opened.png'
    area_of_screenshot = (935, 650, 1220, 735)

    return check(screenshot_name, template_name, area_of_screenshot)


def confirm_roll_button_available() -> bool:
    """Проверка на то, что есть кнопка подтверждения результатов ролла"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\is_there_confirm_roll_button.png'
    template_name = 'bots\\alchemy\\imgs\\templates\\confirm_roll_button.png'
    area_of_screenshot = (785, 905, 1075, 990)

    return check(screenshot_name, template_name, area_of_screenshot)

