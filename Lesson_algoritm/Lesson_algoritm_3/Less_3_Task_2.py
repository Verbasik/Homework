# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

num_1 = [random.randint(1,100) for i in range (10)]
print(num_1)

num_2 = []

for i, n in enumerate(num_1):
    num_2.append(i) if n % 2 == 0 else ''

print(num_2)