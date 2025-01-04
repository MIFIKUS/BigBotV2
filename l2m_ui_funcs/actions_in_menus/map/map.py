from main_funcs import mouse
from l2m_ui_funcs.actions_in_menus.map._checks import *
from l2m_ui_funcs.main_screen import open_map

import time


def open_favorites():
    """Открывает Избранное в карте"""
    while not favorites_opened():
        mouse.move_and_click(180, 190)


def click_on_town():
    """Нажимает на нужный город в избранном"""
    while not town_opened():
        mouse.move_and_click(150, 320)


def teleport():
    """Телепортирует"""
    while not teleport_confirm_menu_opened():
        mouse.move_and_click(1600, 710)

    while teleport_confirm_menu_opened():
        mouse.move_and_click(1080, 710)


def teleport_to_town():
    """Телепортирует персонажа в город"""
    open_map()

    open_favorites()
    click_on_town()

    teleport()

    time.sleep(6)

