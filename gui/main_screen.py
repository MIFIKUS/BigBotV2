from version import VERSION

from general.git.update import get_last_version, update_project

from gui.fonts.fonts import load_fonts
from gui.imgs.imgs import load_imgs

from gui.extensions.numbers import custom_number

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout,
    QScrollArea, QSizePolicy, QSpacerItem, QPushButton, QHBoxLayout, QProgressBar, QGridLayout
)
from PySide6.QtCore import Qt

from bots.autosell import autosell_bot
from bots.sbor import sbor_bot


import sys
import random

app = QApplication(sys.argv)
app.setStyle('Fusion')


fonts = load_fonts()
imgs = load_imgs()

GIT_VERSION = get_last_version()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        if VERSION == GIT_VERSION:
            self.setWindowTitle(f"BigBot v.{VERSION}")
        else:
            self.setWindowTitle(f"BigBot v.{VERSION} УСТАРЕЛО")

        self.setFixedSize(1280, 720)

        self.setWindowIcon(QIcon("gui\\imgs\\logo.jpg"))

        self.init_menu()
        self.bot_menu()

    def init_menu(self):
        """Создает верхнюю панель меню"""
        menubar = self.menuBar()

        menubar.setStyleSheet("""
            background-color: black;
        """)

        file_menu = menubar.addMenu("Боты")
        exit_action = QAction("Открыть папку логов", self)
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Настройки")
        about_action = QAction("Расписание", self)
        help_menu.addAction(about_action)
        about_action = QAction("Обновить", self)
        help_menu.addAction(about_action)

        self.setStyleSheet("""
             QWidget {background-color:#1f1f1f;}
            """)

    def bot_menu(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        # Верхний пустой спейсер (создаёт отступ сверху)
        main_layout.addItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Горизонтальный макет для scroll_area и accounts_scroll_area
        h_layout = QHBoxLayout()

        # Область с прокруткой для аккаунтов
        accounts_scroll_area = QScrollArea(self)
        accounts_scroll_area.setFixedSize(int(self.width() * 0.24), int(self.height() * 0.9))  # 90% высоты, 25% ширины
        accounts_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Скрыть вертикальную полосу прокрутки
        accounts_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Скрыть горизонтальную полосу прокрутки
        accounts_scroll_area.setWidgetResizable(True)

        accounts_scroll_area.setStyleSheet("""
            QScrollArea{
                border: none;
            }
        """)

        # Область с прокруткой для основного контента
        scroll_area = QScrollArea(self)
        scroll_area.setFixedSize(int(self.width() * 0.74), int(self.height() * 0.9))  # 90% высоты, 75% ширины
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Скрыть вертикальную полосу прокрутки
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Скрыть горизонтальную полосу прокрутки
        scroll_area.setWidgetResizable(True)

        scroll_area.setStyleSheet("""
            QScrollArea{
                border: none;
            }
        """)

        # Контейнер для содержимого
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.accounts_scroll_widget = QWidget()
        self.accounts_scroll_layout = QVBoxLayout(self.accounts_scroll_widget)
        self.accounts_scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Добавляем элементы в макет
        for i in ['Перстановка', 'Сборщик']:
            match i:
                case 'Перстановка':
                    label = self._create_autosell_widget()
                case 'Сборщик':
                    label = self._create_sbor_widget()

            self.scroll_layout.addWidget(label)

        for i in range(50):
            label = self._create_account_widget(self.scroll_layout, str(i), random.randint(0, 10000), 10000, random.randint(1, 1000), random.randint(10_000, 100_000_000))
            self.accounts_scroll_layout.addWidget(label)

        self.scroll_widget.setLayout(self.scroll_layout)
        self.accounts_scroll_widget.setLayout(self.accounts_scroll_layout)
        scroll_area.setWidget(self.scroll_widget)
        accounts_scroll_area.setWidget(self.accounts_scroll_widget)

        # Добавляем ScrollArea в горизонтальный макет в измененном порядке
        h_layout.addWidget(accounts_scroll_area)  # Сначала добавляем accounts_scroll_area
        h_layout.addWidget(scroll_area)           # Затем добавляем scroll_area

        # Добавляем горизонтальный макет в главный макет
        main_layout.addLayout(h_layout)

        # Нижний пустой спейсер (создаёт отступ снизу)
        main_layout.addItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Устанавливаем главный макет
        self.setCentralWidget(central_widget)

    def _create_autosell_widget(self):
        return self._create_bot_widget('Перестановка', autosell_bot.start)

    def _create_sbor_widget(self):
        return self._create_bot_widget('Сборщик', sbor_bot.start)


    def _create_bot_widget(self, bot_name: str, bot_func) -> QWidget:
        """Макет для создания виджета ботов"""
        bot_widget = QWidget(self)
        bot_widget.setMinimumHeight(100)  # Минимальная высота 150 пикселей
        bot_widget.setMaximumHeight(100)

        # Создаём горизонтальный макет
        bot_layout = QHBoxLayout(bot_widget)

        bot_label = QLabel(bot_name)
        bot_label.setFont(fonts['regular'])
        bot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        start_button = QPushButton('Старт')
        start_button.setFont(fonts['regular'])
        start_button.setCursor(Qt.PointingHandCursor)

        start_button.clicked.connect(bot_func)

        # Устанавливаем фиксированную высоту для кнопки и метки
        bot_label.setFixedHeight(self.height() * 0.1)
        start_button.setFixedHeight(self.height() * 0.1)
        start_button.setFixedWidth(self.width()* 0.2)

        # Добавляем виджеты в макет
        bot_layout.addWidget(bot_label)
        bot_layout.addWidget(start_button)

        # Настройка стилей
        bot_widget.setStyleSheet("""
            QWidget {
                border: none;
                border-radius: 5px;
                background-color: #32383b;
            }
            QWidget:hover {
                background-color: #232729;
            }
            QLabel, QPushButton {
                border: none;
                cursor: pointer;
            }
            QPushButton {
                border-radius: 10px;
                background-color: #822f61;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #6b2750;
            }
            QLabel {
                color: white;
                background: none;
                font-size: 24px;
            }
        """)

        bot_widget.setLayout(bot_layout)
        return bot_widget

    def _create_account_widget(self, layout: QVBoxLayout, acc_name: str, current_hp: int, max_hp: int, diamonds: int, adena: int) -> QWidget:

        diamonds = custom_number(diamonds)
        adena = custom_number(adena)

        acc_widget = QWidget()
        acc_widget.setCursor(Qt.CursorShape.PointingHandCursor)

        # Устанавливаем фиксированную высоту
        acc_widget.setMinimumHeight(100)  # Минимальная высота 100 пикселей
        acc_widget.setMaximumHeight(100)

        # Создаём сеточный макет
        acc_layout = QGridLayout(acc_widget)

        # Метка с именем аккаунта
        acc_label = QLabel(f"{acc_name}")
        acc_label.setFont(fonts['ultralight'])
        acc_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)  # Выравнивание по левому краю и по центру по вертикали
        acc_label.setFixedHeight(30)  # Устанавливаем фиксированную высоту

        # Прогресс-бар для HP
        hp_bar = QProgressBar()
        hp_bar.setMinimum(0)
        hp_bar.setMaximum(max_hp)
        hp_bar.setValue(current_hp)
        hp_bar.setFixedHeight(30)
        hp_bar.setMaximumWidth(150)
        hp_bar.setFormat("%v/%m")
        hp_bar.setFont(fonts['regular'])

        # Изображение алмаза
        diamond_img = QLabel()
        diamond_img.setPixmap(imgs['diamond'])
        diamond_img.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        diamond_img.setFixedHeight(30)

        diamond_img.setAlignment(
            Qt.AlignmentFlag.AlignRight| Qt.AlignmentFlag.AlignVCenter)  # Выравнивание по правому краю и по верхнему краю

        adena_img = QLabel()
        adena_img.setPixmap(imgs['adena'])
        adena_img.setAlignment(Qt.AlignmentFlag.AlignRight| Qt.AlignmentFlag.AlignVCenter)

        adena_img.setFixedHeight(30)

        diamonds_label = QLabel(diamonds)
        diamonds_label.setFixedHeight(30)
        diamonds_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        adena_label = QLabel(adena)
        adena_label.setFixedHeight(30)
        adena_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # Добавляем виджеты в макет
        acc_layout.addWidget(acc_label, 0, 0)  # Первая строка, первый столбец
        acc_layout.addWidget(hp_bar, 1, 0)  # Вторая строка, первый столбец

        acc_layout.addWidget(diamond_img, 0, 1)  # Первая и вторая строки, второй столбец (занимает две строки)
        acc_layout.addWidget(diamonds_label, 0,2)

        acc_layout.addWidget(adena_img, 1, 1)
        acc_layout.addWidget(adena_label, 1, 2)

        # Настройка выравнивания
        acc_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        # Стилизация
        acc_widget.setStyleSheet("""
            QWidget {
                border: none;  /* Серый цвет рамки */
                border-radius: 5px;      /* Скругленные углы */
                background-color: #32383b;
            }
            QWidget:hover {
                background-color: #232729;
            }
            QLabel {
                color: white;
                background: none;
                font-size: 18px;
            }
            QProgressBar {
                background-color: #216e3a;
                text-align: center;
                border-radius: 10px;
                font-size: 11px;
                color: black;
            }
            QProgressBar::chunk {
                background-color: #31b55d;
                border-radius: 10px;
                text-align: center;
            }
        """)

        acc_widget.setLayout(acc_layout)
        return acc_widget

    def _update(self):
        """Обновляет проект"""


window = MainWindow()
window.show()
sys.exit(app.exec())