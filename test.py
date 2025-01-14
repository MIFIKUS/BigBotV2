import ctypes
from ctypes import wintypes

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


# Функция поиска строки UTF-16 LE в памяти процесса
def search_utf16_in_process(pid, search_string):
    # Преобразуем строку в UTF-16 LE
    search_bytes = search_string.encode('utf-16le')
    buffer_size = 0x1000  # Размер блока чтения (4 КБ)
    overlap = len(search_bytes)  # Перекрытие равно размеру искомой строки

    # Открываем процесс для чтения
    process_handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
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
                            print(f"String found at address: 0x{address + offset:x}")

                            # Чтение и декодирование строки по найденному адресу
                            found_address = address + offset
                            print(f"Reading string from address 0x{found_address:x}...")

                            # Читаем строку UTF-16 LE
                            decoded_string = read_unicode_string(process_handle, found_address)
                            print(f"Found string: {decoded_string}")

                            start = offset + 1  # Ищем дальше в текущем блоке

                    # Сдвиг адреса на размер блока минус перекрытие
                    address += buffer_size - overlap
            else:
                address += mbi.RegionSize
    finally:
        kernel32.CloseHandle(process_handle)


# Функция для чтения строки в формате UTF-16 LE
def read_unicode_string(process_handle, address, max_length=256):
    # Чтение данных из памяти
    buffer = (ctypes.c_char * max_length)()
    bytes_read = ctypes.c_size_t()
    if kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, max_length,
                                  ctypes.byref(bytes_read)):
        data = bytes(buffer[:bytes_read.value])

        # Преобразуем данные в строку, удаляя нулевые байты
        return data.decode('utf-16le', errors='ignore').rstrip('\x00')
    return ""


# Пример вызова
if __name__ == "__main__":
    pid = int(input("Enter process ID: "))
    search_utf16_in_process(pid, "Вы чувствуете вибрацию энергии мощной магии.")