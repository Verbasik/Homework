import math

index = input('Вы используете 2-х мерное пространство (2) или 3-х мерное пространство(3)? ')
if index == '2':
    x_1 = int(input('Введите координату X начала вектора: '))
    y_1 = int(input('Введите координату Y начала вектора: '))
    x_2 = int(input('Введите координату X конца вектора: '))
    y_2 = int(input('Введите координату Y конца вектора: '))
    length = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    print(length)
else:
    x_1 = int(input('Введите координату X начала вектора: '))
    y_1 = int(input('Введите координату Y начала вектора: '))
    z_1 = int(input('Введите координату Z начала вектора: '))
    x_2 = int(input('Введите координату X конца вектора: '))
    y_2 = int(input('Введите координату Y конца вектора: '))
    z_2 = int(input('Введите координату Z конца вектора: '))
    length = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2 + (z_2 - z_1)**2)
    print(length)