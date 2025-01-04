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


def open_map():
    """Открывает карту"""
    while not map_opened():
        mouse.move_and_click(160, 235)
        time.sleep(2)


def open_sellers_menu():
    """Открывает меню торговцев"""
    while not sellers_menu_opened():
        mouse.move_and_click(350, 275)
        time.sleep(0.5)


def open_adena_market():
    """Открывает адена шоп"""
    while not adena_market_opened():
        mouse.move_and_click(1430, 90)


def open_market():
    """Открывает аукцион"""
    while not market_opened():
        mouse.move_and_click(1600, 450)
        time.sleep(0.5)


def open_clan():
    """Открывает меню клана"""
    while not clan_menu_opened():
        mouse.move_and_click(1600, 575)
        time.sleep(0.5)


def open_bonuses():
    """Открывает меню бонусов"""
    while not bonuses_opened():
        mouse.move_and_click(1775, 580)
        time.sleep(0.5)


def open_messages():
    """Открывает меню сообщений"""
    while not messages_opened():
        mouse.move_and_click(1425, 825)
        time.sleep(0.5)


def open_battle_pass():
    """Открывает меню сезонного пропуска"""
    while not battle_pass_opened():
        mouse.move_and_click(1510, 820)
        time.sleep(0.5)


def open_settings():
    """Открывает меню настроек"""
    while not settings_opened():
        mouse.move_and_click(1690, 815)
        time.sleep(0.5)



