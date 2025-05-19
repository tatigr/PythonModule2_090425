# Дан готовый код
def add_prefix(text):
    return "prefix_" + text


items = ["one", "two", "three"]
prefixed_items = list(map(add_prefix, items))
print(prefixed_items)

# Задача: перепишите код, используя lambda-функцию
items = ["one", "two", "three"]
prefixed_items = list(map(lambda text: "prefix_" + text, items))
print(prefixed_items)