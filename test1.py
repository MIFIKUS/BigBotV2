import ctypes
from ctypes import wintypes

# Определение функций и флагов
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

PROCESS_VM_READ = 0x0010
PROCESS_QUERY_INFORMATION = 0x0400

def read_null_terminated_unicode_string(pid, address, max_read=1024):
    # Открываем процесс для чтения
    process_handle = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
    if not process_handle:
        raise ctypes.WinError(ctypes.get_last_error())

    try:
        # Буфер для чтения данных
        buffer = (ctypes.c_char * max_read)()
        bytes_read = ctypes.c_size_t()

        # Читаем память начиная с адреса
        if not kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, max_read, ctypes.byref(bytes_read)):
            raise ctypes.WinError(ctypes.get_last_error())

        # Преобразуем прочитанные данные в строку UTF-16
        data = buffer.raw[:bytes_read.value]
        end_idx = data.find(b'\x00\x00')  # Поиск конца строки (нулевой символ)
        if end_idx != -1:
            print(data[:end_idx + 2])
            return data[:end_idx + 2].decode('utf-8').rstrip('\x00')
        else:
            raise ValueError("String termination not found within max_read bytes.")
    finally:
        kernel32.CloseHandle(process_handle)

# Пример использования
pid = int(input("Enter process ID: "))  # Укажите PID процесса
address = int(input("Enter address to read (hex): "), 16)  # Адрес строки

try:
    result = read_null_terminated_unicode_string(pid, address)
    print(f"String at address 0x{address:x}: {result}")
except Exception as e:
    print(f"Error: {e}")