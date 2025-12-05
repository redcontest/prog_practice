import requests  # Чтобы делать запросы к PokeAPI
from typing import Literal  # Для аннотации типов


class Poketeam:
    def __init__(self):
        self.team = {}

    def get_pokemon_data(self, name: str) -> dict:
        """
        Функция для формирования словаря с данными о Покемоне.

        Args:
            name (str): имя или id Покемона.

        Returns:
            dict: {
                'weight': масса Покемона в гектограммах (int),
                'height': рост Покемона в дециметрах (int),
                'types': типы Покемона (list[str]),
                'abilities': его способности (list[str]),
                'hp': начальное здоровье (int),
                'attack': урон Покемона в бою (int).
            }
            ИЛИ пустой словарь, если обращение к api вызвало ошибку.
        """
        # Извлекает данные из pokeapi для нужного Покемона и обрабатывает
        # ошибки.
        try:
            response = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{name}/'
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Ошибка {e}")
            return {}
        data = response.json()

        # Следующий блок кода извлекает данные из json.
        weight = data['weight']
        height = data['height']
        types = [type['type']['name'] for type in data['types']]
        abilities = [
            ability['ability']['name'] for ability in data['abilities']
        ]
        hp = data['stats'][0]['base_stat']
        attack = data['stats'][1]['base_stat']

        # Возвращаем всё в удобном виде - в словаре.
        return {
            'weight': weight,
            'height': height,
            'types': types,
            'abilities': abilities,
            'hp': hp,
            'attack': attack,
        }

    def add_pokemon(self, name: str) -> None:
        """
        Функция для добавления Покемона с подробной о нём информацией в свою
        команду. Добавит Покемона только если http-запрос к API не закончился
        ошибкой и если Покемона ещё нет в команде.

        Args:
            name (str): имя покемона или его ID.
        """
        pokemon = self.get_pokemon_data(name)
        if pokemon and name not in self.team.keys():
            self.team[name] = pokemon

    def remove_pokemon(self, name: str) -> None:
        """
        Функция для удаления Покемона из своей команды. Ничего не сделает, если
        покемона в команде нет.

        Args:
            name (str): имя покемона или его ID.
        """
        if name in self.team.keys():
            del self.team['name']

    def teaminfo(self) -> None:
        '''В удобной форме выводит подробную информацию о команде'''
        print('Информация о команде:')
        print('---------------------\n')
        for key in self.team.keys():
            print(f'''Покемон {key}:
--------{'-' * len(key)}-
Вес - {self.team[key]['weight']} гектограмм
Рост - {self.team[key]['height']} дециметров
Типы - {', '.join(self.team[key]['types'])}
Способности - {', '.join(self.team[key]['abilities'])}
Здоровье - {self.team[key]['hp']} ед.
Атака - {self.team[key]['attack']} ед.\n''')

    def find(self, name: str) -> Literal[False] | dict:
        '''
        Функция для поиска Покемона в команде. Вернёт False, если Покемона нет
        в команде. Если покемон найден, вернёт его данные.

        Args:
            name (str): имя покемона или его ID.

        Returns:
            False | dict: данные о покемоне или False, если его нет в команде.
        '''
        if name in self.team.keys():
            return self.team[name]
        return False

    def training(self, pokemon1: str, pokemon2: str) -> None:
        '''
        Функция для проведения тренировочных боёв между Покемонами.
        Тренировочный бой здесь подразумевает одновременное нанесение ударов
        друг другу.

        Args:
            pokemon1 (str): имя или ID первого Покемона.
            pokemon2 (str): имя или ID второго Покемона.
        '''
        # Получаем данные первого и второго Покемона.
        pokemon1_data = self.get_pokemon_data(pokemon1)
        pokemon2_data = self.get_pokemon_data(pokemon2)

        # Осуществляем проверку, всех ли Покемонов удалось добавить в команду.
        bad_pokemon: list = []
        if not pokemon1_data:
            bad_pokemon.append(pokemon1)
        if not pokemon2_data:
            bad_pokemon.append(pokemon2)
            print(f'Кажется, покемона {', '.join(bad_pokemon)} нет в команде!')
            return

        # Извлекаем здоровье и урон первого Покемона.
        hp_1: int = pokemon1_data['hp']
        attack_1: int = pokemon1_data['attack']

        # Извлекаем здоровье и урон второго Покемона.
        hp_2: int = pokemon2_data['hp']
        attack_2: int = pokemon2_data['attack']

        # Реализуем самую простую логику боя - пусть Покемоны бьют друг друга
        # одновременно.
        while hp_1 > 0 and hp_2 > 0:
            hp_2 -= attack_1
            hp_1 -= attack_2

        if hp_1 <= 0:
            print(f'Победил Покемон {pokemon2}!')
        elif hp_2 <= 0:
            print(f'Победил Покемон {pokemon1}')
        else:
            print('Ничья!')


# Инициализируем новую команду.
my_team = Poketeam()

# Добавим 10 Покемонов в команду.
pokemons = ["pikachu", "charmander", "bulbasaur", "squirtle", "eevee",
            "jigglypuff", "meowth", "psyduck", "snorlax", "magikarp"]
for pokemon in pokemons:
    my_team.add_pokemon(pokemon)

# Выведем информацию об одном покемоне.
print(my_team.get_pokemon_data('meowth'))

# Выведем информацию о команде в целом.
my_team.teaminfo()

# Поищем одного реального Покемона из команды и одного Покемона (или не
# Покемона вовсе) не из команды.
print(my_team.find('pikachu'))
print(my_team.find('vladislav'))

# Заставим двух Покемонов из команды и двух Покемонов (или не Покемонов) не
# из команды провести тренировочный бой.
my_team.training('charmander', 'eevee')
my_team.training('vladislav', 'putin')
