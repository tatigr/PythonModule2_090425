# Вариант-1
def my_abs(number):
    if number > 0:
        return number
    else:
        return -number
# Вариант-2
#    def my_abs(x):
#    if x < 0:
#        x *= -1
#    return x
# Вариант-3

def my_abs(number):
    if number > 0:
        return number
    return -number

print(my_abs(-5))
print(my_abs(5))
print(my_abs(0))
print(my_abs(-5.45))
print(my_abs(5.45))



