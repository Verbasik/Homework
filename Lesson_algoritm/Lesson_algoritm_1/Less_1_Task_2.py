# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x_1 = int(input('Введите X1'))
y_1 = int(input('Введите Y1'))
x_2 = int(input('Введите X2'))
y_2 = int(input('Введите Y2'))
k = (y_1 - y_2) / (x_1 - x_2)
b = y_2 - (k * x_2)
print (f'y = {k}x + {b}')