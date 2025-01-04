from general.funcs.checks import check


def window_locked() -> bool:
    """Проверка заблокировано ли окно"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\screen_is_locked.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_screen_locked.png'

    return check(screenshot_name, template_name, (400, 200, 1250, 800))


def map_opened() -> bool:
    """Проверка на то, что карта открыта"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\map_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_map_opened.png'

    return check(screenshot_name, template_name, (1605, 70, 1735, 120))


def sellers_menu_opened() -> bool:
    """Проверка на то, что меню торговцев открыто"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\sellers_menu_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_sellers_menu_opened.png'

    return check(screenshot_name, template_name, (65, 160, 100, 520))


def menu_opened() -> bool:
    """Проверка на то, открыто ли меню"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\menu_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_menu_opened.png'

    return check(screenshot_name, template_name, (1750, 60, 1800, 115))


def adena_market_opened() -> bool:
    """Проверка на то, открыт ли адена шоп"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\adena_market_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_adena_shop_opened.png'

    return check(screenshot_name, template_name, (1455, 70, 1745, 115))


def inventory_opened() -> bool:
    """Проверка на то, открыт ли инвентарь"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\inventory_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_inventory_opened.png'

    return check(screenshot_name, template_name, (1330, 170, 1415, 205))


def classes_opened() -> bool:
    """Проверка на то, открыто ли меню классов"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\classes_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_classes_opened.png'

    return check(screenshot_name, template_name, (1610, 65, 1740, 120))


def aghations_opened() -> bool:
    """Проверка на то, открыто ли меню классов"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\aghations_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_aghations_opened.png'

    return check(screenshot_name, template_name, (1515, 70, 1740, 125))


def market_opened() -> bool:
    """Проверка на то, открыт ли аукцион"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\market_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_market_opened.png'

    return check(screenshot_name, template_name, (1560, 65, 1745, 120))


def clan_menu_opened() -> bool:
    """Проверка на то, что меню клана открыто"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\clan_menu_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_clan_menu_opened.png'

    return check(screenshot_name, template_name, (1625, 70, 1735, 110))


def bonuses_opened() -> bool:
    """Проверка на то, что меню бонусов открыто"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\bonuses_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_bonuses_opened.png'

    return check(screenshot_name, template_name, (1250, 65, 1735, 120))


def messages_opened() -> bool:
    """Проверка на то, что меню сообщений открыто"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\messages_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_messages_opened.png'

    return check(screenshot_name, template_name, (1595, 70, 1735, 110))


def battle_pass_opened() -> bool:
    """Проверка на то, что меню сезонного пропуска открыто"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\battle_pass_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_battle_pass_opened.png'

    return check(screenshot_name, template_name, (1300, 65, 1740, 125))


def settings_opened() -> bool:
    """Проверка на то, открыто ли меню настроек"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\settings_opened.png'
    screenshot_name = 'l2m_ui_funcs\\imgs\\screenshots\\is_settings_opened.png'

    return check(screenshot_name, template_name, (1485, 65, 1740, 130))
