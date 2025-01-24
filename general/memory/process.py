from main_funcs.windows import get_window_pid
from ctypes import wintypes
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)


def get_process_handle():
    """Получает хендл процесса"""

    # Флаги для открытия процесса
    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_READ = 0x0010

    process = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, get_window_pid())
    print(get_window_pid())
    return process


def close_handle(process_handle):
    """Закрывает хендл процесса"""
    kernel32.CloseHandle(process_handle)
