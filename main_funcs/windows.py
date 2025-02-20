from l2m_ui_funcs.main_screen import unlock_screen, lock_screen
from l2m_ui_funcs.actions_in_menus.respawn.respawn import respawn, get_lost_items, dead
from l2m_ui_funcs.actions_in_menus.locations.locations import tp_to_last_location

from general.logs.logger import logger

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

    for window in windows_list:
        logger.debug(f'Открытик окна с HWND: {window}')
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
    all_windows = [hwnd for hwnd in hwnd_list if 'Lineage2M' in win32gui.GetWindowText(hwnd)]

    logger.debug(f'Список всех HWND окон линейки {all_windows}')

    return all_windows


def get_window_pid() -> int:
    """Возвращает PID окна которое находится сверху"""
    hwnd = find_l2m_windows()[0]
    pid = DWORD()
    GetWindowThreadProcessId(HWND(hwnd), ctypes.byref(pid))
    final_pid = pid.value
    logger.debug(f'PID по HWND HWND: {hwnd} PID: {final_pid}')

    return final_pid
