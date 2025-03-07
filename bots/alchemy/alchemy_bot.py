from bots.alchemy.rolls import all_rolls
from bots.alchemy.funcs.inventory.items import set_rolls_items
from bots.alchemy.funcs.roll.roll import make_roll

from general.funcs.acc_info import get_server_id
from general.memory.process import get_process_handle

from l2m_ui_funcs.main_screen import open_alchemy, open_menu, open_market

from l2m_ui_funcs.actions_in_menus.alchemy.alchemy import repeat_forecast, reset_forecast_items, start_roll, exit_from_alchemy
from l2m_ui_funcs.actions_in_menus.market.market import sell_last_item, open_sell_menu, exit_from_market, get_amount_of_slots
from l2m_ui_funcs.actions_in_menus.settings.settings import exit_from_settings


def roll(roll_info: dict):
    """Тут происхоидт весь процесс ролла"""
    slot_to_check = roll_info['slot_to_check']
    items = roll_info['items']
    min_avg = roll_info['min_avg']
    red_slots = roll_info['red_slots']
    roll_items = roll_info['roll_items']
    colors = roll_info['colors']

    server_id = get_server_id()
    exit_from_settings()

    process_handle = get_process_handle()

    open_menu()
    open_market()

    amount_of_free_slots = get_amount_of_slots()
    exit_from_market()

    for _ in range(amount_of_free_slots):
        open_menu()
        open_alchemy()

        reset_forecast_items()

        set_rolls_items(roll_items, server_id)
        repeat_forecast()

        make_roll(process_handle, server_id, colors, [slot_to_check], items, 'memory', True, min_avg)
        start_roll()

        exit_from_alchemy()
        open_market()
        open_sell_menu()
        sell_last_item(server_id)
        exit_from_market()
