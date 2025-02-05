from version import VERSION
from PySide6 import QtWidgets  # Импорт модуля QtWidgets из библиотеки PySide6
import sys


app = QtWidgets.QApplication(sys.argv)


def set_window() -> QtWidgets.QWidget:
    """Задает параметры главного окна"""
    window = QtWidgets.QWidget()

    window.setWindowTitle(f"BigBot {VERSION}")
    window.setFixedSize(1280, 720)

    return window

window = set_window()

window.show()

# Запуск основного цикла обработки событий приложения
sys.exit(app.exec())