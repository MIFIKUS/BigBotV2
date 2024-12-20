from general.lists.all_items_ids import ALL_ITEMS
from string import digits


def get_item_id(item_name: str) -> str or bool:
    """Получает ID предмета, если не удалось, возвращает False"""
    item_name = item_name.replace('+', '').lower()

    item_name_fixed = ''

    for i in item_name:
        if i not in digits:
            item_name_fixed += i

    for item_id, name in ALL_ITEMS.items():
        name = name.replace(' ', '').lower()
        if name == item_name_fixed:
            return item_id
    else:
        return False


def get_item_sharp(item_name: str) -> int:
    """Получает заточку предмета"""

    item_name = item_name.replace('+', '')

    sharp = ''

    for i in item_name:
        if i in digits:
            sharp += i

    if not sharp:
        sharp = 0

    return int(sharp)

