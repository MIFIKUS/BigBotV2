from main_funcs.windows import get_window_pid
from ctypes import wintypes
import ctypes


kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Флаги для открытия процесса
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010


# Структура для информации о памяти
class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ('BaseAddress', ctypes.c_void_p),
        ('AllocationBase', ctypes.c_void_p),
        ('AllocationProtect', wintypes.DWORD),
        ('RegionSize', ctypes.c_size_t),
        ('State', wintypes.DWORD),
        ('Protect', wintypes.DWORD),
        ('Type', wintypes.DWORD),
    ]


def find_addresses(target: str) -> list:
    """Ищет адреса памяти строки или числа"""
    search_bytes = target.encode('utf-16le')
    buffer_size = 0x1000  # Размер блока чтения (4 КБ)
    overlap = len(search_bytes)  # Перекрытие равно размеру искомой строки

    found_addresses = []

    process_handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, get_window_pid())
    if not process_handle:
        raise ctypes.WinError(ctypes.get_last_error())

    try:
        mbi = MEMORY_BASIC_INFORMATION()
        address = 0

        while kernel32.VirtualQueryEx(process_handle, ctypes.c_void_p(address), ctypes.byref(mbi), ctypes.sizeof(mbi)):
            # Проверяем, доступна ли память для чтения
            if mbi.State == 0x1000 and mbi.Protect in (0x04, 0x02, 0x20):  # MEM_COMMIT и читаемые
                region_end = address + mbi.RegionSize

                while address < region_end:
                    # Вычисляем размер буфера для чтения
                    size_to_read = min(buffer_size, region_end - address)

                    # Читаем память
                    buffer = (ctypes.c_char * size_to_read)()
                    bytes_read = ctypes.c_size_t()
                    if kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, size_to_read,
                                                  ctypes.byref(bytes_read)):
                        data = bytes(buffer[:bytes_read.value])

                        # Ищем строку в прочитанных данных
                        start = 0
                        while (offset := data.find(search_bytes, start)) != -1:
                            # Печатаем адрес, где найдена строка
                            found_address = address + offset

                            found_addresses.append(found_address)

                    address += buffer_size - overlap
            else:
                address += mbi.RegionSize
    finally:
        kernel32.CloseHandle(process_handle)

    return found_addresses


def sort_addresses(target: str, addresses_list: list) -> list:
    """Сортирует адреса из списка. Чтобы в них было значение из target"""
    found_addresses = []

    process_handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, get_window_pid())

    for address in addresses_list:
        buffer = (ctypes.c_char * 256)()
        bytes_read = ctypes.c_size_t()
        if kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, 256,
                                      ctypes.byref(bytes_read)):
            data = bytes(buffer[:bytes_read.value])

            # Преобразуем данные в строку, удаляя нулевые байты
            found_string = data.decode('utf-16le', errors='ignore').rstrip('\x00')

            if target in found_string:
                found_addresses.append(address)

    return found_addresses


