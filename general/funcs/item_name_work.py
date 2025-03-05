from bots.alchemy.extensions import items_grade
from general.lists.all_items_ids import ALL_ITEMS
from string import digits


def get_item_id(item_name: str) -> str or bool:
    """Получает ID предмета, если не удалось, возвращает False"""
    item_name = item_name.replace('+', '').replace(' ', '').lower()

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


def is_item_accessory(item_name: str) -> bool:
    """Проверка на то, что предмет является бижей"""
    item_name = item_name.lower()

    ACCESSORY_NAMES = ('кольцо', 'ожерелье', 'пояс', 'серьга')

    for i in ACCESSORY_NAMES:
        if i in item_name:
            return True
    return False


def is_item_piece(item_name: str) -> bool:
    """Проверка на то, что предмет является кусочком"""
    item_name = item_name.lower()

    PIECE_NAMES = ('авадон', 'зубе', 'молнии', 'кронвист')

    for i in PIECE_NAMES:
        if i in item_name:
            return True
    return False


def get_item_grade(item_name, color: str) -> str:
    """Получает грейд предмета"""
    sharp = get_item_sharp(item_name)
    is_accessory = is_item_accessory(item_name)
    is_piece = is_item_piece(item_name)

    if color == 'blue':
        if not is_accessory and not is_piece:
            if sharp != 0:
                return items_grade.BLUE_SHARP
            else:
                return items_grade.BLUE

        if is_piece:
            if sharp == 8:
                return items_grade.PIECE_PLUS_8
            else:
                return items_grade.PIECE_NOT_PLUS_8

        match sharp:
            case 0:
                return items_grade.ACCESSORY_PLUS_0
            case 1:
                return items_grade.ACCESSORY_PLUS_1
            case 2:
                return items_grade.ACCESSORY_PLUS_2
            case 3:
                return items_grade.ACCESSORY_PLUS_3
            case 4:
                return items_grade.ACCESSORY_PLUS_4
            case 5:
                return items_grade.ACCESSORY_PLUS_5

    if color == 'green':
        if sharp != 0:
            return items_grade.GREEN_SHARP
        else:
            return items_grade.GREEN

    if color == 'red':
        if sharp != 0:
            return items_grade.RED_SHARP
        else:
            return items_grade.RED


def transform_item_name_to_market(item_name: str) -> str:
    """Переводит название предмета в вид который подойдет на аукционе"""
    item_name_new = []

    for i in item_name.split(' '):
        item_name_new.append(i.capitalize())

    return ''.join(item_name_new)
