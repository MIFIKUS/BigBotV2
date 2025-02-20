from datetime import datetime
import logging


logger = logging.getLogger('logs')

if not logger.handlers:
    # Определяем форматтер для всех обработчиков
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Формируем имя файла с логами, включая текущую дату
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"logs\\{date_str}.log"

    # Обработчик для записи логов в файл
    file_handler = logging.FileHandler(log_filename, mode='a')  # 'a' — добавление в конец файла
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

