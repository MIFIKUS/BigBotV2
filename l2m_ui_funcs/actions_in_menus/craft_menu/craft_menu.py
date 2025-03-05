from l2m_ui_funcs.actions_in_menus.craft_menu._checks import *
from l2m_ui_funcs.actions_in_menus.market.market import buy_cristal, exit_from_market

from l2m_ui_funcs.main_screen import craft_menu_opened, open_craft_menu

from main_funcs import mouse
from main_funcs import keyboard

import time


def exit_craft_menu():
    """Выходит из меню крафта"""
    while craft_menu_opened():
        mouse.move_and_click(1790, 90)


def find_necklace():
    """Открывает меню крафта ожерелья"""
    while not search_area_opened():
        mouse.move_and_click(1760, 195)

    keyboard.type_text('Ожерелье Феникса')

    while search_area_opened():
        mouse.move_and_click(210, 300)

    while not necklace_opened():
        mouse.move_and_click(400, 290)


def open_cristal_craft_menu():
    """Открывает меню крафта кристала"""
    while not cristal_craft_button_available():
        mouse.move_and_click(1450, 400)

    while not cristal_opened():
        mouse.move_and_click(1780, 400)


def open_cristal_buy_menu():
    """Открывает меню покупки кристалов"""
    while not cristal_buy_button_available():
        mouse.move_and_click(1450, 450)

    while cristal_buy_button_available():
        mouse.move_and_click(1775, 450)


def craft():
    """Создает предмет"""
    mouse.move_and_click(1550, 950)
    time.sleep(5)


def set_max():
    """Задает максимальное количество предметов для крафта"""
    mouse.move_and_click(1070, 950)


def craft_green_item():
    """Создает зеленый предмет"""
    item_crafted = False

    while not item_crafted:
        find_necklace()
        if craft_available():
            craft()
            return
        else:
            open_cristal_craft_menu()
            if craft_available():
                set_max()
                craft()
                continue
            else:
                open_cristal_buy_menu()
                buy_cristal()

                exit_from_market()
                exit_craft_menu()

