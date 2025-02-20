from ahk import AHK
from general.logs.logger import logger

ahk = AHK()


def y():
    """Нажимает Y"""
    logger.debug('Нажата кнопка Y')
    while True:
        try:
            ahk.key_press('y')
            break
        except:
            pass


def esc():
    """Нажимает esc"""
    logger.debug('Нажат Esc')
    while True:
        try:
            ahk.key_press('esc')
            break
        except:
            pass
