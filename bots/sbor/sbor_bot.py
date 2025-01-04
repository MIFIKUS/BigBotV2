from l2m_ui_funcs.actions_in_menus.messages import messages
from l2m_ui_funcs.actions_in_menus.clan import clan
from l2m_ui_funcs.actions_in_menus.bonuses import bonuses
from l2m_ui_funcs.actions_in_menus.battle_pass import battle_pass
from l2m_ui_funcs.actions_in_menus.map import map
from l2m_ui_funcs.actions_in_menus.sellers import sellers

from bots.sbor.funcs.ingame.menus import adena_market
from l2m_ui_funcs.main_screen import *

import time


def collect_adena_market():
    """Собирает все в адена шопе"""
    open_menu()
    open_adena_market()

    adena_market.close_ad()

    adena_market.open_adena()

    for shop_num in range(4):
        adena_market.click_on_inner_shop(shop_num)
        adena_market.buy()
        if adena_market.nothing_to_buy():
            adena_market.close_inner_shop()
        else:
            adena_market.confirm_buy()

    adena_market.exit_adena_shop()


def collect_messages():
    """Собирает бонусы из сообщений"""
    open_menu()
    open_messages()

    messages.collect()
    time.sleep(1.5)

    if messages.energy_collect_available():
        messages.decline_collect_energy()

    messages.exit_from_messages()


def collect_clan():
    """Собирает бонусы в клане"""
    open_menu()
    open_clan()

    if not clan.character_in_clan():
        clan.exit_from_clan_menu()
        return

    clan.open_contribution_menu()

    while not clan.no_more_contributions():
        clan.make_contribute()
    clan.close_contribution_menu()

    time.sleep(0.5)

    clan.get_reward()

    clan.exit_from_clan_menu()


def collect_bonuses():
    """Собирает бонусы в меню бонусов"""
    open_menu()
    open_bonuses()

    for bonus_num in range(7):
        if bonuses.no_more_bonuses(bonus_num):
            break

        bonuses.click_on_bonus(bonus_num)

        if not bonuses.bonus_unused() or bonuses.bonus_unavailable() or bonuses.bonus_for_diamonds() or bonuses.bonus_for_compas():
            continue

        bonuses.get_bonus()

    bonuses.exit_from_bonuses()


def collect_battle_pass():
    """Собирает все награды с Сезонного пропуска"""
    open_menu()
    open_battle_pass()

    for battle_pass_num in range(2):
        if not battle_pass.rewards_in_battle_pass_available(battle_pass_num):
            continue

        battle_pass.click_on_battle_pass(battle_pass_num)

        for sub_battle_pass_num in range(2):
            if not battle_pass.rewards_in_sub_battle_pass_available(sub_battle_pass_num):
                continue
            battle_pass.click_on_sub_battle_pass(sub_battle_pass_num)

            fail_counter = 0
            while battle_pass.get_subreward_available():
                battle_pass.get_sub_battle_pass_reward()
                if fail_counter > 100:
                    break
                fail_counter += 1
                time.sleep(0.1)

        battle_pass.get_battle_pass_reward()

    battle_pass.exit_from_battle_pass()


def collect_sellers():
    """Проходит по торговцам"""
    grocer_pos = 0
    sklad_pos = 2
    buyer_pos = 3

    map.teleport_to_town()

    open_sellers_menu()

    amount_of_events = sellers.get_amount_of_events()

    for event_pos in range(amount_of_events):
        sellers.collect_event(event_pos)

    grocer_pos += amount_of_events
    sklad_pos += amount_of_events
    buyer_pos += amount_of_events

    sellers.collect_grocer(grocer_pos)
    sellers.collect_sklad(sklad_pos)

    if amount_of_events == 2:
        mouse.move(190, 315)
        mouse.wheel_down(3)

    sellers.collect_buyer(buyer_pos)

    if amount_of_events == 2:
        mouse.move(190, 315)
        mouse.wheel_up(3)

    sellers.exit_sellers_menu()


def run():
    """Запускает бота"""
    collect_adena_market()
    collect_messages()
    collect_clan()
    collect_bonuses()
    collect_battle_pass()
    collect_sellers()


