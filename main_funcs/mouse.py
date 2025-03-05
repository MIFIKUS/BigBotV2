from ahk import AHK
from general.logs.logger import logger

ahk = AHK()


def move(x: int, y: int, relative=False):
    """Двигает мышку по координатам"""
    logger.debug(f'Перемещение курсора x: {x} y: {y}')
    while True:
        try:
            ahk.mouse_move(x, y, speed=0, relative=relative)
            break
        except Exception:
            pass


def click():
    """Делает клик мышкой"""
    logger.debug('Делает клик')
    while True:
        try:
            ahk.click()
            break
        except Exception:
            pass


def move_and_click(x, y):
    """Двигает мышку и делает клик"""
    move(x, y)
    click()


def drag(x: int, y: int, relative: bool):
    """Дергает мышку в координаты"""
    logger.debug(f'Дергает мышку x: {x} y: {y} relative: {relative}')
    while True:
        try:
            ahk.mouse_drag(x, y, relative=relative)
            break
        except:
            pass


def wheel_down(amount_of_spins: int):
    """Вращает колесико мышки вниз"""
    logger.debug(f'Вращение колесика вниз amount_of_spins: {amount_of_spins}')
    while True:
        try:
            for _ in  range(amount_of_spins):
                ahk.wheel_down()
            break
        except:
            pass


def wheel_up(amount_of_spins: int):
    """Вращает колесико мышки вверх"""
    logger.debug(f'Вращение колесика вверх amount_of_spins: {amount_of_spins}')
    while True:
        try:
            for _ in range(amount_of_spins):
                ahk.wheel_up()
            break
        except:
            pass


def press_down():
    """Зажимает ЛКМ"""
    while True:
        try:
            ahk.click(direction='D')
            break
        except:
            pass


def press_up():
    """Отпускает ЛКМ"""
    while True:
        try:
            ahk.click(direction='U')
            break
        except:
            pass
