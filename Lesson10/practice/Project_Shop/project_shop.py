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


def show_items(items: list[dict]):
    for i, item in enumerate(items):
        print(f"{i} Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")


def add_item_to_inventory(items: list[dict]) -> None:
    """Добавляет товар в инвентарь"""
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    new_item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    items.append(new_item)

def remove_item_from_inventory(items: list[dict]) -> None:
    """Удаляет товар из инвентаря по названию с вводом данных внутри функции."""
    name = input("Введите название товара для удаления: ")
    for item in items:
        if item["name"].lower() == name.lower():
            items.remove(item)
            print(f"Товар '{name}' успешно удалён.")

def find_item_by_name(items: list[dict], name: str) -> dict | None:
    for item in items:
        if item["name"].lower() == name.lower():
            return item

    return None

def update_item_from_inventory(items: list[dict]) -> None:
     """Обновляет товар из инвентаря по названию с вводом данных внутри функции."""
     name = input("Введите название товара для корректировки: ")
     item = find_item_by_name(items, name)
     if item:
         print(f"Текущие данные: Цена = {item['price']}, Количество = {item['quantity']}")
         try:
             new_price = float(input("Введите новую цену (оставьте пустым, чтобы не менять): ") or item['price'])
             new_quantity = int(input("Введите новое количество (оставьте пустым, чтобы не менять): ") or item['quantity'])
             item['price'] = new_price
             item['quantity'] = new_quantity
             print(f"Товар '{name}' успешно обновлён.")
         except ValueError:
             print("Ошибка: Введены некорректные данные.")
     else:
        print(f"Товар '{name}' не найден.")

# def filter_price(number):
#     .......
#     return number < n

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
        name = input("Введите название товара для поиска: ")
        item = find_item_by_name(inventory, name)
        if item:
            print(f"Найден товар: Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")
        else:
            print(f"Товар '{name}' не найден.")
        input("Press Enter to continue")
    #
    # elif choice == "6":
    #
    # elif choice == "7":
    #
    elif choice == "8":
