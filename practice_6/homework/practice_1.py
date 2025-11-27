import requests


def get_list_of_pokemon(number: int) -> list | None:
    """
    Функция, возвращающая список нужного количества имён Покемонов.

    Args:
        number (int): количество Покемонов, имена которых нужно вернуть.

    Returns:
        pokemon_names (list): имена требующегося количества Покемонов.
    """
    # Попытка извлечь данные из api с обработкой ошибок.
    try:
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon?limit={number}"
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка {e}")
        return None
    data = response.json()
    pokemon_names = [pokemon['name'] for pokemon in data['results']]
    return pokemon_names


def get_pokemon_data(name: str) -> None:
    """
    Функция для удобочитаемого вывода информации о запрошенном Покемоне.
    Выводит имя, типы, вес, рост и способности.

    Args:
        name (str): имя Покемона.
    """
    # Извлекает данные из pokeapi для нужного Покемона и обрабатывает ошибки.
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка {e}")
        return
    data = response.json()

    # Следующий блок кода приводит данные к удобочитаемому виду.
    weight = data['weight']
    height = data['height']
    types_list = [type['type']['name'] for type in data['types']]
    types = ', '.join(types_list)
    abilities_list = [
        ability['ability']['name'] for ability in data['abilities']
    ]
    abilities = ', '.join(abilities_list)

    # Выводим подготовленные данные.
    print(f"""
Информация о покемоне {name.capitalize()}:
Имя - {name.capitalize()}
Типы - {types}
Вес - {weight} гектограмм
Рост - {height} дециметров
Способности: {abilities}
""")


# Тестируем для 20 Покемонов.
pokemon_list = get_list_of_pokemon(20)
print(pokemon_list)

# Тестируем get_pokemon_data().
pokemon_name = input('Введите имя покемона (например, clefairy): ')
get_pokemon_data(pokemon_name)
