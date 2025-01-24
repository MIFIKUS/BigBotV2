from main_funcs import image
from difflib import SequenceMatcher
from bots.alchemy.extensions.forecast_colors_names import FORECAST_COLORS_NAMES
from general.funcs.string_work import delete_junk_symbols


def get_forecast_name() -> str:
    """Получает строку которая написана в круге"""
    screenshot_name = 'bots\\alchemy\\imgs\\screenshots\\forecast_name.png'
    area_of_screenshot = (525, 675, 1345, 720)
    color = [245, 245, 245]

    image.take_screenshot(screenshot_name, area_of_screenshot)
    image.delete_all_colors_except_one(screenshot_name, color)

    forecast_name = image.image_to_string(screenshot_name, False)
    forecast_name = delete_junk_symbols(forecast_name)
    forecast_name = forecast_name.replace(' ', '').lower()

    for name in FORECAST_COLORS_NAMES.keys():
        if SequenceMatcher(a=name.replace(' ', '').lower(), b=forecast_name).ratio() > 0.9:
            return name
