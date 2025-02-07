from version import VERSION

from PySide6.QtGui import QAction, QFontDatabase, QFont
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout,
    QScrollArea, QSizePolicy, QSpacerItem, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt

import sys
app = QApplication(sys.argv)
app.setStyle('Fusion')

font_id = QFontDatabase.addApplicationFont("fonts\\sf\\SF-Pro-Display-Black.otf")
font_families = QFontDatabase.applicationFontFamilies(font_id)

if font_families:
    font_name = font_families[0]

font_name = font_families[0]  # Получаем имя шрифта
normal_font = QFont(font_name, 12)  # Обычный шрифт
bold_font = QFont(font_name, 12, QFont.Bold)  # Жирный шрифт
italic_font = QFont(font_name, 12)  # Создаем обычный шрифт и затем устанавливаем курсив

# Установка курсивного стиля
italic_font.setStyle(QFont.StyleItalic)

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
        for i in ['Алхимия', 'Перстановка', 'Сборщик', '123', '23']:
            label = self._create_bot_widget(self.scroll_layout, i, '')
            self.scroll_layout.addWidget(label)

        for i in range(50):
            label = self._create_account_widget(self.scroll_layout, str(i), '123123')
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

    def _create_bot_widget(self, layout: QVBoxLayout, bot_name: str, bot_img_path: str) -> QWidget:
        """Макет для создания виджета ботов"""
        bot_widget = QWidget(self)

        bot_widget.setMinimumHeight(150)  # Минимальная высота 100 пикселей
        bot_widget.setMaximumHeight(150)

        # Создаём макет
        bot_layout = QVBoxLayout(bot_widget)

        bot_label = QLabel(bot_name)
        bot_label.setFont(italic_font)
        bot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        bot_label.setFixedHeight(self.height() * 0.05)

        start_button = QPushButton('Старт')
        start_button.setCursor(Qt.PointingHandCursor)

        start_button.setFixedHeight(self.height() * 0.1)

        bot_layout.addWidget(bot_label)
        bot_layout.addWidget(start_button)

        bot_widget.setStyleSheet("""
            QWidget {
                   border: none;  /* Серый цвет рамки */
                   border-radius: 5px;      /* Скругленные углы */
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
                background-color: #822f61;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #6b2750;
                font-size: 16px;
            }
            
            QLabel {
                color: white;
                background: none;
                font-size: 24px;
            }
            """)
        bot_widget.setLayout(bot_layout)
        return bot_widget

    def _create_account_widget(self, layout: QVBoxLayout, acc_name: str, pid: str) -> QWidget:
        acc_widget = QWidget()

        acc_widget.setMinimumHeight(100)  # Минимальная высота 100 пикселей
        acc_widget.setMaximumHeight(100)

        # Создаём горизонтальный макет
        acc_layout = QHBoxLayout(acc_widget)

        acc_label = QLabel(f"{acc_name}({pid})")

        acc_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft)  # Выравнивание по левому краю и по центру по вертикали
          # Выравнивание по правому краю и по центру по вертикали

        acc_label.setFixedHeight(100)  # Устанавливаем фиксированную высоту


        acc_layout.addWidget(acc_label)


        acc_widget.setStyleSheet("""
            QWidget {
                border: none;  /* Серый цвет рамки */
                border-radius: 5px;      /* Скругленные углы */
                background-color: #32383b;
            }
            QLabel {
                color: white;
                background: none;
                font-size: 24px;
            }
        """)

        acc_widget.setLayout(acc_layout)
        return acc_widget



window = MainWindow()
window.show()
sys.exit(app.exec())