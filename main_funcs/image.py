from general.logs.logger import logger

from PIL import Image as pil

import cv2
import numpy as np
import pytesseract
import PIL.ImageGrab


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def matching(main_image_name, template_image_name, threshold=0.8) -> bool:
    """Сравнивает 2 изображения"""
    logger.debug(f'Сравнение {main_image_name} с {template_image_name} threshold: {threshold}')
    img_rgb = cv2.imread(main_image_name)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_image_name, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        i = pt
    try:
        logger.debug('Шаблон найден')
        return pt
    except:
        logger.debug('Шаблон не найден')
        return False


def get_matching_image_cords(main_image_name, template_image_name, threshold=0.8) -> tuple or bool:
    """Возвращает координаты найденного шаблона, возвращает False если не смог найти"""
    logger.debug(f'Поиск координат на {main_image_name} Шаблон: {template_image_name} threshold: {threshold}')
    img_rgb = cv2.imread(main_image_name)
    template = cv2.imread(template_image_name)

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        logger.debug(f'Координаты найдены: {pt}')
        return pt
    logger.debug('Координаты не найдены')
    return False


def take_screenshot(image_name, area_of_screenshot=None):
    """Делает скриншот"""
    logger.debug(f'Создание скриншота {image_name} координаты: {area_of_screenshot}')
    if area_of_screenshot:
        main_screen = PIL.ImageGrab.grab(bbox=area_of_screenshot)
    else:
        main_screen = PIL.ImageGrab.grab()
    main_screen.save(image_name)


def get_main_color(file, colors_amount=1024) -> tuple:
    """Получает самый частый цвет на картинке"""
    logger.debug(f'Получение основного цвета для {file} colors_amount: {colors_amount}')
    img = pil.open(file)
    colors = img.getcolors(colors_amount)  # put a higher value if there are many colors in your image

    colors = sorted(colors)
    if (0,0,0) in colors:
        colors.remove(colors[0])
    logger.debug(f'Основной цвет: {colors[0][1]}')
    return colors[0][1]


def image_to_string(image_name: str, is_digits: bool, custom_config='') -> str:
    """Переводит картинку в строку"""
    logger.debug(f'Перевод картинки в текст {image_name} is_digits: {is_digits} custom_config: {custom_config}')

    if custom_config:
        text = pytesseract.image_to_string(image_name, config=custom_config)
        logger.debug(f'Полученный текст: {text}')
        return text

    if is_digits:
        text = pytesseract.image_to_string(image_name, config='--psm 11 -c tessedit_char_whitelist=0123456789/')
        logger.debug(f'Полученный текст: {text}')
        return text

    text = pytesseract.image_to_string(image_name, lang='rus', config='--psm 3')
    logger.debug(f'Полученный текст: {text}')
    return text


def delete_all_colors_except_one(image_name: str, color, color_min_list=None, color_max_list=None, new_image_name=''):
    """Удаляет с картинки все цвета кроме одного"""
    im = cv2.imread(image_name)

    threshold = 10

    logger.debug(f'Удаление всех цветов кроме одного с {image_name} color: {color} color_min_list={color_min_list} color_max_list: {color_max_list} new_image_name: {new_image_name}')

    if color:
        r, g, b = color

        r_min = r - threshold
        g_min = g - threshold
        b_min = b - threshold

        r_max = r + threshold
        g_max = g + threshold
        b_max = b + threshold
    else:
        r_min, g_min, b_min = color_min_list
        r_max, g_max, b_max = color_max_list

    color_min = np.array([r_min, g_min, b_min], np.uint8)
    color_max = np.array([r_max, g_max, b_max], np.uint8)

    rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(rgb, color_min, color_max)

    inverse_cachement_mask = cv2.bitwise_not(mask)
    im[inverse_cachement_mask > 0] = [0, 0, 0]

    if new_image_name:
        cv2.imwrite(new_image_name, mask)
    else:
        cv2.imwrite(image_name, mask)

