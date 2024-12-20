from l2m_ui_funcs.main_screen import open_menu, open_settings
from l2m_ui_funcs.actions_in_menus.settings.settings import open_information_menu, exit_from_settings

from main_funcs import image
from general.funcs import string_work

from general.lists.servers import ALL_SERVERS_IDS

from difflib import SequenceMatcher


def get_server_id() -> str or bool:
    """Заходит в настройки и возвращает id сервера"""
    def _get_server_name() -> str:
        """Делает скриншот названия сервера, и возвращает эту строку"""
        image_name = 'general\\imgs\\screenshots\\server_name.png'
        area_of_screenshot = (1200, 450, 1425, 485)

        image.take_screenshot(image_name, area_of_screenshot)

        item_name = image.image_to_string(image_name, False)
        item_name = string_work.delete_junk_symbols(item_name)

        return item_name

    open_menu()
    open_settings()
    open_information_menu()

    server_name = _get_server_name().lower()

    for server, server_id in ALL_SERVERS_IDS.items():
        server = server.replace(' ', '').lower()
        if server == server_name:
            return server_id
    return False
