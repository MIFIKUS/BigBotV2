from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import repeat_forecast
from l2m_ui_funcs.actions_in_menus.alchemy._checks import get_forecast_color

import time


def get_necessary_forecast_color(colors: list):
    """Повторяет прогноз пока не будет нужный цвет круга"""
    while get_forecast_color() not in colors:
        repeat_forecast()
        time.sleep(0.65y)