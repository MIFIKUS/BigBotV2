from general.funcs.checks import check, check_color


def classes_list_opened() -> bool:
    """Проверка на то, что вкладка Класс открыта"""
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_classes_list_opened.png'
    color = [245, 245, 245]
    area_of_screenshot = (327, 183, 328, 184)

    return check_color(color, screenshot_name, area_of_screenshot)


def fuses_list_opened() -> bool:
    """Проверка на то, что вкладка Синтез открыта"""
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_fuses_list_opened.png'
    color = [245, 245, 245]
    area_of_screenshot = (743, 183, 744, 184)

    return check_color(color, screenshot_name, area_of_screenshot)


def confirm_list_opened() -> bool:
    """Проверка на то, что меню подтверждения открыто"""
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_confirm_list_opened.png'
    color = [245, 245, 245]
    area_of_screenshot = (1151, 189, 1152, 190)

    return check_color(color, screenshot_name, area_of_screenshot)


def fuse_available() -> bool:
    """Проверка на то, что есть возможность синтеза"""
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_fuse_available.png'
    color = [215, 100, 10]
    area_of_screenshot = (1380, 930, 1381, 931)

    return check_color(color, screenshot_name, area_of_screenshot)


def no_more_fuse() -> bool:
    """Проверка на то, что больше нет карт для слияния"""
    template_name = 'bots\\booster\\fuse\\imgs\\templates\\nomore_fuses.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_nomore_fuses.png'
    area_of_screenshot = (650, 260, 1215, 310)

    return check(screenshot_name, template_name, area_of_screenshot)


def show_all_available() -> bool:
    """Проверка на то, что кнопка показать все доступна"""
    template_name = 'bots\\booster\\fuse\\imgs\\templates\\show_all_available.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_show_all_available.png'
    area_of_screenshot = (760, 910, 1120, 990)

    return check(screenshot_name, template_name, area_of_screenshot)


def repeat_available() -> bool:
    """Проверка на то, что повтор доступен"""
    template_name = 'bots\\booster\\fuse\\imgs\\templates\\repeat_available.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_show_all_available.png'
    area_of_screenshot = (940, 910, 1300, 990)

    return check(screenshot_name, template_name, area_of_screenshot)


def exit_available() -> bool:
    """Проверка на то, что есть кнопка выхода по середине, и больше нет карт для слияния"""
    template_name = 'bots\\booster\\fuse\\imgs\\templates\\exit_available.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_exit_available.png'
    area_of_screenshot = (750, 910, 1110, 990)

    return check(screenshot_name, template_name, area_of_screenshot)


def go_to_result_available() -> bool:
    """Проверка на то, что есть кнопка перейти к результату"""
    template_name = 'bots\\booster\\fuse\\imgs\\templates\\go_to_result.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_go_to_result_available.png'
    area_of_screenshot = (750, 910, 1110, 990)

    return check(screenshot_name, template_name, area_of_screenshot)


def confirm_red_available() -> bool:
    """Проверка на то, что есть классы для подтверждения"""
    template_name = 'l2m_ui_funcs\\imgs\\templates\\red_dot.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_exit_available.png'
    area_of_screenshot = (1280, 135, 1325, 175)

    return check(screenshot_name, template_name, area_of_screenshot)


def confirm_all_opened() -> bool:
    """Проверка на то, что кнопка подтвердить все нажата"""
    template_name = 'bots\\booster\\fuse\\imgs\\templates\\confirm_all_opened.png'
    screenshot_name = 'bots\\booster\\fuse\\imgs\\screenshots\\is_confirm_all_opened.png'
    area_of_screenshot = (640, 665, 1220, 745)

    return check(screenshot_name, template_name, area_of_screenshot)
