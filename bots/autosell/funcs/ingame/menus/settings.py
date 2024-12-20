from l2m_ui_funcs.main_screen import open_menu, open_market, open_settings
from l2m_ui_funcs.actions_in_menus.settings import settings


def turn_off_auto_collect():
    """Заходит в настройки и выключает автоподбор предметов"""
    open_menu()
    open_settings()

    settings.open_attack_menu()
    settings.open_collect_menu()

    settings.turn_off_auto_collect()

    settings.exit_from_settings()
