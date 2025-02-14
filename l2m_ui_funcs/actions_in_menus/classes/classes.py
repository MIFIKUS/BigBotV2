from l2m_ui_funcs.actions_in_menus.classes._checks import *
from l2m_ui_funcs.main_screen import classes_opened
from main_funcs import mouse

import time


def exit_classes_menu():
    """Выходит из меню классов"""
    while classes_opened():
        mouse.move_and_click(1780, 90)


def open_classes_list():
    """Открывает вкладку Классы"""
    while not classes_list_opened():
        mouse.move_and_click(370, 190)


def open_fuses_list():
    """Открывает вкладку Синтез"""
    while not fuses_list_opened():
        mouse.move_and_click(790, 190)


def open_confirm_list():
    """Открывает вкладку подтверждения класса"""
    while not confirm_list_opened():
        mouse.move_and_click(1200, 190)


def confirm_all():
    """Подтверждает получение классов"""
    while not confirm_all_opened():
        mouse.move_and_click(1545, 970)

    while confirm_all_opened():
        mouse.move_and_click(1070, 720)


def auto_select() -> bool or None:
    """Закладывает карты в слияние\n
    Если больше нет карт для слияния возвращает False"""
    while not fuse_available():
        mouse.move_and_click(1000, 950)
        if no_more_fuse():
            return False


def fuse():
    """Сливает карты"""
    while not show_all_available() and not go_to_result_available():
        mouse.move_and_click(1400, 950)
        time.sleep(0.1)

def show_all():
    """Нажимает показать все"""
    while not repeat_available() and not exit_available():
        mouse.move_and_click(930, 950)
        time.sleep(0.1)

def repeat():
    """Повторяет слияние"""
    while repeat_available():
        mouse.move_and_click(1110, 950)
        time.sleep(0.1)

def exit_fuse():
    """Закрывает результат слияния"""
    while exit_available():
        mouse.move_and_click(950, 950)


def go_to_result():
    """Нажимает на кнопку перейти к результату"""
    while go_to_result_available():
        mouse.move_and_click(930, 950)
    time.sleep(3)


def reopen_fuse_menu():
    """Переоткрывает меню слияния"""
    open_classes_list()
    open_fuses_list()

