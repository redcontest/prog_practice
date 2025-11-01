class Product:
    """
    Класс, описывающий некоторый товар
    """

    def __init__(
        self, name: str, price: float, in_stock: bool, category: str
    ) -> None:
        """
        Инициализатор класса Product.

        Args:
            name (str): название продукта;
            price (float): цена в рублях;
            in_stock (bool): наличие на складе:
                True - есть на складе;
                False - закончился.
            category (str): категория товара.
        """
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.category = category

    def __str__(self) -> str:
        """
        Магический метод для получения описания продукта.

        Returnes:
            (str): f-string с названием, ценой, категорией и информацией о
                наличии на складе продукта.
        """
        return (
            f"{self.name}: {self.price} рублей, {self.category}. "
            f"Наличие на складе: {self.in_stock}"
        )


class ShoppingCart:
    """
    Класс описывает список товаров. Созданный экземлпяр класса будет
    являться итератором.
    """

    def __init__(self, products: list[Product] = None) -> None:
        """
        Инициализатор класса ShoppingCart.

        Args:
            product (list[Products]): список объектов класса Product. По
                умолчанию не инициализирован, так как нет надобности создавать
                объект изначально с готовым списком. Элементы можно добавить
                позже.
        """
        # На случай, если список продуктов не инициализирован...
        if products is None:
            # ...инициализируем его сами.
            self.products = list()
        else:
            self.products = products
        self.index = 0  # Задаём начальный индекс для итерации.

    def add_product(self, new_product: Product) -> None:
        """
        Метод для добавления продуктов в список продуктов. Если продукта нет
        на складе, метод ничего не сделает.

        Args:
            new_product (Product): новый продукт, который хотим добавить.
        """
        if new_product.in_stock is True:
            self.products.append(new_product)

    def remove_product(self, product_to_delete: Product) -> None:
        """
        Метод для удаления продукта из списка продуктов.

        Args:
            product_to_delete (Product): конкретный товар, который нужно
                удалить.
        """
        self.products.remove(product_to_delete)

    def __iter__(self) -> None:
        """
        Магический метод для объявления объекта как итератора.
        """
        # Сбрасываем индекс, чтобы итерироваться можно было несколько раз:
        self.index = 0
        return self

    def __next__(self) -> None:
        """
        Магический метод для получения следующего товара из списка товаров.
        """
        if self.index < len(self.products):
            result = self.products[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __str__(self) -> str:
        """
        Магический метод для получения описания списка продуктов.

        Returnes:
            (str): f-string с описанием всех продуктов из списка.
        """
        info = ""
        for product in self.products:
            info += str(product) + '; '
        return info[:-2]


class Order:
    """
    Класс, задающий конкретный заказ. В отличие от списка продуктов (класс
    ShoppingCart), класс Order содержит информацию о итоговой стоимости
    всех товаров из списка - после налогов и со скидками.
    """

    def __init__(
            self, products: ShoppingCart, discount: float = 0, tax: float = 0
    ) -> None:
        """
        Инициализатор для класса Order

        Args:
            products (ShoppingCart): список товаров, предназначенных для
                заказа;
            discount (float): скидка в процентах.  По умолчанию равна 0.
            tax (float): налог в процентах. По умолчанию равен 0.
        """
        self.products = products
        self.discount = discount
        self.tax = tax

    @property
    def final_price(self) -> float:
        """
        Свойство заказа - возвращает итоговую стоимость всех товаров из списка
        с учётом скидок и налогов.

        Returnes:
            result_price (float): итоговая стоимость.
        """
        result_price = 0
        for product in self.products:
            result_price += product.price
        result_price -= result_price * (self.discount / 100)
        result_price += result_price * (self.tax / 100)
        return result_price

    def __str__(self) -> str:
        """
        Магический метод для получения описания заказа.

        Returnes:
            (str): f-string со списком продуктов и итоговой стоимостью всех
                продуктов.
        """
        return (
            f"Список продуктов: {str(self.products)}. Итоговая стоимость: "
            f"{self.final_price} рублей."
        )


class Customer:
    """
    Класс, описывающий покупателя.
    """

    def __init__(
        self, full_name: str, customer_id: int, orders: list[Order] = None
    ) -> None:
        """
        Инициализатор для класса Customer.

        Args:
            full_name (str): Фамилия, имя и отчество покупателя;
            customer_id (int): уникальный идентифиактор покупателя;
            orders (list[Order]): список заказов. По умолчанию отсутсвует,
                можно инициализировать вручную.
        """
        self.full_name = full_name
        self.customer_id = customer_id
        # Если список заказов не инициализирован...
        if orders is None:
            # ...инициализируем его самостоятельно.
            self.orders = list()
        else:
            self.orders = orders

    def add_order(self, new_order: Order):
        """
        Метод для добавления заказа в историю заказов покупателя.

        Args:
            new_order (Order): новый заказ, который хотим добавить.
        """
        self.orders.append(new_order)

    def delete_order(self, order_to_delete: Order):
        """
        Метод для удаления заказа из истории заказов покупателя.

        Args:
            order_to_delete (Order): заказ, который хотим удалить.
        """
        self.orders.remove(order_to_delete)

    def __str__(self) -> str:
        """
        Магический метод для получения описания покупателя.

        Returnes:
            str: f-string с ФИО, ID и историей заказов покупателя.
        """
        history = ''
        for order in self.orders:
            history += str(order) + '\n'
        return (
            f"ФИО покупателя: {self.full_name}, ID: {self.customer_id}.\n"
            f"История заказов:\n"
            f"{history}"
        )


apple = Product('яблоко', 150, True, 'Фрукты и овощи')
banana = Product('банан', 90, True, 'Фрукты и овощи')
bread = Product('хлеб', 50, True, 'Выпечка')
smak = Product('Булка смак забава с корицей', 49.9, False, 'Выпечка')
milk = Product('молоко', 20, True, 'Молочные продукты')
water = Product('вода', 70, True, 'Вода')

cart_1 = ShoppingCart([apple, banana, bread])
cart_1.add_product(milk)
cart_1.remove_product(apple)
cart_2 = ShoppingCart([apple, water])
cart_2.add_product(smak)

order_1 = Order(cart_1, discount=5, tax=20)
order_2 = Order(cart_2, discount=10, tax=22)
order_3 = Order(cart_1, discount=10, tax=20)

customer_1 = Customer('Иванов Иван Иванович', 12312, [order_1, order_2])
customer_2 = Customer('Петров Пётр Петрович', 45645)
customer_2.add_order(order_3)

print(customer_1)
print(customer_2)
