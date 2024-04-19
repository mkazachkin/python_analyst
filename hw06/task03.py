# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.


import random

from task02 import check_queens


def generate_boards() -> list:
    result = []
    for i in range(4):
        flag = False
        queens = []
        while not flag:
            for j in range(8):
                x = random.randrange(1, 9)
                y = random.randrange(1, 9)
                queens.append((x, y))
            if not check_queens(queens):
                flag = True
        result.append(queens)
    return str(result).replace('[', '').replace('], ', '\n').replace(']]', '')


print(f'Четыре успешные расстановки ферзей:\n{generate_boards()}')
