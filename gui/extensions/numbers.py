def custom_number(number):
    if number >= 1_000_000:
        return f"{number / 1_000_000:.0f}KK"  # Миллионы
    elif number >= 1_000:
        return f"{number / 1_000:.0f}K"  # Тысячи
    else:
        return str(number)