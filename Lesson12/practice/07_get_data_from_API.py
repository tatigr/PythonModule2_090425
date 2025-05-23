import requests


# # Дан пример получения данных с сайта: jsonplaceholder.typicode.com
#
# url = 'https://jsonplaceholder.typicode.com/todos/2'
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()  # Преобразование ответа в JSON
#     print(data)
# else:
#     print(f'Ошибка: {response.status_code}')

# Дан пример получения данных с сайта: jsonplaceholder.typicode.com

url = 'https://jsonplaceholder.typicode.com/todoss/2'
response = requests.get(url)

if response.status_code == 200: # 200 - OK, 404 - Not found, 400 - Bad request, 500 - ...
    data = response.json()  # Преобразование ответа в JSON
    print(data)
else:
    print(f'Ошибка: {response.status_code}')

# Задание 1: Получение информации о пользователе.
# Напишите функцию, которая принимает идентификатор пользователя (например, число) и отправляет GET-запрос
# к API https://jsonplaceholder.typicode.com/users/{id} (где {id} — идентификатор пользователя).
# Функция должна возвращать словарь с информацией о пользователе в формате JSON, если запрос успешен (статус код 200),
# и выводить сообщение об ошибке в противном случае.

def get_user(user_id: int) -> dict | None:
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    # raise ValueError
    print("Пользователь не найден")



# Задание 2: Получение списка задач.
# Напишите функцию, которая отправляет GET-запрос к API https://jsonplaceholder.typicode.com/todos
# и возвращает список задач в формате JSON.
# Функция должна обрабатывать ошибки запроса и выводить соответствующие сообщения.

def get_to_do_list() -> list | None:
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)



# Задание 3: Получение комментариев к посту.
# Напишите функцию, которая принимает идентификатор поста и отправляет
# GET-запрос к API https://jsonplaceholder.typicode.com/posts/{id}/comments (где {id} — идентификатор поста).
# Функция должна возвращать список комментариев к посту в формате JSON.
#
# Задание 4: Получение информации о посте.
# Напишите функцию, которая принимает идентификатор поста и отправляет
# GET-запрос к API https://jsonplaceholder.typicode.com/posts/{id}.
# Функция должна возвращать словарь с информацией о посте в формате JSON, если запрос успешен,
# и выводить сообщение об ошибке в противном случае.

# Задание 5: Получение альбомов пользователя.
# Напишите функцию, которая принимает идентификатор пользователя и отправляет
# GET-запрос к API https://jsonplaceholder.typicode.com/users/{id}/albums.
# Функция должна возвращать список альбомов пользователя в формате JSON.