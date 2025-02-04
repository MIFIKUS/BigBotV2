from l2m_ui_funcs.actions_in_menus.locations._checks import *
from main_funcs import mouse

import time


def open_locations_menu():
    """Открывает меню локаций"""
    while not locations_menu_opened():
        mouse.move_and_click(350, 185)
        time.sleep(1)

def tp_to_last_location(need_to_auto_hunt=True):
    """Телепортирует персонажа в последнюю локацию"""
    open_locations_menu()

    while not location_opened():
        mouse.move_and_click(250, 350)

    while location_opened():
        mouse.move_and_click(415, 415)

    if need_to_auto_hunt:
        time.sleep(4)
        mouse.move_and_click(1530, 550)