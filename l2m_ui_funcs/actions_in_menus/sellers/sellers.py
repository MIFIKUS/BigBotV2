from l2m_ui_funcs.actions_in_menus.sellers._checks import *
from l2m_ui_funcs.checks import sellers_menu_opened

from main_funcs import mouse

import time


def exit_sellers_menu():
    """Закрывает меню торговцев"""
    while sellers_menu_opened():
        mouse.move_and_click(355, 270)


def _go_to_seller(position: int):
    """Нажимает на нужного торговца"""
    mouse.move_and_click(125, 190 + (position * 60))
    while not came_to_seller() and not came_to_event_seller() and not came_to_event():
        time.sleep(0.1)


def _buy():
    """Покупает вещи в автопокупке у торговцев"""
    mouse.move_and_click(1470, 950)
    mouse.move_and_click(1700, 950)
    mouse.move_and_click(1050, 700)
    mouse.move_and_click(1790, 100)


def collect_event(position: int):
    """Идет к ивенту"""
    _go_to_seller(position)

    while not came_to_event() and not came_to_seller() and not came_to_event_seller():
        time.sleep(0.1)

    if came_to_event():
        mouse.move_and_click(1080, 720)
    else:
        _buy()


def collect_grocer(position):
    """Делает все нужное у бакалейщика"""
    _go_to_seller(position)
    print(22323)
    _buy()


def collect_sklad(position):
    """Делает все нужное у склада"""
    _go_to_seller(position)
    _buy()


def collect_buyer(position):
    """Делает все нужное у скупщика"""
    _go_to_seller(position)
    _buy()

