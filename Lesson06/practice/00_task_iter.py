text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
num_longest_words = 0
words = text.split()

for word in words:
    if len(word) > 5:
        num_longest_words += 1
print("Колличество слов больше 5 символов: ", num_longest_words)