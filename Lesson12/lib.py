import random

def generate_number(at: int = -10, to: int = 10) -> float:
    return random.uniform(at, to)


def find_item_by_name(items: list[dict], name: str) -> dict | None:
    for item in items:
        if item["name"].lower() == name.lower():
            return item
    return None


def to_upper(strings):
    return list(map(string_to_upper, strings))

def count_vowels(text: str): #-> int:
    vowels = "ауоыэяюёие"
    num_vowels = 0
    for char in text.lower():
        if char in vowels:
            num_vowels += 1
    return num_vowels

if __name__ == "__main__":
    print(count_vowels("hello"))
    print(count_vowels("hi"))