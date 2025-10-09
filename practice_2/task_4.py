"""
task_4.py

Программа для генерации паролей

Основные возможности:
- Выставление длины
- Включение/отключение верхнего/нижнего регистра
- Включение/отключение специальных символов
- Включение/отключение цифр в пароле
- Удобное консольное меню
- Проверка корректности введённых данных
- Завершение программы только по требованию пользователя
"""


import string
import random


def main():
    lenght = 10
    uppercase = True
    lowercase = True
    special = True
    digits = True

    print("Генератор паролей")
    get_help()
    command = input("> ").replace(' ', '')
    while command != "quit":
        if command == "values":
            show_values(lenght, uppercase, lowercase, special, digits)
            command = input("> ").replace(' ', '')
        elif command == "lenght":
            lenght = set_lenght()
            command = input("> ").replace(' ', '')
        elif command == "uppercase":
            uppercase = set_uppercase()
            command = input("> ").replace(' ', '')
        elif command == "lowercase":
            lowercase = set_lowercase()
            command = input("> ").replace(' ', '')
        elif command == "special":
            special = set_special()
            command = input("> ").replace(' ', '')
        elif command == "digits":
            digits = set_digits()
            command = input("> ").replace(' ', '')
        elif command == "create":
            print(
                create_password(lenght, uppercase, lowercase, special, digits)
            )
            command = input("> ").replace(' ', '')
        elif command == "help":
            get_help()
            command = input("> ").replace(' ', '')
        else:
            print("Некорректная команда!")
            command = input("> ").replace(' ', '')


def get_help():
    """
    Выводит список допустимых команд в программе.
    """
    print("Список доступных команд:\n"
          "values - показать выставленные значения\n"
          "lenght - выставить длину пароля (по умолчанию 10)\n"
          "uppercase - выставить наличие верхнего регистра в пароле "
          "(по умолчанию вкл)\n"
          "lowercase - выставить наличие нижнего регистра в пароле "
          "(по умолчанию вкл)\n"
          "special - использование специальных символов (по умолчанию вкл)\n"
          "digits - использования цифр в пароле (по умолчанию вкл)\n"
          "create - сгенерировать пароль\n"
          "help - показать список команд\n"
          "quit - завершить программу")


def show_values(lenght: int, uppercase: bool, lowercase: bool, special: bool,
                digits: bool):
    """
    Выводит все выставленные значения для генерации пароля

    Args:
        lenght (int): длина пароля
        uppercase (bool): использование верхнего регистра
        lowercase (bool): использование нижнего регистра
        special (bool): использование специальных символов
        digits (bool): использование цифр
    """
    print(f"длина пароля: {lenght}")
    print(f"верхний регистр: {"вкл" if uppercase is True else "выкл"}")
    print(f"нижний регистр: {"вкл" if lowercase is True else "выкл"}")
    print(f"специальные символы: {"вкл" if special is True else "выкл"}")
    print(f"цифры: {"вкл" if special is True else "выкл"}")


def set_lenght() -> int:
    """
    Возвращает введённую пользователем длину пароля

    Returns:
        lenght (int): длина пароля
    """
    print("Введите длину пароля:")
    lenght = input("> ").replace(' ', '')
    while not (all(i in string.digits for i in lenght) and lenght != ''):
        print("Некорректное значение! Введите длину пароля:")
        lenght = input("> ").replace(' ', '')
    print(f"Выставлено значение {lenght}")

    return int(lenght)


def set_uppercase() -> bool:
    """
    Возвращает логическое условие (вкл/выкл верхний регистр)

    Returns:
        bool: использование верхнего регистра
    """
    print("Использование верхнего регистра [вкл/выкл]:")
    uppercase = input("> ").replace(' ', '')
    while uppercase.upper() != "ВКЛ" and uppercase.upper() != "ВЫКЛ":
        print("Некорректное значение! Требуется вкл/выкл")
        uppercase = input("> ").replace(' ', '')
    print(f"Выставлено значение {uppercase}")

    return True if uppercase.upper() == 'ВКЛ' else False


def set_lowercase() -> bool:
    """
    Возвращает логическое условие (вкл/выкл нижний регистр)

    Returns:
        bool: использование нижнего регистра
    """
    print("Использование нижнего регистра [вкл/выкл]:")
    lowercase = input("> ").replace(' ', '')
    while lowercase.upper() != "ВКЛ" and lowercase.upper() != "ВЫКЛ":
        print("Некорректное значение! Требуется вкл/выкл")
        lowercase = input("> ").replace(' ', '')
    print(f"Выставлено значение {lowercase}")

    return True if lowercase.upper() == 'ВКЛ' else False


def set_special() -> bool:
    """
    Возвращает логическое условие (вкл/выкл специальные символы)

    Returns:
        bool: использование специальных символов
    """
    print("Использование специальных символов [вкл/выкл]:")
    special = input("> ").replace(' ', '')
    while special.upper() != "ВКЛ" and special.upper() != "ВЫКЛ":
        print("Некорректное значение! Требуется вкл/выкл")
        special = input("> ").replace(' ', '')
    print(f"Выставлено значение {special}")

    return True if special.upper() == 'ВКЛ' else False


def set_digits() -> bool:
    """
    Возвращает логическое условие (вкл/выкл цифры)

    Returns:
        bool: использование цифр
    """
    print("Использование цифр [вкл/выкл]:")
    digits = input("> ").replace(' ', '')
    while digits.upper() != "ВКЛ" and digits.upper() != "ВЫКЛ":
        print("Некорректное значение! Требуется вкл/выкл")
        digits = input("> ").replace(' ', '')
    print(f"Выставлено значение {digits}")

    return True if digits.upper() == 'ВКЛ' else False


def create_password(lenght: int, uppercase: bool, lowercase: bool,
                    special: bool, digits: bool) -> str:
    """
    Генерирует пароль по выставленным аргументам

    Args:
        lenght (int): длина пароля
        uppercase (bool): использование верхнего регистра
        lowercase (bool): использование нижнего регистра
        special (bool): использование специальных символов
        digits (bool): использование цифр
    Returns:
        password (str): готовый пароль
    """
    alphabet = ''
    if uppercase is True:
        alphabet += string.ascii_uppercase
    if lowercase is True:
        alphabet += string.ascii_lowercase
    if special is True:
        alphabet += string.punctuation
    if digits is True:
        alphabet += string.digits

    password = ''
    if alphabet != '':
        for i in range(lenght):
            password += random.choice(alphabet)

    return password


if __name__ == '__main__':
    main()
