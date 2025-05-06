#def demo(a, b, c):
 # ...

#demo(2, 4, 7) #позиционные аргументы
#demo(b=4, a=7, c=9) #именованные аргументы
#demo(4, c=12, b=8) #смешанные: сначала обязательно позиционные

#def demo2(*args): #Только с позиционными(!) аргументами
  #  ...
#demo2()
#demo2(2)
#demo2(2, 4, 6)

#def demo3(*kwargs): # любое количество именнованных аргументов
   # ...
#demo3(a=12)
#demo3(hello=22, my=44, by=99)
#{"hello": 22, "my": 44, "by": 99}

#def demo4(*args, **kwargs):
  #  ...
#demo4(3, 4, 5, 6, а=12, b=99)

#def average(*args):
#    return sum(args) / len(args)

#result = average(2, 2, 6)
#print(result)

#result = average # получаем ссылку на об'ект функции
#print(result)

#print(average(3, 3, 3))
#print(result(3, 3, 3))

# ______________________________
#def meter_to_ft(dist):
 #   return dist * 3.28084

#distances_m = [1200, 1300, 1250, 1400]
#distances_m = []

#for dist in distances_m:
 #   dist_f = dist_m * 3.28084
  #  distances_f.append(dist_f)

#distances_f = list(map(meter_to_ft, distances_m))
#print(distances_f)

#__________________________________

def is_positive(number):
    return number > 0

numbers = [2, 5, -5, 6, 9, 12, 0, -8, 5, -6]
# Сумма положительных элементов

#sum_pos = 0
#for number in numbers:
#    if number > 0:
#        sum_pos += number

result = sum(filter(is_positive, numbers))
print(result)