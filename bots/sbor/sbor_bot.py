from l2m_ui_funcs.actions_in_menus.messages import messages
from l2m_ui_funcs.actions_in_menus.clan import clan
from l2m_ui_funcs.actions_in_menus.bonuses import bonuses
from l2m_ui_funcs.actions_in_menus.battle_pass import battle_pass
from l2m_ui_funcs.actions_in_menus.map import map
from l2m_ui_funcs.actions_in_menus.sellers import sellers
from l2m_ui_funcs.actions_in_menus.locations.locations import tp_to_last_location

from bots.sbor.funcs.ingame.menus import adena_market
from l2m_ui_funcs.main_screen import *

from main_funcs.windows import switch_windows

from general.logs.logger import logger

import time


def collect_adena_market():
    """Собирает все в адена шопе"""
    open_menu()
    open_adena_market()

    logger.info('Открыт адена шоп')

    adena_market.close_ad()
    logger.info('Закрыто объявление')

    adena_market.open_adena()
    logger.info('Открыта вкладка с покупкой за адену')

    for shop_num in range(4):
        adena_market.click_on_inner_shop(shop_num)
        logger.info(f'Открыт магазин #{shop_num+1}')
        adena_market.buy()

        if adena_market.nothing_to_buy():
            logger.info(f'Нечего покупать')
            adena_market.close_inner_shop()
        else:
            logger.info('Покупка')
            adena_market.confirm_buy()

    adena_market.exit_adena_shop()
    logger.info('Вышел из адена шопа')


def collect_messages():
    """Собирает бонусы из сообщений"""
    open_menu()
    open_messages()

    logger.info('Открыто меню сообщений')

    collected = messages.collect()
    logger.info('Нажата кнопка собрать')

    if collected:
        for _ in range(2):
            time.sleep(3)

            if messages.energy_collect_available():
                logger.info('Есть плашка с энергией')
                messages.decline_collect_energy()

    messages.exit_from_messages()
    logger.info('Вышел из меню сообщений')


def collect_clan():
    """Собирает бонусы в клане"""
    open_menu()
    open_clan()

    logger.info('Открыто меню клана')

    if not clan.character_in_clan():
        logger.info('Персонаж не состоит в клане')
        clan.exit_from_clan_menu()
        return

    clan.open_contribution_menu()

    logger.info('Открыто меню взносов')

    while not clan.no_more_contributions():
        clan.make_contribute()
        logger.info('Сделан взном')

    logger.info('Больше нет взносов')

    clan.close_contribution_menu()

    logger.info('Меню взносов закрыто')

    time.sleep(0.5)

    clan.get_reward()

    logger.info('Нажата кнопка получить награду')

    clan.exit_from_clan_menu()

    logger.info('Вышел из меню клана')


def collect_bonuses():
    """Собирает бонусы в меню бонусов"""
    open_menu()
    open_bonuses()

    logger.info('Открыто меню бонусов')

    for bonus_num in range(7):
        if bonuses.no_more_bonuses(bonus_num):
            logger.info('Больше нет бонусов')
            break

        bonuses.click_on_bonus(bonus_num)
        logger.info('Нажата кнопка получить бонус')

        if not bonuses.bonus_unused() or bonuses.bonus_unavailable() or bonuses.bonus_for_diamonds() or bonuses.bonus_for_compas():
            logger.info('Невозможно собрать бонус')
            continue

        if bonuses.get_bonus() is False:
            break

        logger.info('Бонус собран')

    bonuses.exit_from_bonuses()
    logger.info('Вышел из меню бонусов')


def collect_battle_pass():
    """Собирает все награды с Сезонного пропуска"""
    open_menu()
    open_battle_pass()
    logger.info('Зашел в меню батл пасса')

    for battle_pass_num in range(2):
        if not battle_pass.rewards_in_battle_pass_available(battle_pass_num):
            logger.info(f'Нечего собирать в БП №{battle_pass_num}')
            continue

        battle_pass.click_on_battle_pass(battle_pass_num)
        logger.info(f'Нажал на батл пасс №{battle_pass_num}')

        for sub_battle_pass_num in range(2):
            if not battle_pass.rewards_in_sub_battle_pass_available(sub_battle_pass_num):
                logger.info(f'Нечего собирать в саб батл пассе №{sub_battle_pass_num}')
                continue

            battle_pass.click_on_sub_battle_pass(sub_battle_pass_num)
            logger.info(f'Нажал на саб батл пасс №{sub_battle_pass_num}')

            fail_counter = 0
            while battle_pass.get_subreward_available():
                logger.info('Есть награда которую можно собрать')
                battle_pass.get_sub_battle_pass_reward()
                if fail_counter > 100:
                    break
                fail_counter += 1
                time.sleep(0.3)

        battle_pass.get_battle_pass_reward()
        logger.info(f'Собрал общую награду БП #{battle_pass_num}')

    battle_pass.exit_from_battle_pass()
    logger.info('Вышел из меню БП')


def collect_sellers():
    """Проходит по торговцам"""
    grocer_pos = 0
    sklad_pos = 2
    buyer_pos = 4

    logger.info('Попытка телепортироваться в город')
    map.teleport_to_town()

    open_sellers_menu()
    logger.info('Открыл меню торговцев')

    amount_of_events = sellers.get_amount_of_events()
    logger.info(f'Количество ивентов: {amount_of_events}')

    for event_pos in range(amount_of_events):
        logger.info(f'Собирает ивент #{event_pos}')
        sellers.collect_event(event_pos)

    grocer_pos += amount_of_events
    sklad_pos += amount_of_events
    buyer_pos += amount_of_events

    logger.debug(f'''grocer_pos: {grocer_pos} sklad_pos: {sklad_pos} buyer_pos: {buyer_pos}''')

    logger.info('Собирает бакалейщика')
    sellers.collect_grocer(grocer_pos)

    logger.info('Собирает склад')
    sellers.collect_sklad(sklad_pos)

    if amount_of_events == 2:
        logger.info('Количество ивентов = 2, прокручивает вниз')
        mouse.move(190, 315)
        mouse.wheel_down(3)

    logger.info('Собирает скупщика')
    sellers.collect_buyer(buyer_pos)

    if amount_of_events == 2:
        logger.info('Прокручивает вверх')
        mouse.move(190, 315)
        mouse.wheel_up(3)

    sellers.exit_sellers_menu()
    logger.info('Закрывает меню торговцев')


def run():
    """Запускает бота"""
    collect_adena_market()
    collect_messages()
    collect_clan()
    collect_bonuses()
    collect_battle_pass()
    collect_sellers()
    tp_to_last_location()


def start():
    switch_windows(run)