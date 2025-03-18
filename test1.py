import tkinter as tk
import win32gui
import random


class HUDOverlay:
    def __init__(self, target_title):
        self.target_title = target_title

        # Создаём окно без рамок, всегда поверх остальных и с прозрачным фоном.
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # убираем стандартное оформление окна
        self.root.wm_attributes("-topmost", True)
        # Устанавливаем цвет прозрачности (здесь "white" – фон канвы будет прозрачным)
        self.root.wm_attributes("-transparentcolor", "white")

        # Создаём канву для рисования HUD
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Параметры внешнего вида (можно менять через метод customize_appearance)
        self.health_color = "red"
        self.ammo_color = "yellow"
        self.font = ("Arial", 16, "bold")

        # Пример игровых данных
        self.health = 100
        self.ammo = 50

        # Привязываемся к нужному окну (по заголовку)
        self.attach_to_window()
        self.update_data()

    def attach_to_window(self):
        # Находим окно по заголовку. Замените target_title на фактический заголовок игрового окна.
        hwnd = win32gui.FindWindow(None, self.target_title)
        if hwnd:
            # Получаем позицию и размеры целевого окна
            rect = win32gui.GetWindowRect(hwnd)
            x, y, x2, y2 = rect
            width = x2 - x
            height = y2 - y
            # Устанавливаем геометрию HUD-окна, чтобы оно совпадало с целевым окном
            self.root.geometry(f"{width}x{height}+{x}+{y}")
        else:
            print("Целевое окно не найдено. Проверьте заголовок окна.")

    def update_data(self):
        # Очищаем канву и рисуем HUD-элементы (например, текстовые индикаторы здоровья и боеприпасов)
        self.canvas.delete("all")
        self.canvas.create_text(50, 20, text=f"Health: {self.health}", fill=self.health_color, font=self.font)
        self.canvas.create_text(50, 50, text=f"Ammo: {self.ammo}", fill=self.ammo_color, font=self.font)
        # Запланировать обновление данных через 1000 мс (можно заменить на реальные данные игры)
        self.root.after(1000, self.simulate_game_data)

    def simulate_game_data(self):
        # Симуляция изменения игровых данных для демонстрации (уменьшаем значения случайно)
        self.health = max(0, self.health - random.randint(0, 5))
        self.ammo = max(0, self.ammo - random.randint(0, 3))
        self.update_data()

    def customize_appearance(self, health_color=None, ammo_color=None, font=None):
        """
        Метод для изменения внешнего вида HUD.
        Параметры:
          health_color: цвет текста для индикатора здоровья;
          ammo_color: цвет текста для индикатора боеприпасов;
          font: кортеж с параметрами шрифта.
        """
        if health_color:
            self.health_color = health_color
        if ammo_color:
            self.ammo_color = ammo_color
        if font:
            self.font = font
        self.update_data()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    # Задайте заголовок окна, к которому нужно привязать HUD (например, заголовок окна игры)
    target_window_title = "Параметры"  # Замените на фактический заголовок
    hud = HUDOverlay(target_window_title)


    # Пример смены внешнего вида (раскомментируйте, чтобы увидеть эффект)
    # hud.customize_appearance(health_color="green", ammo_color="blue", font=("Comic Sans MS", 18, "bold"))

    hud.run()
