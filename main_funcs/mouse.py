from ahk import AHK

ahk = AHK()


def move(x: int, y: int):
    """Двигает мышку по координатам"""
    while True:
        try:
            ahk.mouse_move(x, y, speed=0)
            break
        except Exception:
            pass


def click():
    """Делает клик мышкой"""
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
    while True:
        try:
            ahk.mouse_drag(x, y, relative=relative)
            break
        except:
            pass


def wheel_down(amount_of_spins: int):
    """Вращает колесико мышки вниз"""
    while True:
        try:
            for _ in  range(amount_of_spins):
                ahk.wheel_down()
            break
        except:
            pass


def wheel_up(amount_of_spins: int):
    """Вращает колесико мышки вверх"""
    while True:
        try:
            for _ in range(amount_of_spins):
                ahk.wheel_up()
            break
        except:
            pass

