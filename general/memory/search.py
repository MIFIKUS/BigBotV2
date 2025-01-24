from ctypes import wintypes
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

# Флаги для открытия процесса


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


def find_addresses(process_handle, target_list: list) -> dict:
    """Ищет адреса памяти для каждого элемента в списке target_list"""
    buffer_size = 0x1000  # Размер блока чтения (4 КБ)

    # Словарь для хранения найденных адресов для каждого элемента
    results = {target: [] for target in target_list}

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

                        # Ищем каждый элемент из списка target_list
                        for target in target_list:
                            if isinstance(target, str):
                                search_bytes = target.encode('utf-16le')
                                start = 0
                                while (offset := data.find(search_bytes, start)) != -1:
                                    found_address = address + offset
                                    results[target].append(found_address)
                                    start = offset + len(search_bytes)
                            elif isinstance(target, (int, float)):
                                if len(str(target)) == 1:
                                    length = 1
                                else:
                                    length = 4
                                search_bytes = target.to_bytes(length, 'little', signed=isinstance(target, int))
                                start = 0
                                while (offset := data.find(search_bytes, start)) != -1:
                                    found_address = address + offset
                                    results[target].append(found_address)
                                    start = offset + len(search_bytes)

                    address += buffer_size

            else:
                address += mbi.RegionSize
    except:
        pass
    return results


def sort_addresses(process_handle, target_dict: dict) -> dict:
    """Сортирует адреса памяти в словаре, оставляя только те, которые содержат целевые значения"""

    try:
        sorted_results = {}

        for target, addresses in target_dict.items():
            print(target)
            valid_addresses = []

            for address in addresses:

                buffer = (ctypes.c_char * 256)()
                bytes_read = ctypes.c_size_t()

                if kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, 256, ctypes.byref(bytes_read)):
                    data = bytes(buffer[:bytes_read.value])

                    if isinstance(target, str):
                        # Преобразуем данные в строку
                        found_string = data.decode('utf-16le', errors='ignore').rstrip('\x00')
                        if target in found_string:
                            valid_addresses.append(address)
                    elif isinstance(target, (int, float)):
                        # Преобразуем данные в число
                        if len(str(target)) == 1:
                            lenght = 1
                        else:
                            lenght = 4

                        target_bytes = target.to_bytes(lenght, 'little', signed=isinstance(target, int))
                        if data.startswith(target_bytes):
                            valid_addresses.append(address)

            sorted_results[target] = valid_addresses


        return valid_addresses

    finally:
        pass


def get_value(process_handle, address: int, var_type: str or int, is_sharp=False):
    """Получает значения по адресу памяти"""
    if isinstance(var_type, int):
        if is_sharp:
            value = ctypes.c_uint8()
        else:
            value = ctypes.c_uint()
        bytes_read = ctypes.c_size_t()
        kernel32.ReadProcessMemory(
            process_handle,
            ctypes.c_void_p(address),  # Адрес памяти
            ctypes.byref(value),  # Буфер для чтения
            ctypes.sizeof(value),  # Размер буфера
            ctypes.byref(bytes_read)  # Реально прочитанные байты
        )

        return value.value

    elif isinstance(var_type, str):
        buffer = (ctypes.c_char * 256)()
        bytes_read = ctypes.c_size_t()

        if kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, 256, ctypes.byref(bytes_read)):
            data = bytes(buffer[:bytes_read.value])
            
        return data.decode('utf-16le', errors='ignore').rstrip('\x00')

    else:
        raise Exception('Есть поддержка только int и str')


