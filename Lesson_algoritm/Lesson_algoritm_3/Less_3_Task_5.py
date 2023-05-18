# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

num_1 = [random.randint(-100, 10) for i in range (20)]
print(num_1)

n_1 = 0
n_ind = 0

for i, n in enumerate(num_1):
    if n < 0:
        if n_1 == 0:
            n_1 = n
        if n > n_1:
            n_1 = n
            n_ind = i

print(f'Максимальный отрицательный элемент {n_1} его индекс = {n_ind}')