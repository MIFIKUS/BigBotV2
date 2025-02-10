from l2m_ui_funcs.main_screen import unlock_screen, lock_screen
from l2m_ui_funcs.actions_in_menus.respawn.respawn import respawn, get_lost_items, dead
from l2m_ui_funcs.actions_in_menus.locations.locations import tp_to_last_location

from ctypes.wintypes import HWND, DWORD
import ctypes

import win32gui
import win32com.client
import win32con

import time


user32 = ctypes.WinDLL("user32", use_last_error=True)
GetWindowThreadProcessId = user32.GetWindowThreadProcessId


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

        time.sleep(0.2)
        unlock_screen()
        time.sleep(1)
        if dead():
            respawn()
            get_lost_items()
            tp_to_last_location()

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


def get_window_pid() -> int:
    """Возвращает PID окна которое находится сверху"""
    hwnd = find_l2m_windows()[0]
    pid = DWORD()
    GetWindowThreadProcessId(HWND(hwnd), ctypes.byref(pid))
    return pid.value
