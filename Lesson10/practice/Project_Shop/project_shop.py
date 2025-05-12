def display_menu():
    """Отображает меню."""
    print("\nМеню:")
    print("1. Показать список товаров.")
    print("2. Добавить товар.")
    print("3. Удалить товар.")
    print("4. Обновить товар.")
    print("5. Найти товар по названию.")
    print("6. Вывести товары с ценой ниже заданной.")
    print("7. Вывести товары с количеством ниже заданного.")
    print("8. Выход. \n")

# 1. Показать список товаров
def show_items(items: list[dict]):
    for i, item in enumerate(items):
        print(f"{i + 1} Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")

# 2. Добавить товар
def add_item_to_inventory(items: list[dict]) -> None:
    """Добавляет товар в инвентарь"""
    name = input("Введите название товара: ")
    name = name.title()
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    new_item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    items.append(new_item)


# 3. Удалить товар
def remove_item_from_inventory(items: list[dict]) -> None:
    """Удаляет товар из инвентаря по названию с вводом данных внутри функции."""
    name = input("Введите название товара для удаления: ")
    for item in items:
        if item["name"].lower() == name.lower():
            items.remove(item)
            print(f"Товар '{name}' успешно удалён.")


# 4. Обновить товар
def update_item_from_inventory(items: list[dict]) -> None:
    """Обновляет товар из инвентаря по названию с вводом данных внутри функции."""
    name = str(input("Введите название товара для корректировки: "))
    for item in items:
        if item["name"].lower() == name.lower():
            print(f"Текущие данные: Цена = {item['price']}, Количество = {item['quantity']}")
            try:
                new_price = float(input("Введите новую цену или оставьте пустым, чтобы не менять: "))
                new_quantity = int(input("Введите новое количество или оставьте пустым, чтобы не менять: "))

                if new_price:
                    item['price'] = float(new_price)
                if new_quantity:
                    item['quantity'] = int(new_quantity)
                print(f"Товар '{name}' успешно обновлён.")
            except ValueError:
                print("Ошибка: Введены некорректные данные.")
            return
    print(f"Товар '{name}' не найден.")


# 5. Найти товар по названию
def find_item_by_name(items: list[dict]) -> dict | None:
    name = input("Введите название товара для поиска: ")
    for item in items:
        if item["name"].lower() == name.lower():
            print(f"Найден товар: Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
            return item
        print(f"Товар '{name}' не найден.")
        return None



# 6. Вывести товары с ценой ниже заданной
def filter_item_by_price(items: list[dict], price: float) -> dict | None:
    price = float(input("Введите цену товара для сортировки: "))
    for item in items:
        if item["price"] < price:
            print(f"Товары, стоимость которых меньше {price}: {inventory}")
            return item
        print(f"Товары, стоимость которых меньше '{price}' не найдены.")
        return None


# 7. Вывести товары с количеством ниже заданного
def filter_item_by_quantity(items: list[dict], quantity: int) -> dict | None:
    quantity = int(input("Введите количество товара для сортировки: "))
    for item in items:
        if item["quantity"] < quantity:
            print(f"Список товаров, количество которых меньше {quantity}: {inventory}")
            return item
        print(f"Товары, количество которых меньше {quantity}' не найдены.")
        return None



inventory = [
    {"name": "Ноутбук", "price": 1200, "quantity": 10},
    {"name": "Мышь", "price": 25, "quantity": 50},
    {"name": "Клавиатура", "price": 50, "quantity": 30},
]

# Menu
while True:
    display_menu()
    choice = input("Выберите действие: ")

    if choice == "1":
        show_items(inventory)
        input("Press Enter to continue")
    elif choice == "2":
        add_item_to_inventory(inventory)
        input("Press Enter to continue")
    elif choice == "3":
        remove_item_from_inventory(inventory)
        input("Press Enter to continue")
    elif choice == "4":
        update_item_from_inventory(inventory)
        input("Press Enter to continue")
    elif choice == "5":
        item = find_item_by_name(inventory)
        input("Press Enter to continue")

    elif choice == "6":
        item = filter_item_by_price(inventory)
        input("Press Enter to continue")

    elif choice == "7":
        item = filter_item_by_quantity(inventory)
        input("Press Enter to continue")

    elif choice == "8":
        print("Вы вышли из программы.")
        break
    else:
        print("Выберите корректный пункт меню.")

        input("Press Enter to continue")
