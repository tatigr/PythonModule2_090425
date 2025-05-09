# Напишите декоратор cache, который кэширует результаты выполнения декорируемой функции.
# Если функция вызывается с теми же аргументами, что и ранее,
# декоратор должен возвращать сохраненный результат, не выполняя функцию заново.



import time

def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        # Сортируем kwargs для стабильного ключа
        key = args, tuple(sorted(kwargs.items()))
        if key in _cache:
            print("Из кеша:", _cache)
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result

    return wrapper

@cache
def expensive_calculation(n):
    time.sleep(2)
    return n * n

print(expensive_calculation(5))      # Медленно (новый вызов)
print(expensive_calculation(5))      # Быстро (из кеша)
print(expensive_calculation(n=4))    # Медленно (новый вызов)
print(expensive_calculation(n=3))    # Медленно (новый вызов)
print(expensive_calculation(n=4))    # Быстро (из кеша)