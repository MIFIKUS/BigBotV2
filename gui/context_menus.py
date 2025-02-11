from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QPoint


def booster_context_menu(parent: QWidget, pos: QPoint):
    menu = QMenu(parent)  # Передаём родителя, чтобы меню не закрывалось сразу

    fuses = QAction('Фьюзы', parent)
    fuses.triggered.connect(lambda: print("Выбраны Фьюзы"))

    menu.addAction(fuses)

    menu.exec(parent.mapToGlobal(pos))
