from l2m_ui_funcs.actions_in_menus.alchemy._checks import *
from main_funcs import mouse, keyboard


def click_on_item(table: int, row: int):
    """Нажимает на предмет в инвентаре"""
    mouse.move_and_click(1445 + (100 * row), 310 + (100 * table))


def click_on_item_in_forecast(slot: int):
    """Нажимает на предмет в меню прогноза"""
    mouse.move_and_click(730 + (slot * 100), 500)


def open_forecast():
    """Открывает прогноз в меню алхимии"""
    while not forecast_opened():
        keyboard.y()


def reset_forecast():
    """Заново повторяет прогноз в меню алхимии"""
    while forecast_opened():
        keyboard.y()


def repeat_forecast():
    """Открывает и закрывает прогноз"""
    open_forecast()
    reset_forecast()


def close_forecast():
    """Закрывает меню прогноза в меню алхимии"""
    while forecast_opened():
        keyboard.esc()
