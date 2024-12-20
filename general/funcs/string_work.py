JUNK_SYMBOLS = ['\n', ' ', '"', '']


def delete_junk_symbols(word: str) -> str:
    """Удаляет мусорные символы из строки, в основном используется для удаления символов после переведения картинки в строку"""
    fixed_word = ''
    for i in word:
        if i in JUNK_SYMBOLS:
            continue
        fixed_word += i

    return fixed_word
