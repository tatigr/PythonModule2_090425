# Даны два словаря, представляющие продажи товаров в двух магазинах.
# Ключи — это названия товаров, а значения — количество проданных единиц.
# Напишите программу, которая объединяет эти данные в один словарь,
# суммируя количество проданных единиц для одинаковых товаров.

sales_store1 = {
    "яблоки": 100,
    "бананы": 150,
    "апельсины": 120,
    "молоко": 80
}

sales_store2 = {
    "яблоки": 130,
    "груши": 90,
    "апельсины": 110,
    "хлеб": 70
}

combined_sales = sales_store1.copy()
# Вариант-1
# Ключ - любой неизменяемый тип: tuple, str, int, float



# Вариант-2
# for product, quantity in sales_store2.items():
#    if product in combined_sales:
#        combined_sales[product] += quantity
#    else:
#        combined_sales[product] = quantity

#print(combined_sales)