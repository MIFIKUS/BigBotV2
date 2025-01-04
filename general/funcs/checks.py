from main_funcs import image


def check(screenshot_name: str, template_name: str, area_of_screenshot: tuple or None) -> bool:
    """Макет для проверки картинки, в основном используется для проверки открыты ли менюшки"""

    image.take_screenshot(screenshot_name, area_of_screenshot)

    return image.matching(screenshot_name, template_name)


def check_color(color: list[int], screenshot_name: str, area_of_screenshot: tuple) -> bool:
    """Макет для проверки цвета, в основном используется для проверки того, активна ли менюшка"""
    image.take_screenshot(screenshot_name, area_of_screenshot)

    img_color = image.get_main_color(screenshot_name)

    print(img_color)

    threshold = 10 #Разброс по цвету, например 200 - threshold(10) = 190

    color_red, color_green, color_blue = color
    img_color_red, img_color_green, img_color_blue = img_color

    if (color_red - threshold) <= img_color_red <= (color_red + threshold) and \
       (color_green - threshold) <= img_color_green <= (color_green + threshold) and \
       (color_blue - threshold) <= img_color_blue <= (color_blue + threshold):

        return True
    return False


