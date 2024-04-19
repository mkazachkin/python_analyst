# Создайте функцию генератор чисел Фибоначчи


num = 10

def fibonacci():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

f = fibonacci()

for i in range(num):
    print(next(f))
    