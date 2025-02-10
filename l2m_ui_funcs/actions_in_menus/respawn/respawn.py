from l2m_ui_funcs.actions_in_menus.respawn._checks import *
from main_funcs import mouse
import time


def open_respawn_menu():
    """Открывает меню возвращения предметов и опыта после смерти"""
    while not respawn_menu_opened():
        mouse.move_and_click(1260, 80)
        time.sleep(1)


def close_respawn_menu():
    """Закрывает меню возвращения предметов и опыта после смерти"""
    while respawn_menu_opened():
        mouse.move_and_click(530, 175)


def get_items():
    """Нажимает на кнопку восстановить"""
    def _click_revive_button():
        """Нажимает кнопку восстановить"""
        while not exp_confirm_button_available():
            mouse.move_and_click(310, 750)

    def _confirm():
        """Подтверждает восстановление"""
        while exp_confirm_button_available():
            mouse.move_and_click(1070, 700)

    _click_revive_button()
    _confirm()


def click_on_items():
    """Нажимает на 5 слотов восстановления после смерти"""
    for i in range(5):
        mouse.move_and_click(100, 275 + (i * 95))


def open_equipment():
    """Открывает меню снаряжения"""
    mouse.move_and_click(370, 185)


def choose_adena():
    """Выбирает адену в меню снаряжения"""
    while not adena_chosen():
        mouse.move_and_click(500, 625)


def respawn():
    """Воскрешает персонажа"""
    mouse.move_and_click(900, 870)
    time.sleep(7)


def get_lost_items():
    """Получает пропавшие из-за смерти вещи"""
    open_respawn_menu()
    time.sleep(2)

    if not nothing_to_revive():
        click_on_items()
        get_items()

    open_equipment()
    if not nothing_to_revive():
        choose_adena()
        click_on_items()
        get_items()

    close_respawn_menu()
