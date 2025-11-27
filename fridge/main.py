"""
Программа, содержащие функции для холодильника.

Основные возможности:
- Умное добавление продуктов в холодильник с поиском нужных данных в строке.
- Поиск продуктов в холодильнике по подстроке.
- Поиск количества продуктов определённого названия.
"""


import datetime
from decimal import Decimal


def add(items, title, amount, expiration_date=None):
    """
    Функция для прямого добавления продуктов в холодильник, работает только
    с точным описанием продукта.

    Args:
        items (dict): словарь, представляющий собой холодильник.
        title (str): название продукта.
        amount (Decimal): количество штук (или объём) в одной единице продукта.
        expiration_date (datetime.date): срок годности продукта.
    """
    # На случай, если ключа в словаре нет вообще, т. к. потом мы применяем
    # append к уже существующему списку.
    if title not in items:
        items[title] = []

    # expiration date не является необходимым, а None здесь обрабатывается
    # иначе, поэтому проводим проверку:
    if expiration_date is not None:
        # Дата в функцию поступает не в нужном виде, поэтому строку типа
        # %Y-%m-%d приводим к типу datetime.date
        expiration_date = datetime.datetime.strptime(
                              expiration_date, r'%Y-%m-%d'
                          ).date()
        items[title].append(
            {
                'amount': amount,
                'expiration_date': expiration_date
            }
        )
    # Добавляем элемент по другому, если expiration_date не задан.
    else:
        items[title].append(
            {
                'amount': amount,
                'expiration_date': None
            }
        )


def add_by_note(items, note):
    """
    Функция для удобного добавления продуктов в холодильник, выделяет из
    строки нужные данные.

    Args:
        items (dict): словарь, представляющий собой холодильник.
        note (str): строка с описанием продукта.
    """
    # Строка note, если разбить её по пробелам, в любом случае будет иметь
    # следующий вид:
    # Последний элемент - дата, если имеет "-"; количество продуктов в
    # противном случае.
    # Предпоследний элемент - количество продуктов, если не нашли дату; часть
    # названия продукта в противном случае.
    # Всё остальное - части названия продукта.
    title = None
    amount = None
    expiration_date = None
    note = note.split()
    if '-' in note[-1]:
        expiration_date = note.pop(-1)
    else:
        expiration_date = None
    amount = note.pop(-1)
    title = ' '.join(note)

    # Отфильтрованные данные добавляем в холодильник.
    add(items, title, Decimal(amount), expiration_date)


def find(items, needle):
    """
    Функция для поиска продуктов в холодильнике.

    Args:
        items (dict): словарь, представляющий собой холодильник.
        needle (str): подстрока, которая ищется среди всех названий продуктов
                      в холодильнике.

    Returns:
        result (list): список названий, соответствующих подстроке needle.
    """
    items_keys = dict.keys(items)  # Получаем все ключи (названия продуктов).
    result = []  # Итоговый список товаров.

    for item in items_keys:  # Проверяем на соответсвие needle каждый продукт.
        if needle.lower() in item.lower():  # Игнорируем регистр.
            result.append(item)
    return result


def amount(items, needle):
    """
    Функция для подсчёта количества продуктов определенного названия.

    Args:
        items (dict): словарь, представляющий собой холодильник.
        needle (str): подстрока, которой должны соответствовать продукты.

    Returns:
        amount_of_products (Decimal): найденное количество соответствий.
    """
    amount_of_products = 0  # Переменная для подсчёта количества продуктов.

    # Здесь key - название продукта, по нему мы проходимся и смотрим
    # соответствие needle. В value мы находим именно количество продуктов и
    # добавляем в amount_of_products.
    for key, value in dict.items(items):
        if needle.lower() in key.lower():  # Игнорируем регистр.
            for product in value:
                amount_of_products += product['amount']
    return Decimal(amount_of_products)
