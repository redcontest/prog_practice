class Employee:
    """
    Класс, представляющий простого штатного сотрудника.
    """

    def __init__(self, hours: int) -> None:
        """
        Инициализатор для объектов класса Employee.

        Args:
            hours (int): рабочие часы сотрудника.
        """
        self.hours = hours

    @property
    def salary(self) -> int:
        """
        Свойство для получения зарплаты сотрудника.

        Returnes:
            salary (int): зарплата сотрудника.
        """
        salary = self.hours * 100  # Стандартный коэффициент = 100.
        return salary


class Manager(Employee):
    """
    Класс, представляющий менеджера по продажам.
    """

    def __init__(self, hours: int, sales: int) -> None:
        """
        Инициализатор для объектов класса Manager.

        Args:
            hours (int): рабочие часы менеджера;
            sales (int): число продаж.
        """
        super().__init__(hours)
        self.sales = sales

    @property
    def salary(self) -> int:
        """
        Свойство для получения зарплаты менеджера.

        Returnes:
            salary (int): зарплата менеджера.
        """
        # Коэффициент для часов менеджера = 200, для продаж = 3000.
        salary = self.hours * 200 + self.sales * 3000
        return salary


class Developer(Employee):
    """
    Класс, представляющий разработчика.
    """

    def __init__(self, hours: int, contributions: int) -> None:
        """
        Инициализатор для объектов класса Developer.

        Args:
            hours (int): рабочие часы разработчика;
            contributions (int): количество активностей в рабочем репозитории.
        """
        super().__init__(hours)
        self.contributions = contributions

    @property
    def salary(self) -> int:
        """
        Свойство для получения зарплаты разработчика.

        Returnes:
            salary (int): зарплата разработчика.
        """
        # Коэффициент для часов разработчика = 400, для активностей = 2000.
        salary = self.hours * 400 + self.contributions * 2000
        return salary
