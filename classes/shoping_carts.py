# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, buyer, manager):
        self.items = []
        self.buyer = buyer
        self.manager = manager

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name, user):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]


    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = f"Покупатель {self.buyer.username} приобрел:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общее: {self.get_total()} руб.\nПокупки зарегистрировал пользователь: {self.manager.username}"
        return details
