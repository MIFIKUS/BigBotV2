from PySide6.QtWidgets import QPushButton, QDialog, QVBoxLayout, QLabel, QWidget, QScrollArea, QHBoxLayout
from PySide6.QtCore import Qt

from gui.fonts.fonts import load_fonts

from general.git.update import update_project


class UpdateComplete(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Обновление')
        self.setFixedSize(400, 100)
        fonts = load_fonts()

        label = QLabel('Обновление завершено, перезагрузите бота', alignment=Qt.AlignmentFlag.AlignCenter)
        label.setFont(fonts['regular'])

        label.setStyleSheet("""
            font-size: 16px;
        """)

        main_layout = QVBoxLayout()

        main_layout.addWidget(label)

        self.setLayout(main_layout)


class UpdateDialog(QDialog):
    def __init__(self, update_comments: list):
        super().__init__()
        self.setWindowTitle("Обновление")
        self.setFixedSize(500, 300)
        fonts = load_fonts()
        main_layout = QVBoxLayout()

        # Создаём контейнер для меток
        scroll_container = QWidget()
        scroll_layout = QVBoxLayout(scroll_container)

        # Добавляем метки в контейнер
        if update_comments:
            for comment in update_comments:
                label = QLabel(comment)
                label.setFont(fonts['semibold'])
                scroll_layout.addWidget(label)
        else:
            label = QLabel('Новых обновлений нет', alignment=Qt.AlignmentFlag.AlignCenter)

            label.setFont(fonts['regular'])

            scroll_layout.addWidget(label)

        # Создаём QScrollArea и добавляем в неё контейнер с метками
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Разрешаем изменение размера
        scroll_area.setWidget(scroll_container)

        # Добавляем QScrollArea в основной layout
        main_layout.addWidget(scroll_area)

        # Создаём горизонтальный layout для кнопки
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Добавляем растяжку, чтобы кнопка была справа

        # Создаём кнопку "Обновить"
        if update_comments:
            update_button = QPushButton('Обновить')
            update_button.setFont(fonts['regular'])
            update_button.setCursor(Qt.CursorShape.PointingHandCursor)

            update_button.setStyleSheet("""
                QPushButton {
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #822f61;
                }
            """)

            update_button.clicked.connect(self._update)

            button_layout.addWidget(update_button)

        # Добавляем горизонтальный layout с кнопкой в основной layout
            main_layout.addLayout(button_layout)

        # Устанавливаем основной layout для окна
        self.setLayout(main_layout)


    def _update(self):
        update_project()
        self.close()
        update_complete = UpdateComplete()
        update_complete.exec()
