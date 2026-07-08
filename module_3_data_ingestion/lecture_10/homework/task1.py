class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print('Ошибка безопасности: Цена должна быть положительной!')

    def calculate_cost(self):
        return self.get_price()

    def get_display_info(self):
        return f'"Товар: {self.name} | Цена: {self.get_price()} руб."'


class WeighableProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def calculate_cost(self):
        return self.weight * self.get_price()

    def get_display_info(self):
        return f'Весовой товар: {self.name} | Вес: {self.weight} кг | Итого: {self.calculate_cost()} руб.'

class PackagedProduct(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def calculate_cost(self):
        return self.quantity * self.get_price()

    def get_display_info(self):
        return f'Упаковка: {self.name} | Количество: {self.quantity} шт. | Итого: {self.calculate_cost()} руб.'

cart = [
    Product('Молоко', 100),
    WeighableProduct('Яблоки', 50, 2.5),
    PackagedProduct('Яйца', 12, 10)
]

cart[0].set_price(-200)

total_sum = 0
for i in cart:
    print(i.get_display_info())
    total_sum += i.calculate_cost()
print(f'ИТОГО К ОПЛАТЕ: {total_sum}')
