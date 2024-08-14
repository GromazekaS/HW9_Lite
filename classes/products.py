# 1. Базовый класс Product и производные классы для различных типов продуктов

class Product:
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Продукт: {self.name}, Цера: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб."


# 1. Добавить новый тип продуктов (например, бытовая химия).
class HouseholdChemicals(Product):
    """
    Класс, представляющий продукты бытовой химии, наследующий класс Product.
    """
    def __init__(self, name, price, brand, volume):
        super().__init__(name, price)
        self.brand = brand
        self.volume = volume

    def get_details(self):
        return f"Средство: {self.name}, Марка: {self.brand}, Объем: {self.volume}, Цена: {self.price} руб."
