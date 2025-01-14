from ahk import AHK

ahk = AHK()


def y():
    """Нажимает Y"""
    while True:
        try:
            ahk.key_press('y')
            break
        except:
            pass


def esc():
    """Нажимает esc"""
    while True:
        try:
            ahk.key_press('esc')
            break
        except:
            pass
