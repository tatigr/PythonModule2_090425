import time

def get_time(origin_func):
    def wrapper(*args, **kwargs):
        before = time.time() # засекаем время до
        result = origin_func(*args, **kwargs)
        after = time.time() # засекаем время после
        print(f"Функция {origin_func.__name__}: {after-before}")
        return result
    return wrapper

@get_time

def demo():
    time.sleep(3)

demo()