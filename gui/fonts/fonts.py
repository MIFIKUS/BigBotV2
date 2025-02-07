from PySide6.QtGui import QFontDatabase, QFont


def load_fonts():
    """
    Загружает шрифты из файлов и возвращает словарь с объектами QFont.
    """
    # Загружаем шрифты из файлов

    path_to_fonts = 'gui\\fonts\\sf\\'

    font_files = [
        "SF-Pro-Display-Black.otf",
        "SF-Pro-Display-BlackItalic.otf",
        "SF-Pro-Display-Bold.otf",
        "SF-Pro-Display-BoldItalic.otf",
        "SF-Pro-Display-Heavy.otf",
        "SF-Pro-Display-HeavyItalic.otf",
        "SF-Pro-Display-Light.otf",
        "SF-Pro-Display-LightItalic.otf",
        "SF-Pro-Display-Medium.otf",
        "SF-Pro-Display-MediumItalic.otf",
        "SF-Pro-Display-Regular.otf",
        "SF-Pro-Display-RegularItalic.otf",
        "SF-Pro-Display-Semibold.otf",
        "SF-Pro-Display-SemiboldItalic.otf",
        "SF-Pro-Display-Thin.otf",
        "SF-Pro-Display-ThinItalic.otf",
        "SF-Pro-Display-Ultralight.otf",
        "SF-Pro-Display-UltralightItalic.otf",
    ]

    for font_file in font_files:
        font_file = path_to_fonts + font_file
        QFontDatabase.addApplicationFont(font_file)

    # Создаем объекты QFont для каждого стиля
    fonts = {
        "black": QFont("SF Pro Display", 16, QFont.Weight.Black),
        "black_italic": QFont("SF Pro Display", 16, QFont.Weight.Black),
        "bold": QFont("SF Pro Display", 16, QFont.Weight.Bold),
        "bold_italic": QFont("SF Pro Display", 16, QFont.Weight.Bold),
        "heavy": QFont("SF Pro Display", 16, QFont.Weight.ExtraBold),
        "heavy_italic": QFont("SF Pro Display", 16, QFont.Weight.ExtraBold),
        "light": QFont("SF Pro Display", 16, QFont.Weight.Light),
        "light_italic": QFont("SF Pro Display", 16, QFont.Weight.Light),
        "medium": QFont("SF Pro Display", 16, QFont.Weight.Medium),
        "medium_italic": QFont("SF Pro Display", 16, QFont.Weight.Medium),
        "regular": QFont("SF Pro Display", 16, QFont.Weight.Normal),
        "regular_italic": QFont("SF Pro Display", 16, QFont.Weight.Normal),
        "semibold": QFont("SF Pro Display", 16, QFont.Weight.DemiBold),
        "semibold_italic": QFont("SF Pro Display", 16, QFont.Weight.DemiBold),
        "thin": QFont("SF Pro Display", 16, QFont.Weight.Thin),
        "thin_italic": QFont("SF Pro Display", 16, QFont.Weight.Thin),
        "ultralight": QFont("SF Pro Display", 16, QFont.Weight.ExtraLight),
        "ultralight_italic": QFont("SF Pro Display", 16, QFont.Weight.ExtraLight),
    }

    # Устанавливаем курсив для соответствующих шрифтов
    fonts["black_italic"].setItalic(True)
    fonts["bold_italic"].setItalic(True)
    fonts["heavy_italic"].setItalic(True)
    fonts["light_italic"].setItalic(True)
    fonts["medium_italic"].setItalic(True)
    fonts["regular_italic"].setItalic(True)
    fonts["semibold_italic"].setItalic(True)
    fonts["thin_italic"].setItalic(True)
    fonts["ultralight_italic"].setItalic(True)

    return fonts