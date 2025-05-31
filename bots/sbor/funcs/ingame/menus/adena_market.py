from l2m_ui_funcs.main_screen import adena_market_opened
from bots.sbor.funcs.image.adena_market import *
from main_funcs import mouse

import time


def exit_adena_shop():
    """Выходит из адена шопа"""
    while adena_opened():
        mouse.move_and_click(1800, 100)


def close_ad():
    """Нажимает на крестик для закрытия рекламы"""
    while not there_is_cross():
        time.sleep(0.1)

    while there_is_cross():
        mouse.move_and_click(1535, 780)


def open_adena():
    """Открывает вкладку адена в магазине"""
  #  while not adena_opened():
    mouse.move_and_click(700, 190)


def click_on_inner_shop(shop_num: int):
    """Нажимает на внутренний магазин"""
    mouse.move_and_click(1690, 290 + (shop_num * 90))


def buy():
    """Открывает меню покупки во внутреннем магазине"""
    while not inner_shop_opened():
        mouse.move_and_click(1700, 990)


def confirm_buy():
    """Подтверждает покупку"""
    while not adena_opened():
        mouse.move_and_click(1070, 900)



def close_inner_shop():
    """Закрывает внутренний магазин"""
    while inner_shop_opened():
        mouse.move_and_click(780, 890)


