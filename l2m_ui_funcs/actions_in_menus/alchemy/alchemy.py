from l2m_ui_funcs.actions_in_menus.alchemy._checks import *
from l2m_ui_funcs.main_screen import alchemy_opened
from main_funcs import mouse, keyboard

import time


def exit_from_alchemy():
    """Выходит из меню алхимии"""
    while alchemy_opened():
        mouse.move_and_click(1800, 80)


def click_on_item(table: int, row: int):
    """Нажимает на предмет в инвентаре"""
    mouse.move_and_click(1445 + (100 * row), 310 + (100 * table))


def click_on_item_in_forecast(slot: int):
    """Нажимает на предмет в меню прогноза"""
    mouse.move_and_click(730 + (slot * 100), 500)


def open_forecast():
    """Открывает прогноз в меню алхимии"""
    while not forecast_opened():
        time.sleep(0.5)
        keyboard.y()


def reset_forecast():
    """Заново повторяет прогноз в меню алхимии"""
 #   while forecast_opened():
    time.sleep(0.5)
    keyboard.y()


def repeat_forecast():
    """Открывает и закрывает прогноз"""
    open_forecast()
    reset_forecast()


def repeat_forecast_instant():
    """Мгновенно меняет прогноз"""
    for _ in range(2):
        keyboard.y()


def close_forecast():
    """Закрывает меню прогноза в меню алхимии"""
    while forecast_opened():
        keyboard.esc()


def reset_forecast_items():
    """Сбрасывает выбранные предметы в ролле"""
    if need_to_reset_forecast_items():
        while not reset_items_menu_opened():
            mouse.move_and_click(205, 950)

        while reset_items_menu_opened():
            mouse.move_and_click(1070, 700)


def start_roll():
    """Запускает создание ролла, и подтверждает его"""
    while not start_roll_menu_opened():
        mouse.move_and_click(1400, 950)
    while start_roll_menu_opened():
        mouse.move_and_click(1090, 700)

    while not confirm_roll_button_available():
        mouse.move_and_click(930, 800)
    while confirm_roll_button_available():
        mouse.move_and_click(930, 950)
