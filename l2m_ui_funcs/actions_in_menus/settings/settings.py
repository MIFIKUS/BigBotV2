from main_funcs import mouse
from l2m_ui_funcs.actions_in_menus.settings._checks import *
from l2m_ui_funcs.checks import settings_opened

import time


def exit_from_settings():
    while settings_opened():
        mouse.move_and_click(1800, 100)
        time.sleep(1)


def open_attack_menu():
    """Открывает вкладку бой в настройках"""
    while not attack_menu_opened():
        mouse.move_and_click(180, 200)
        time.sleep(0.5)


def open_collect_menu():
    """Открывает во вкладке Бой меню подбор"""
    while not collect_menu_opened():
        mouse.move_and_click(170, 395)
        time.sleep(0.5)


def turn_off_auto_collect():
    """Отключает автоподбор снаряжения"""
    def _turn_off_auto_collect_equipment():
        while not equipment_auto_collect_off():
            mouse.move_and_click(1700, 290)

    def _turn_off_items_auto_collect():
        while not items_auto_collect_off():
            mouse.move_and_click(1700, 500)

    open_attack_menu()
    open_collect_menu()

    _turn_off_auto_collect_equipment()
    _turn_off_items_auto_collect()


def open_information_menu():
    """Открывает вкладку информации в настройках"""
    while not information_menu_opened():
        mouse.move_and_click(1570, 190)
