from l2m_ui_funcs.checks import messages_opened
from l2m_ui_funcs.actions_in_menus.messages._checks import *
from main_funcs import mouse


def exit_from_messages():
    """Выходит из меню сообщений"""
    while messages_opened():
        mouse.move_and_click(1790, 95)


def collect():
    """Собирает бонусы из меню сообщений"""
    fail_count = 0
    while collect_button_available():
        mouse.move_and_click(1580, 950)
        if fail_count > 50:
            return False
        fail_count += 1
    return True

def decline_collect_energy():
    """Нажимает отмена в меню сбора энергии Эйнсхад"""
    while energy_collect_available():
        mouse.move_and_click(790, 705)
