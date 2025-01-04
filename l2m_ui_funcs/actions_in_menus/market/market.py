from l2m_ui_funcs.actions_in_menus.market._checks import *
from l2m_ui_funcs.checks import market_opened
from main_funcs import mouse

import time


def exit_from_market():
    """Выходит из аукциона"""
    while market_opened():
        mouse.move_and_click(1800, 100)
        time.sleep(1)


def open_global_market():
    """Открывает мировой аукцион"""
    while not global_market_opened():
        mouse.move_and_click(1400, 95)


def open_sell_menu():
    """Открывает в аукционе меню Продажа"""
    while not sell_menu_opened():
        mouse.move_and_click(400, 190)


def open_sold_menu():
    """Открывает в аукционе меню Продано"""
    while not sold_menu_opened():
        mouse.move_and_click(650, 190)


def take_off_item_from_sell() -> None or bool:
    """Убрать вещь с меню продажи"""
    def _accept():
        """Подтверждает снятие шмотки с аука"""
        mouse.move_and_click(1080, 750)

    while not item_taking_off():
        mouse.move_and_click(1310, 360) #Нажимает кнопку забрать
        if inventory_overflow():
            return False

    while item_taking_off():
        _accept()


def take_item_to_sell(x: int, y: int):
    """Нажимает на шмотку в инвентаре, для дальнейшей продажи"""
    while not sell_item_menu_opened():
        mouse.move_and_click(x, y)


def sell_item():
    """Выставляет предмет на аукцион"""
    def _click_ok_button():
        """Нажимает кнопку ок"""
        while there_is_ok_button_in_sell_menu():
            mouse.move_and_click(1100, 910)

    def _click_add_button():
        """Нажимает кнопку добавить"""
        while there_is_add_button():
            mouse.move_and_click(950, 750)

    _click_ok_button()
    _click_add_button()


def collect_income():
    """Получает доход с аукциона"""
    open_sold_menu()
    while not there_is_income():
        mouse.move_and_click(1550, 980)


def cancel_selling_item():
    """Отменят продажу шмотки"""
    while there_is_cancel_button():
        mouse.move_and_click(770, 925)