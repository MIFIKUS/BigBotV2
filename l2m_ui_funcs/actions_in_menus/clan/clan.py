from l2m_ui_funcs.actions_in_menus.clan._checks import *
from l2m_ui_funcs.checks import clan_menu_opened

from main_funcs import mouse


def exit_from_clan_menu():
    """Выходит из меню кланов"""
    while clan_menu_opened():
        mouse.move_and_click(1780, 90)


def open_contribution_menu():
    """Открывает меню взноса"""
    while not contribution_menu_opened():
        mouse.move_and_click(995, 950)


def close_contribution_menu():
    while contribution_menu_opened():
        mouse.move_and_click(1580, 160)


def make_contribute():
    """Делает взнос"""
    def _contribute():
        """Нажимает кнопку сделать взнос"""
        while not accept_contribute_opened():
            mouse.move_and_click(465, 805)

    def _accept():
        """Подтверждает взнос"""
        while accept_contribute_opened():
            mouse.move_and_click(1070, 710)

    _contribute()
    _accept()


def get_reward():
    """Получает награду за посещаемость"""
    mouse.move_and_click(485, 755)
