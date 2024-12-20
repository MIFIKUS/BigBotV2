from l2m_ui_funcs.main_screen import unlock_screen, lock_screen

import win32gui
import win32com.client
import win32con


def switch_windows(func):
    """Переключает окна и запускает функцию"""
    shell = win32com.client.Dispatch("WScript.Shell")

    windows_list = find_l2m_windows()
    print(windows_list)
    for window in windows_list:
        shell.SendKeys('%')
        win32gui.ShowWindow(window, win32con.SW_RESTORE)
        while True:
            try:
                win32gui.SetForegroundWindow(window)
                break
            except:
                pass

        unlock_screen()
        func()
        lock_screen()


def find_l2m_windows() -> list:
    """Ищет все окна линейки"""
    def _is_toplevel(hwnd):
        """Проверяет доступно ли окно"""
        return win32gui.GetParent(hwnd) == 0 and win32gui.IsWindowVisible(hwnd)

    hwnd_list = []

    win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd) if _is_toplevel(hwnd) else None, hwnd_list)

    hwnd_list = [hwnd for hwnd in hwnd_list if 'Lineage2M' in win32gui.GetWindowText(hwnd)]

    return [hwnd for hwnd in hwnd_list if 'Lineage2M' in win32gui.GetWindowText(hwnd)]
