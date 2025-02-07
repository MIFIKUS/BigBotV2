from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


def load_imgs() -> dict:
    path = 'gui\\imgs'

    diamond = QPixmap(f'{path}\\diamond.svg')
    diamond = diamond.scaled(20, 30, Qt.AspectRatioMode.KeepAspectRatio)

    adena = QPixmap(f'{path}\\adena.svg')
    adena = adena.scaled(20, 40, Qt.AspectRatioMode.KeepAspectRatio)

    return {'diamond': diamond, 'adena': adena}
