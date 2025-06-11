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
    time.sleep(1)
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
        time.sleep(0.5)


def open_classes_menu():
    """Открывает меню классов"""
    while not classes_opened():
        mouse.move_and_click(1340, 220)
        time.sleep(0.5)


def open_aghathions_menu():
    """Открывает меню агатионов"""
    while not aghations_opened():
        mouse.move_and_click(1430, 220)


def open_alchemy():
    """Открывает меню алхимии"""
    while not alchemy_opened():
        mouse.move_and_click(1780, 340)
        time.sleep(0.5)


def open_craft_menu():
    """Открывает меню создания"""
    while not craft_menu_opened():
        mouse.move_and_click(1350, 460)
        time.sleep(0.5)


def open_market():
    """Открывает аукцион"""
    while not market_opened():
        mouse.move_and_click(1420, 450)
        time.sleep(0.5)


def open_clan():
    """Открывает меню клана"""
    while not clan_menu_opened():
        mouse.move_and_click(1690, 450)
        time.sleep(0.5)


def open_bonuses():
    """Открывает меню бонусов"""
    while not bonuses_opened():
        mouse.move_and_click(1420, 570)
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



