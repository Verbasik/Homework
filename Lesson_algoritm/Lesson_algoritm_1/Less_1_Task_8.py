# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

n_1 = float(input('Введите первое число: '))
n_2 = float(input('Введите второе число: '))
n_3 = float(input('Введите третье число: '))
if n_2 < n_1 < n_3 or n_3 < n_1 < n_2:
    print(f'{n_1} является средним числом')
elif n_1 < n_2 < n_3 or n_3 < n_2 < n_1:
    print(f'{n_2} является средним числом')
else:
    print(f'{n_3} является средним числом')