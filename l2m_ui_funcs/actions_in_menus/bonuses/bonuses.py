from main_funcs import mouse
from l2m_ui_funcs.actions_in_menus.bonuses._checks import *
from l2m_ui_funcs.checks import bonuses_opened

import time


def exit_from_bonuses():
    """Выходит из меню бонусов"""
    while bonuses_opened():
        mouse.move_and_click(1800, 85)


def click_on_bonus(bonus_pos):
    """Нажимает на бонус"""
    mouse.move_and_click(1715, 250 + (bonus_pos * 110))


def get_bonus():
    """Получает бонус"""
    while bonus_unused():
        mouse.move_and_click(1400, 555)
    time.sleep(0.5)

    if need_to_confirm():
        while need_to_confirm():
            mouse.move_and_click(1050, 710)
