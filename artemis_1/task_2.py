def rational_to_decimal(numerator: int, denominator: int, precision=10):
    """
    Функция для точного деления двух целых чисел. Может работать с указанной
    точностью и корректно отображать числа с периодом.

    Args:
        numerator (int): числитель
        denominator (int): знаменатель
        precision (int): точность в количестве знаков после запятой.

    Returns:
        str: дробное число.
    """

    # Убедимся, что значения даны верные.
    if denominator == 0:
        raise ValueError('Деление на ноль невозможно!')
    if precision < 0:
        raise ValueError('Точность не может быть отрицательной.')

    # Определим знак итогового числа.
    if (numerator > 0 and denominator < 0) or \
            (numerator < 0 and denominator > 0):
        sign = '-'
    else:
        sign = ''

    # Знак уже учтён - теперь можно работать только с положительными числами.
    numerator = abs(numerator)
    denominator = abs(denominator)

    # Найдём целую часть и целый остаток при делении.
    integer_part = str(numerator // denominator)
    remainder = numerator % denominator

    # Если остаток получился равным 0, значит деление было целочисленным.
    # Вернём целое число.
    if remainder == 0:
        return f'{sign}{integer_part}'

    remainder_list = []  # Список остатков.
    decimal_part = ''  # Дробная часть (цифры после точки).

    # Осуществим деление до самого конца либо до обнаружения периода.
    while remainder not in remainder_list and remainder != 0:
        remainder_list.append(remainder)  # Сначала добавим последний остаток.
        remainder *= 10  # "Снесём" запятую.
        decimal_part += str(remainder // denominator)
        remainder %= denominator

    # Отформатируем вывод с учетом знака и наличия периода.
    if remainder == 0:
        return f'{sign}{integer_part}.{decimal_part[:precision]}'
    period_position = remainder_list.index(remainder)
    not_period = ''.join(decimal_part[:period_position])
    period = ''.join(decimal_part[period_position:])
    if precision < len(decimal_part):
        return f'{sign}{integer_part}.{decimal_part[:precision]}'
    return f'{sign}{integer_part}.{not_period}({period})'
