from bots.autosell.config import DIFFERENCE_IN_PRICE, MINIMAL_PRICE_FOR_RED
from general.logs.logger import logger


def calculate_price(old_price: int, new_price: int, is_global: bool) -> int or bool:
    """Возвращает или старую цену, или новую - 1, в зависимости от разницы в процентах"""
    logger.debug(f'Вычисление новой цены для шмотки')
    logger.debug(f'old_price: {old_price} new_price: {new_price} is_global: {is_global}')

    if new_price < 10:
        logger.debug('Новая цена меньше 10')
        return old_price if old_price == 10 else old_price - 1

    difference = abs(new_price - old_price) / old_price * 100
    logger.debug(f'Разница в цене {difference}')

    if is_global:
        if new_price < MINIMAL_PRICE_FOR_RED:
            logger.debug(f'Новая цена меньше чем минимальная цена для краснухи new_price: {new_price} MINIMAL_PRICE_FOR_RED: {MINIMAL_PRICE_FOR_RED}')
            return False

    if difference > DIFFERENCE_IN_PRICE:
        logger.debug(f'Разница в цене больше чем максимально допустимая Разница: {difference} Максимальная разница: {DIFFERENCE_IN_PRICE}')
        return old_price

    price = new_price - 1
    logger.debug(f'Цена: {price}')

    if price < 10:
        logger.debug('Цена меньше 10, возвращает 10')
        return 10

    return price
