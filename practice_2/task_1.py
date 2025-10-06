"""
task_1.py

Решение задачи на шифр Цезаря

Основные возможности:
- Шифрование и дешифрование
- Возможность выставить ключ шифрования и дешифрования
- Работа одновременно с английским и русским алфавитом
"""


import string


def main():
    data = get_data()

    while data[0] != 0:
        result = caesar(data[1], data[2], data[3])
        print(result)
        data = get_data()


def get_data() -> list:
    """
    Получает данные от пользователя для шифрования Цезаря

    Returns:
        list: набор необходимых данных
            [0]: flag (int) - флаг продолжения программы. Если возвращается
                 0, программа завершается
            [1]: text (str) - текст для шифрования/дешифрования
            [2]: mode (int) - режим работы. 1 - шифрование, 0 - дешифрование
            [3]: key (int) - ключ шифрования (смещение по шифру)
    """
    flag = 1

    text = input("Введите текст (enter для выхода): ")
    if text == '':
        return [0]

    mode = input("Режим работы "
                 "(1 - шифрование, 0 - дешифрование): ")
    while mode != '1' and mode != '0':
        mode = input('Требуется значение 0 - дешифрование '
                     'или 1 - шифрование!\n'
                     'Введите режим работы: ')
    mode = int(mode)

    key = input("Введите ключ шифрования (целое число): ")
    while not all(char in '0123456789-' for char in key):
        key = input("Требуется целочисленное значение!\n"
                    "Введите ключ шифрования: ")
    key = int(key)

    return [flag, text, mode, key]


def get_language(char: str) -> int:
    """
    Определяет язык, к которому относится символ.

    Returns:
        int: язык символа (0 - английский, 1 - русский)
    """
    if char in string.ascii_letters:
        return 0
    return 1


def caesar(text: str, mode: int, key: int) -> str:
    """
    Выполняет шифрование/дешифрование по шифру Цезаря

    Args:
        text (str): текст для шифрования/дешифрования
        mode (int): режим работы (0 - дешифрование, 1 - шифрование)
        key (int): ключ шифрования (смещение по алфавиту)

    Returns:
        result (str): получившийся результат шифрования/дешифрования
    """
    english_uppercase = string.ascii_uppercase
    english_lowercase = string.ascii_lowercase
    russian_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    russian_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ''

    if mode == 0:
        for i in range(len(text)):
            if text[i] not in english_lowercase + english_uppercase + \
                              russian_lowercase + russian_uppercase:
                result += text[i]
            else:
                if get_language(text[i]) == 0:
                    if str.isupper(text[i]):
                        result += english_uppercase[
                            (english_uppercase.index(text[i]) - key)
                            % len(english_uppercase)
                        ]
                    else:
                        result += english_lowercase[
                            (english_lowercase.index(text[i]) - key)
                            % len(english_lowercase)
                        ]
                elif get_language(text[i]) == 1:
                    if str.isupper(text[i]):
                        result += russian_uppercase[
                            (russian_uppercase.index(text[i]) - key)
                            % len(russian_uppercase)
                        ]
                    else:
                        result += russian_lowercase[
                            (russian_lowercase.index(text[i]) - key)
                            % len(russian_lowercase)
                        ]

    else:
        for i in range(len(text)):
            if text[i] not in english_lowercase + english_uppercase + \
                              russian_lowercase + russian_uppercase:
                result += text[i]
            else:
                if get_language(text[i]) == 0:
                    if str.isupper(text[i]):
                        result += english_uppercase[
                            (english_uppercase.index(text[i]) + key) %
                            len(english_uppercase)
                        ]
                    else:
                        result += english_lowercase[
                            (english_lowercase.index(text[i]) + key) %
                            len(english_lowercase)
                        ]
                elif get_language(text[i]) == 1:
                    if str.isupper(text[i]):
                        result += russian_uppercase[
                            (russian_uppercase.index(text[i]) + key) %
                            len(russian_uppercase)
                        ]
                    else:
                        result += russian_lowercase[
                            (russian_lowercase.index(text[i]) + key) %
                            len(russian_lowercase)
                        ]

    return result


if __name__ == "__main__":
    main()
