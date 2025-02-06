from version import VERSION

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout,
    QScrollArea, QSizePolicy, QSpacerItem, QPushButton
)
from PySide6.QtCore import Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"BigBot v.{VERSION}")
        self.setFixedSize(1280, 720)

        self.init_menu()
        self.bot_menu()

    def init_menu(self):
        """Создает верхнюю панель меню"""
        menubar = self.menuBar()

        file_menu = menubar.addMenu("Боты")
        exit_action = QAction("Открыть папку логов", self)
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Настройки")
        about_action = QAction("Расписание", self)
        help_menu.addAction(about_action)
        about_action = QAction("Обновить", self)
        help_menu.addAction(about_action)

    def bot_menu(self):
        """Создаёт область с прокруткой и центрирует её только по вертикали"""
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # Верхний пустой спейсер (создаёт отступ сверху)
        main_layout.addItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Область с прокруткой
        scroll_area = QScrollArea(self)
        scroll_area.setFixedSize(int(self.width() * 0.75), int(self.height() * 0.9))  # 80% высоты, 80% ширины
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setWidgetResizable(True)

        # Контейнер для содержимого
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        # Добавляем элементы в макет
        for i in ['Алхимия', 'Перстановка', 'Сборщик', '123']:
            label = self._create_bot_widget(self.scroll_layout, i, '')
            self.scroll_layout.addWidget(label)

        self.scroll_widget.setLayout(self.scroll_layout)
        scroll_area.setWidget(self.scroll_widget)

        # Добавляем ScrollArea в главный макет (без выравнивания по горизонтали)
        main_layout.addWidget(scroll_area, alignment=Qt.AlignmentFlag.AlignRight)

        # Нижний пустой спейсер (создаёт отступ снизу)
        main_layout.addItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Устанавливаем главный макет
        self.setCentralWidget(central_widget)

    def _create_bot_widget(self, layout: QVBoxLayout, bot_name: str, bot_img_path: str) -> QWidget:
        """Макет для создания виджета ботов"""
        bot_widget = QWidget(self)

        bot_widget.setMinimumHeight(100)  # Минимальная высота 100 пикселей
        bot_widget.setMaximumHeight(100)

        # Создаём макет
        bot_layout = QVBoxLayout(bot_widget)

        bot_label = QLabel(bot_name)
        bot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bot_label.setFixedHeight(self.height() * 0.05)

        start_button = QPushButton('Старт')
        start_button.setFixedHeight(self.height() * 0.05)

        bot_layout.addWidget(bot_label)
        bot_layout.addWidget(start_button)

        bot_widget.setStyleSheet("""
        QWidget {
            border: 2px solid #666;  /* Черная рамка */
            border-radius: 5px;        /* Скругленные углы */}
        QLabel, QPushButton{
            border: none;
            cursor: pointer;
        }    
            """)
        bot_widget.setLayout(bot_layout)
        bot_widget.setAlignment
        return bot_widget


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())