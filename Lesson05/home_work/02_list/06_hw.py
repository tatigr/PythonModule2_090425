# Данные о товарах на складе хранятся в словаре
items = [
    {"name": "Кроссовки", "brand": "adidas", "price": 3440},
    {"name": "Кепка", "brand": "reebok", "price": 3500},
    {"name": "Рюкзак", "brand": "reebok", "price": 4800},
    {"name": "Шорты", "brand": "puma", "price": 2500},
    {"name": "Шорты", "brand": "adidas", "price": 2750},
    {"name": "Футболка", "brand": "puma", "price": 1700},
]
# 1. Напечатайте какими брендами представлены товары на складе:")

print("Товары на складе представлены брэндами:")
items_uniq = set()
for item in items:
    items_uniq.add(item["brand"])
for item in items_uniq:
    print(item)

# 2. Количество повторяющихся брендов:

frequency = {}
for item in items:
    brand = item["brand"]
    if brand in frequency:
        frequency[brand] += 1
    else:
        frequency[brand] = 1
print(f"Количество повторяющихся брендов: {frequency}")

# 3. Больше всего товаров на складе у брэнда(ов):

frequency = {}
for item in items:
    brand = item["brand"]
    if brand in frequency:
        frequency[brand] += 1
    else:
        frequency[brand] = 1
#print(f"Количество повторяющихся брендов: {frequency}")
max_value = max(frequency.values())
max_value_brand = [brand for brand, count in frequency.items() if count == max_value]
#print(len(frequency))
#print(len(max_value_brand))
#print(max_value_brand)
for brand in max_value_brand:
    print(f"На складе больше всего товаров брэнда(ов): {brand}")
if len(max_value_brand) > 1:
    print(f"На складе товаров всех брэнда(ов) одинаковое количество.")



# 4. На складе самый дорогой товар брэнда

most_expensive = max(items, key=lambda x: float(x["price"]))
print(f"На складе самый дорогой товар брэнда: {most_expensive['brand']} - {most_expensive['price']}")


