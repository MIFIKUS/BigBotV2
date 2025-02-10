from bots.autosell.config import DIFFERENCE_IN_PRICE, MINIMAL_PRICE_FOR_RED


def calculate_price(old_price: int, new_price: int, is_global: bool) -> int or bool:
    """Возвращает или старую цену, или новую - 1, в зависимости от разницы в процентах"""
    if old_price == 0:
        return new_price - 1
    difference = abs(new_price - old_price) / old_price * 100

    if is_global:
        if new_price < MINIMAL_PRICE_FOR_RED:
            return False

    if difference > DIFFERENCE_IN_PRICE:
        return old_price

    price = new_price - 1

    if price < 10:
        return 10

    return price
