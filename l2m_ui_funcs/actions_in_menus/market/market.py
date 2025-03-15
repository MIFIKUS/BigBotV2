from l2m_ui_funcs.actions_in_menus.market._checks import *
from l2m_ui_funcs.checks import market_opened

from general.lists.all_items_ids import ALL_ITEMS
from general.funcs.item_name_work import transform_item_name_to_market, get_item_id, get_item_sharp

from general.packets.price import get_minimal_price_for_item, get_avg_price

from bots.autosell.funcs.image.sale_menu import get_item_name
from bots.autosell.funcs.ingame.menus.market import set_price, erase_price
from bots.autosell.funcs.image.sale_menu import get_set_price

from main_funcs import mouse
from main_funcs import keyboard

import time
import asyncio


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


def take_off_item_from_sell() -> bool:
    """Убрать вещь с меню продажи"""
    def _accept():
        """Подтверждает снятие шмотки с аука"""
        mouse.move_and_click(1080, 750)

    while not item_taking_off():
        mouse.move_and_click(1310, 360) #Нажимает кнопку забрать

    while item_taking_off():
        _accept()

    for _ in range(2):
        if inventory_overflow():
            return False
    return True


def take_item_to_sell(x: int, y: int):
    """Нажимает на шмотку в инвентаре, для дальнейшей продажи"""
    while not sell_item_menu_opened():
        mouse.move_and_click(x, y-5)


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


def open_all_items():
    """Нажимает кнопку Все на ауке"""
    while not all_items_opened():
        mouse.move_and_click(70, 380)


def open_search_area():
    """Открывает строку поиска"""
    while not search_area_opened():
        mouse.move_and_click(775, 275)


def click_on_item_in_search_area():
    """Нажимает на шмотку в строке поиска"""
    while search_area_opened():
        mouse.move_and_click(135, 300)
        time.sleep(0.5)

def set_necessary_sharp(sharp: int):
    """Устанавливает нужную заточку предмета и нажимает ок"""
    def __set_sharp(start_drag, end_drag):
        start_x = 315
        end_x = 1770

        mouse.move(start_x, 250)
        mouse.press_down()

        mouse.move(start_drag, 0, True)
        mouse.click()

        mouse.move(end_x, 250)
        mouse.press_down()

        mouse.move(-end_drag, 0, True)
        mouse.click()

    while not filters_menu_opened():
        mouse.move_and_click(480, 300)

    match sharp:
        case 0:
            __set_sharp(start_drag=0, end_drag=1460)
        case 1:
            __set_sharp(start_drag=130, end_drag=1325)
        case 2:
            __set_sharp(start_drag=265, end_drag=1190)
        case 3:
            __set_sharp(start_drag=395, end_drag=1060)
        case 4:
            __set_sharp(start_drag=530, end_drag=925)
        case 5:
            __set_sharp(start_drag=660, end_drag=795)
        case 6:
            __set_sharp(start_drag=795, end_drag=660)
        case 7:
            __set_sharp(start_drag=925, end_drag=530)
        case 8:
            __set_sharp(start_drag=1060, end_drag=395)
        case 9:
            __set_sharp(start_drag=1190, end_drag=265)
        case 10:
            __set_sharp(start_drag=1325, end_drag=130)
        case 11:
            __set_sharp(start_drag=1455, end_drag=0)

    mouse.move_and_click(1100, 955)
    while not no_item_on_market() and not get_item_price_after_set_sharp():
        time.sleep(0.1)


def click_on_item_in_list():
    """Нажимает на предмет в списке шмоток на ауке"""
    mouse.move_and_click(700, 450)


def click_to_buy_item():
    while not buy_menu_opened():
        mouse.move_and_click(700, 470)


def buy_item() -> bool:
    """Нажимает кнопку купить. Если удалось купить возвращает True если нет, возвращает False"""
    while not bought_menu_opened():
        mouse.move_and_click(1080, 925)

    statement = get_buy_statement()

    while bought_menu_opened():
        mouse.move_and_click(930, 900)

    return statement


def buy_item_by_id(item_id: str, sharp: int, price: int) -> bool:
    """Покупает предмет на ауке по id и уровню заточки"""
    item_name = ALL_ITEMS.get(item_id)
    item_name = transform_item_name_to_market(item_name)

    open_all_items()

    open_search_area()
    keyboard.type_text(item_name)
    click_on_item_in_search_area()

    time.sleep(0.2)
    set_necessary_sharp(sharp)
    time.sleep(0.2)

    for _ in range(2):
        click_on_item_in_list()
        time.sleep(2)

    if get_item_price() != price:
        return False

    click_to_buy_item()

    buy_statement = buy_item()
    return buy_statement


def set_price_for_1_piece():
    """Выбирает цену за 1 штуку"""
    while not price_for_1_piece_selected():
        mouse.move_and_click(1760, 375)


def set_sort_desc():
    """Выбирает сортировку по увеличению цену (когда выбрана цена за 1 предмет)"""
    while not price_sorted_desc():
        mouse.move_and_click(1760, 375)


def buy_cristal():
    """Покупает кристалы для крафта зелени"""
    while not get_item_price_after_set_sharp():
        time.sleep(0.1)

    set_price_for_1_piece()
    set_sort_desc()

    while not get_item_price():
        click_on_item_in_list()
        time.sleep(0.2)

    buy_item()


def get_new_item_cords() -> tuple or bool:
    """Возвращает координаты последней выпавшей шмотки"""
    while True:
        screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_item_equiped.png'
        template_name = 'general\\imgs\\templates\\item_is_equiped.png'
        prev_area_of_screenshot = ()
        for table in range(6):
            for row in range(4):
                area_of_screenshot = (1400 + (row * 100), 325 + (table * 100),
                                      1500 + (row * 100), 425 + (table * 100))
                if check(screenshot_name, template_name, area_of_screenshot):
                    return prev_area_of_screenshot[0] + 50, prev_area_of_screenshot[1] + 50
                else:
                    prev_area_of_screenshot = area_of_screenshot
        mouse.move(1600, 520)
        mouse.wheel_down(1)



def sell_last_item(server_id: str):
    """Выставляет на продажу последнюю выпавшую шмотку"""
    new_item_cords = get_new_item_cords()
    take_item_to_sell(new_item_cords[0], new_item_cords[1])

    item_name = get_item_name()
    item_id = get_item_id(item_name)
    item_sharp = get_item_sharp(item_name)

    price = get_minimal_price_for_item(server_id, item_id, item_sharp)
    if not price:
        loop = asyncio.get_event_loop()
        price = int(loop.run_until_complete(get_avg_price(item_id, item_sharp)))

    if price != 10:
        price -= 1

    while get_set_price() != price:
        set_price(price)
        if get_set_price() != price:
            erase_price()

    sell_item()


def get_amount_of_slots() -> int:
    """Получает количество свободных слотов"""
    open_sell_menu()
    time.sleep(2)

    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\amount_of_slots.png'
    area_of_screenshot = (150, 930, 235, 980)
    image.take_screenshot(screenshot_name, area_of_screenshot)
    return int(image.image_to_string(screenshot_name, True).replace('\n', '').split('/')[0])


