class Vehicle:
    """
    Класс, представляющий некоторое транспортное средство.
    """

    def __init__(self, color: str, speed: float, weight: float) -> None:
        """
        Инициализатор для объектов класса Vehicle.

        Args:
            color (str): цвет кузова;
            speed (float): максимальная скорость в км/ч;
            weight (float): масса в килограммах.
        """
        self.color = color
        self.speed = speed
        self.weight = weight

    def __str__(self) -> str:
        """
        Метод, возвращающий описание экземлпяра класса при передачу его в
        функцию print().

        Returnes:
            str: f-string с описанием характеристик транспортного средства.
        """
        return (
            f"Это транспортное средство имеет {self.color} цвет, развивает "
            f"скорость {self.speed} км/ч и весит {self.weight} кг!"
        )


class Car(Vehicle):
    """
    Класс, представляющий бибику.
    """

    def __init__(
        self, color: str, speed: float, weight: float, diesel: bool
    ) -> None:
        """
        Инициализатор для объектов класса Car.

        Args:
            color (str): цвет кузова;
            speed (float): максимальная скорость в км/ч;
            weight (float): масса в килограммах;
            diesel (bool): тип используемого топлива:
                False - бензин;
                True - дизель.
        """
        super().__init__(color, speed, weight)
        self.diesel = diesel

    def __str__(self) -> str:
        """
        Метод, возвращающий описание экземлпяра класса при передачу его в
        функцию print().

        Returnes:
            str: f-string с описанием характеристик бибики.
        """
        return (
            f"Эта бибика на {'дизеле' if self.diesel is True else 'бензине'} "
            f"покрашена в {self.color} и, имея массу в {self.weight} "
            f"килограмм, способна развивать скорость в {self.speed} км/ч!"
        )


class Motorbike(Vehicle):
    """
    Класс, представляющий мотоцикл.
    """
    def __init__(
        self, color: str, speed: float, weight: float, sport: bool
    ) -> None:
        """
        Инициализатор для объектов класса Motorbike.

        Args:
            color (str): цвет кузова;
            speed (float): максимальная скорость в км/ч;
            weight (float): масса в килограммах;
            sport (bool): тип мотоцикла:
                False - стоковый;
                True - спортивная комплектация.
        """
        super().__init__(color, speed, weight)
        self.sport = sport

    def __str__(self) -> str:
        """
        Метод, возвращающий описание экземлпяра класса при передачу его в
        функцию print().

        Returnes:
            str: f-string с описанием характеристик мотоцикла.
        """
        return (
            f"Этот {'стоковый' if self.sport is False else 'спортивный'} "
            f"мотоцикл, покрашенный в {self.color} цвет, может развить "
            f"скорость до {self.speed} км/ч с массой {self.weight}!"
        )


class Airplane(Vehicle):
    def __init__(
        self, color: str, speed: float, weight: float, passenger: bool
    ) -> None:
        """
        Инициализатор для объектов класса Airplane.

        Args:
            color (str): цвет кузова;
            speed (float): максимальная скорость в км/ч;
            weight (float): масса в килограммах;
            passenger (bool): тип самолёта:
                False - не пассажирский;
                True - пассажирский.
        """
        super().__init__(color, speed, weight)
        self.passenger = passenger

    def __str__(self) -> str:
        """
        Метод, возвращающий описание экземлпяра класса при передачу его в
        функцию print().

        Returnes:
            str: f-string с описанием характеристик самолёта.
        """
        return (
            f"Этот {self.color} самолётик "
            f"{'не ' if self.passenger is False else ''}является пассажирским"
            f", имеет массу в {self.weight} кг и может лететь со скоростью "
            f"{self.speed} км/ч!"
        )


my_vehicle = Vehicle('голубенький', 120, 2000)
my_car = Car('розовенький', 220, 3890, True)
my_motorbike = Motorbike('чёрный', 320, 5890, False)
my_airplane = Airplane('красненький', 110, 840, True)

print(my_vehicle)
print(my_car)
print(my_motorbike)
print(my_airplane)
