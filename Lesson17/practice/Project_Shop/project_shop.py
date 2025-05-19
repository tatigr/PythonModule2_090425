def add_item(inventory):
    """Добавляет новый товар в инвентарь."""
    name = input("Введите название товара: ").strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            print("Ошибка: Товар с таким названием уже существует.")
            return

    while True:
        try:
            price = float(input("Введите цену товара: "))
            if price <= 0:
                print("Ошибка: Цена должна быть положительным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите корректное число для цены.")

    while True:
        try:
            quantity = int(input("Введите количество товара: "))
            if quantity < 0:
                print("Ошибка: Количество не может быть отрицательным.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите целое число для количества.")

    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Товар '{name}' успешно добавлен.")


def remove_item(inventory):
    """Удаляет товар из инвентаря по названию."""
    name = input("Введите название товара для удаления: ").strip()
    for i, item in enumerate(inventory):
        if item['name'].lower() == name.lower():
            del inventory[i]
            print(f"Товар '{name}' успешно удален.")
            return
    print(f"Товар с названием '{name}' не найден.")


def update_item(inventory):
    """Обновляет информацию о товаре."""
    name = input("Введите название товара для обновления: ").strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            print("Что вы хотите обновить?")
            print("1. Цена")
            print("2. Количество")
            choice = input("Введите номер опции: ")
            if choice == '1':
                while True:
                    try:
                        price = float(input("Введите новую цену: "))
                        if price <= 0:
                            print("Ошибка: Цена должна быть положительной.")
                        else:
                            item['price'] = price
                            print("Цена обновлена.")
                            break
                    except ValueError:
                        print("Ошибка: Введите число.")
            elif choice == '2':
                while True:
                    try:
                        quantity = int(input("Введите новое количество: "))
                        if quantity < 0:
                            print("Ошибка: Количество не может быть отрицательным.")
                        else:
                            item['quantity'] = quantity
                            print("Количество обновлено.")
                            break
                    except ValueError:
                        print("Ошибка: Введите целое число.")
            return
    print("Товар не найден.")


def search_item(inventory):
    """Поиск товара по части названия."""
    query = input("Введите часть названия: ").strip().lower()
    found = [item for item in inventory if query in item['name'].lower()]
    if found:
        print("Найденные товары:")
        for item in found:
            print(f"{item['name']}: {item['price']} руб, {item['quantity']} шт")
    else:
        print("Совпадений не найдено.")


def display_inventory(inventory):
    """Выводит все товары."""
    if not inventory:
        print("Инвентарь пуст.")
        return
    for i, item in enumerate(inventory, 1):
        print(f"{i}. {item['name']}: {item['price']} руб, {item['quantity']} шт")


def display_below_price(inventory):
    """Товары дешевле заданной цены."""
    try:
        price_limit = float(input("Введите цену: "))
        filtered = [item for item in inventory if item['price'] < price_limit]
        if filtered:
            for item in filtered:
                print(f"{item['name']}: {item['price']} руб")
        else:
            print("Нет таких товаров.")
    except ValueError:
        print("Ошибка: Введите число.")


def display_below_quantity(inventory):
    """Товары с малым количеством."""
    try:
        quantity_limit = int(input("Введите количество: "))
        filtered = [item for item in inventory if item['quantity'] < quantity_limit]
        if filtered:
            for item in filtered:
                print(f"{item['name']}: {item['quantity']} шт")
        else:
            print("Нет таких товаров.")
    except ValueError:
        print("Ошибка: Введите целое число.")


def main():
    inventory = [
        {"name": "Ноутбук", "price": 1200, "quantity": 10},
        {"name": "Мышь", "price": 25, "quantity": 50},
        {"name": "Клавиатура", "price": 50, "quantity": 30},
    ]

    menu = {
        '1': display_inventory,
        '2': add_item,
        '3': remove_item,
        '4': update_item,
        '5': search_item,
        '6': display_below_price,
        '7': display_below_quantity,
    }

    while True:
        print("\nМеню:")
        print("1. Показать список товаров.")
        print("2. Добавить товар.")
        print("3. Удалить товар.")
        print("4. Обновить товар.")
        print("5. Найти товар по названию.")
        print("6. Товары дешевле заданной цены.")
        print("7. Товары с количеством ниже заданного.")
        print("8. Выход.")

        choice = input("Выберите пункт: ")
        if choice == '8':
            print("Выход из программы.")
            break
        elif choice in menu:
            menu[choice](inventory)
        else:
            print("Ошибка: неверный ввод.")


if __name__ == "__main__":
    main()
