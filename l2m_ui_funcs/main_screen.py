from main_funcs import mouse, keyboard
from l2m_ui_funcs.checks import *

import time


def unlock_screen():
    """Разблокирует окно"""
    while window_locked():
        print(123)
        mouse.move(960, 540)
        mouse.drag(100, 100, True)


def lock_screen():
    """Блокирует окно"""
    mouse.move_and_click(70, 640)
    mouse.move_and_click(940, 550)

def open_menu():
    """Открывает меню"""
    while not menu_opened():
        mouse.move_and_click(1775, 85)
        time.sleep(0.5)


def open_market():
    """Открывает аукцион"""
    while not market_opened():
        mouse.move_and_click(1600, 450)
        time.sleep(0.5)


def open_settings():
    """Открывает меню настроек"""
    while not settings_opened():
        mouse.move_and_click(1690, 815)
        time.sleep(0.5)



