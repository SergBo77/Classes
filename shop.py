class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        if item_name in self.items:
             return self.items.get(item_name)
        else: return 'None'

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


store1 = Store('Магазин 1', 'ул. Цветная, 5')
store1.add_item('Яблоки', 0.5)
store1.add_item('Бананы', 0.75)
store1.add_item('Помидоры', 1.0)
store1.add_item('Огурцы', 0.8)

store2 = Store('Магазин 2', 'пр. Мельникова, 10')
store2.add_item('Яблоки', 0.5)
store2.add_item('Бананы', 0.75)
store2.add_item('Помидоры', 1.2)
store2.add_item('Огурцы', 1)

store3 = Store('Магазин 3', 'ул. Котельническая, 1/15')
store3.add_item('Говядина', 5.0)
store3.add_item('Свинина', 4.0)
store3.add_item('Помидоры', 1.0)
store3.add_item('Огурцы', 0.8)


# Тестирование методов
print(f" {store1.name}: {store1.items}")
print(f"Цена яблок в {store1.name}: {store1.get_price('Яблоки')}")

store1.update_price('Яблоки', 0.6)
print(f"Новая цена яблок в {store1.name}: {store1.get_price('Яблоки')}")

store1.delete_item('Бананы')
print(f"Магазин {store1.name} после удаления товара: {store1.items}")