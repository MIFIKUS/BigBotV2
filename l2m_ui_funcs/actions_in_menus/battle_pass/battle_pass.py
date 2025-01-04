from l2m_ui_funcs.actions_in_menus.battle_pass._checks import *
from l2m_ui_funcs.checks import battle_pass_opened

from main_funcs import mouse


def exit_from_battle_pass():
    """Выходит из меню боевого пропуска"""
    while battle_pass_opened():
        mouse.move_and_click(1800, 90)


def click_on_battle_pass(battle_pass_num: int):
    """Нажимает на выбранную вкладку боевого пропуска"""
    mouse.move_and_click(220 + (battle_pass_num * 300), 190)


def click_on_sub_battle_pass(sub_battle_pass_num: int):
    """Нажимает на выбранную под вкладку боевого пропуска"""
    mouse.move_and_click(90, 300 + (90 * sub_battle_pass_num))


def get_battle_pass_reward():
    """Собирает общую награду боевого пропуска"""
    mouse.move_and_click(1445, 950)


def get_sub_battle_pass_reward():
    """Нажимает кнопку получить в боевом пропуске"""
    mouse.move_and_click(1300, 320)
