from general.funcs.acc_info import get_server_id, get_global_server_id
from general.funcs.item_name_work import get_item_id, get_item_sharp
from general.packets.price import get_minimal_price_for_item

from l2m_ui_funcs.actions_in_menus.settings.settings import turn_off_auto_collect, turn_on_auto_collect, exit_from_settings
from l2m_ui_funcs.actions_in_menus.market.market import (take_off_item_from_sell, take_item_to_sell, sell_item,
                                                         collect_income, open_global_market, cancel_selling_item, exit_from_market,
                                                         open_sell_menu)

from bots.autosell.funcs.ingame.menus.market import go_to_sell_menu, set_price, erase_price
from bots.autosell.funcs.image.sale_menu import (no_items_to_replace, check_if_all_items_are_replaced, get_old_price,
                                                 get_equiped_item_cords, get_item_name, get_set_price)

from bots.autosell.funcs.calculations.price import calculate_price

from general.logs.logger import logger

from main_funcs import windows

import time


def run():
    logger.info('Попытка получить ID сервера')
    server_id = get_server_id()
    if not server_id:
        logger.info('Не удалось определить ID сервера')
        return False

    logger.info(f'Удалось определить ID сервера: {server_id}')

    turn_off_auto_collect()

    logger.info('Отключен автоподбор шмоток')

    for is_global in range(2):
        is_global = bool(is_global)
        logger.info(f'Начало перестановки is_global: {is_global}')

        if is_global:
            server_id = get_global_server_id(server_id)
            logger.info(f'ID сервера для глобал маркета {server_id}')

            open_global_market()
            logger.info('Открыта вкладка глобал маркета')

            open_sell_menu()
            logger.info('Открыто меню продажи для глобал маркета')
        else:
            go_to_sell_menu()
            logger.info('Открыто вкладка продажи')

        if no_items_to_replace(is_global):
            logger.info('Нет шмоток чтобы переставить')
        else:
            logger.info('Есть шмотки чтобы переставить')

            x, y = get_equiped_item_cords()
            logger.info(f'Координаты экипированной шмотки x: {x} y: {y}')

            while not check_if_all_items_are_replaced():
                old_price = get_old_price()
                logger.info(f'Старая цена {old_price}')

                if not take_off_item_from_sell(): #Проверка переполнен ли инвентарь
                    logger.info('Инвентарь переполнен')
                    break

                take_item_to_sell(x, y)
                logger.info('Шмотка снята с продажа')

                item_name = get_item_name()
                logger.info(f'Имя предмета {item_name}')

                item_sharp = get_item_sharp(item_name)
                logger.info(f'Заточка предмета {item_sharp}')

                item_id = get_item_id(item_name)
                logger.info(f'ID предмета {item_id}')

                minimal_price = get_minimal_price_for_item(server_id, item_id, item_sharp)

                logger.info(f'Минимальная цена на сервере {minimal_price}')

                new_price = calculate_price(old_price, minimal_price, is_global)

                logger.info(f'Новая цена {new_price}')

                if new_price is False:
                    logger.info('Красная шмотка стоит меньше нужного')
                    cancel_selling_item()
                    logger.info('Отмена выставления шмотки на продажу')
                    continue

                while get_set_price() != new_price:
                    set_price(new_price)
                    logger.info('Новая цена выставлена')

                    if get_set_price() != new_price:
                        logger.info('Новая цена выставлена не правильно')
                        erase_price()
                        logger.info('Цена стерта')

                sell_item()
                logger.info('Шмотка выставлена на продажу')
                time.sleep(0.3)

        collect_income()
        logger.info('Доход собран')

    exit_from_market()
    logger.info('Вышел из аука')

    turn_on_auto_collect(True)
    logger.info('Включен автоподбор')

    exit_from_settings()
    logger.info('Вышел из меню настроек')


def start():
    windows.switch_windows(run)



