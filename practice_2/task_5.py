"""
Программа для конвертации римского числа в арабское или наоборот

Основные возможности
- Автоматическое определение, к какому из систем счёта относится число
- Проверка данных
"""


def main():
    print("Введите число для конвертации. Программа сама определит,\n"
          "к какой системе счёта относится это число и в какую систему\n"
          "счёта его нужно перевести.")
    print("Обратите внимание, что программа не работает с отрицательными "
          "числами")

    number = input("> ")
    roman = all(digit in "0123456789" for digit in number)
    arabic = all(digit in 'MDCLXVI' for digit in number)
    while not roman and not arabic:
        print("Введено некорректное число! Введите положительное арабское или "
              "римское число")
        number = input("> ")

    if roman:
        print(converting(number, 0))
    elif arabic:
        print(converting(number, 1))


def converting(number: str, mode: int) -> str:
    """
    Функция для перевода числа из арабской системы в римскую и наоборот

    Args:
        number (str): число, которое нужно конвертировать
        mode (int): режим конвертации
            1: перевод римского числа в арабское
            0: перевод арабского числа в римское

    Returnes:
        result (str): число после конвертации
    """
    vars = [
        ['M', 1000], ['CM', 900], ['D', 500], ['CD', 400],
        ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
        ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]
    ]
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if mode == 0:
        result = ''
        number = int(number)
        for roman_var, arabic_var in vars:
            while number >= arabic_var:
                result += roman_var
                number -= arabic_var

    elif mode == 1:
        result = 0
        for digit in range(len(number) - 1):
            if digits[number[digit]] < digits[number[digit + 1]]:
                result -= digits[number[digit]]
            else:
                result += digits[number[digit]]
        result += digits[number[-1]]
        result = str(result)
    return result


if __name__ == '__main__':
    main()
