from general.funcs.checks import check, check_color


def rewards_in_battle_pass_available(battle_pass_num: int) -> bool:
    """Проверка что в выбранном сезонном пропуске есть награды"""
    template_name = 'bots\\sbor\\imgs\\templates\\rewards_in_battle_pass_available.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_rewards_in_battle_pass_available.png'
    area_of_screenshot = (45 + (battle_pass_num * 340), 140, 385 + (battle_pass_num * 340), 170)

    return check(screenshot_name, template_name, area_of_screenshot)


def rewards_in_sub_battle_pass_available(sub_battle_pass_num: int) -> bool:
    """Проверка что в выбранной подкатегории сезонного пропуска доступны награды"""
    template_name = 'bots\\sbor\\imgs\\templates\\rewards_in_sub_battle_pass_available.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_rewards_in_sub_battle_pass_available.png'
    area_of_screenshot = (45, 250 + (90 * sub_battle_pass_num), 78, 280 + (90 * sub_battle_pass_num))

    return check(screenshot_name, template_name, area_of_screenshot)


def get_subreward_available() -> bool:
    """Проверка что есть кнопка Получить"""
    template_name = 'bots\\sbor\\imgs\\templates\\battle_pass_reward_button.png'
    screenshot_name = 'bots\\sbor\\imgs\\screenshots\\is_battle_pass_reward_button_available.png'
    area_of_screenshot = (1240, 285, 1375, 350)

    return check(screenshot_name, template_name, area_of_screenshot)


