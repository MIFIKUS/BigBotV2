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
