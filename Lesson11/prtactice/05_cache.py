# Напишите декоратор cache, который кэширует результаты выполнения декорируемой функции.
# Если функция вызывается с теми же аргументами, что и ранее,
# декоратор должен возвращать сохраненный результат, не выполняя функцию заново.



import time

from tmp.demo_fileter import result


def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
<<<<<<< HEAD
        # Сортируем kwargs для стабильного ключа
        key = args, tuple(sorted(kwargs.items()))
        if key in _cache:
            print("Из кеша:", _cache)
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result

    return wrapper
=======
        key = args, tuple(sorted(kwargs.items()))
        if key in _cache:
            print(_cache)
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        print(_cache)
        return result

    return wrapper

>>>>>>> 040a54448726c63696683ea0a75a24518807d195

@cache
def expensive_calculation(n):
    time.sleep(2)
    return n * n

<<<<<<< HEAD
print(expensive_calculation(5))      # Медленно (новый вызов)
print(expensive_calculation(5))      # Быстро (из кеша)
print(expensive_calculation(n=4))    # Медленно (новый вызов)
print(expensive_calculation(n=3))    # Медленно (новый вызов)
print(expensive_calculation(n=4))    # Быстро (из кеша)
=======

print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(n=4, m=10))
print(expensive_calculation(n=3))
print(expensive_calculation(m=10, n=10))
# print(expensive_calculation(4))
>>>>>>> 040a54448726c63696683ea0a75a24518807d195
