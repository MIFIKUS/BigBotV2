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


def run():
    server_id = get_server_id()
    if not server_id:
        print('Не удалось определить ID сервера')
        return False

    print(f'Удалось определить ID сервера: {server_id}')

    turn_off_auto_collect()

    print('Отключен автоподбор шмоток')

    for is_global in range(2):
        is_global = bool(is_global)

        if is_global:
            server_id = get_global_server_id(server_id)
            print(f'ID сервера для глобал маркета {server_id}')

            open_global_market()
            open_sell_menu()
        else:
            go_to_sell_menu()

        if no_items_to_replace(is_global):
            print('Нет шмоток чтобы переставить')
        else:
            print('Есть шмотки чтобы переставить')

            x, y = get_equiped_item_cords()

            print(f'Координаты экипированной шмотки x: {x}, y: {y}')

            while not check_if_all_items_are_replaced():
                old_price = get_old_price()
                print(f'Старая цена {old_price}')

                if not take_off_item_from_sell(): #Проверка переполнен ли инвентарь
                    print('Инвентарь переполнен')
                    break

                take_item_to_sell(x, y)

                item_name = get_item_name()
                print(f'Имя предмета {item_name}')

                item_sharp = get_item_sharp(item_name)
                print(f'Заточка предмета {item_sharp}')

                item_id = get_item_id(item_name)
                print(f'ID предмета {item_id}')

                minimal_price = get_minimal_price_for_item(server_id, item_id, item_sharp)

                print(f'Минимальная цена на сервере {minimal_price}')

                new_price = calculate_price(old_price, minimal_price, is_global)

                if new_price is False:
                    print('Красная шмотка стоит меньше нужного')
                    cancel_selling_item()
                    continue

                print(f'Цена которую нужно установить {new_price}')

                while get_set_price() != new_price:
                    set_price(new_price)

                    if get_set_price() != new_price:
                        erase_price()

                sell_item()

        collect_income()
    exit_from_market()

    turn_on_auto_collect(True)
    exit_from_settings()






