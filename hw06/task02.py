# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
# число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def is_attacking(q1: tuple, q2: tuple):
    x1, y1 = map(int, q1)
    x2, y2 = map(int, q2)
    if (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2)):
        return True
    return False


def check_queens(queens: list):
    for i in range(len(queens)-1):
        for j in range(i+1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


print(check_queens(queens))
