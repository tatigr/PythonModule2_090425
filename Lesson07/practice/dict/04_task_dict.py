# Информация о товарах
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]

# 1. Выведите нумерованный список именований всех товаров
...
# 2. Выведите цену самого дешевого товара
...
items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]
# Вариант-1
# Выведите нумерованный список именований всех товаров
for i, item in enumerate(items, 1):
    print(i, item["name"])
# Выведите цену самого дешевого товара
min_price = float(items[0]["price"])
for item in items:
    if float(item["price"]) < min_price:
        min_price = float(item['price'])
print(f"Цена самого дешевого товара: {min_price} rub")


#item["price"]

# Вариант-2.
# Нумерованный список наименований
#print("Список товаров:")
#for i, item in enumerate(items, start=1):
#    print(f"{i}. {item['name']}")

# Цена самого дешевого товара
#min_price = min(float(item["price"]) for item in items)
#print(f"\nСамая низкая цена: {min_price}")