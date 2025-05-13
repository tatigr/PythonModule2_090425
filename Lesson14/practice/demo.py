# file = open("data.txt", "r", encoding="UTF-8")  # API-OS
# with open("data.txt", "r", encoding="UTF-8") as file:
# for line in file:
#     print(line.rstrip(), end="\n")
# #    line.strip()  # убирает пробельные символы и слева, и справа. Пробельные символы: "", "\n", "\t"
# #    line.rstrip()  # убирает пробельные символы справа
# #    linelstrip()  # убирает пробельные символы и слева
#
# file.close()



file = open("out.txt", "x", encoding="UTF-8")



file.write("Hello world" + '\n')
file.write("My name" + '\n')
file.write(str(42))

file.close()


контекстный менеджер with open('my_file.txt', 'r') as file:
with open("out.txt", "x", encoding="UTF-8") as file:
    file.write("Hello world" + '\n')
    file.write("My name" + '\n')
    file.write(str(42))

