from PIL import Image as pil

import cv2
import pyscreenshot
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def matching(main_image_name, template_image_name, threshold=0.8) -> bool:
    """Сравнивает 2 изображения"""
    img_rgb = cv2.imread(main_image_name)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_image_name, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        i = pt
    try:
        return pt
    except:
        return False


def get_matching_image_cords(main_image_name, template_image_name, threshold=0.8) -> tuple or bool:
    """Возвращает координаты найденного шаблона, возвращает False если не смог найти"""

    img_rgb = cv2.imread(main_image_name)
    template = cv2.imread(template_image_name)

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        return pt
    return False


def take_screenshot(image_name, area_of_screenshot=None):
    """Делает скриншот"""
    if area_of_screenshot:
        main_screen = pyscreenshot.grab(bbox=area_of_screenshot)
    else:
        main_screen = pyscreenshot.grab()
    main_screen.save(image_name)


def get_main_color(file, colors_amount=1024) -> tuple:
    """Получает самый частый цвет на картинке"""
    img = pil.open(file)
    colors = img.getcolors(colors_amount)  # put a higher value if there are many colors in your image

    colors = sorted(colors)
    if (0,0,0) in colors:
        colors.remove(colors[0])
    return colors[0][1]


def image_to_string(image_name: str, is_digits: bool, custom_config='') -> str:
    """Переводит картинку в строку"""
    if custom_config:
        return pytesseract.image_to_string(image_name, config=custom_config)
    if is_digits:
        return pytesseract.image_to_string(image_name, config='--psm 11 -c tessedit_char_whitelist=0123456789/')

    return pytesseract.image_to_string(image_name, lang='rus', config='--psm 3')


def delete_all_colors_except_one(image_name: str, color: [int], color_min_list=None, color_max_list=None):
    """Удаляет с картинки все цвета кроме одного"""
    im = cv2.imread(image_name)

    threshold = 10

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

    cv2.imwrite(image_name, mask)

