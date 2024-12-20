from l2m_ui_funcs.main_screen import open_menu, open_market
from l2m_ui_funcs.actions_in_menus.market import market

from main_funcs import mouse

import time


def go_to_sell_menu():
    """Переходит в меню Продажа, предварительно зайдя в меню продано чтобы избежать бага, когда нет предметов на аукционе"""
    open_menu()
    open_market()

    while not market.loading_complete():
        time.sleep(0.1)

    market.open_sell_menu()
    market.open_sold_menu()
    market.open_sell_menu()


def set_price(price: int):
    """Вводит цену предмета"""

    price = str(price)

    for digit in price:
        print(digit)
        match digit:
            case '0':
                cords = (1300, 835)
            case '1':
                cords = (1055, 835)
            case '2':
                cords = (1140, 835)
            case '3':
                cords = (1220, 835)
            case '4':
                cords = (1055, 775)
            case '5':
                cords = (1140, 775)
            case '6':
                cords = (1220, 775)
            case '7':
                cords = (1055, 720)
            case '8':
                cords = (1140, 720)
            case '9':
                cords = (1220, 720)

        mouse.move_and_click(cords[0], cords[1])

