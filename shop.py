from classes.products import Electronics, Clothing, HouseholdChemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
dishsoap = HouseholdChemicals(name="для мытья посуды", brand="Fairy", price=700, volume=5)

# Создаем пользователей
customer = Customer(username="Mikhail", email="python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(customer, admin)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(dishsoap, 1)

# Выводим детали корзины
print(cart.get_details())
print(laptop.get_details())