try:
    num = int(input('Введите целое число от 1 до 1000000\n>>'))
except ValueError:
    print('Ошибка ввода')
    exit()

if num < 1 or num > 100_000:
    'Я не умею работать с такими числами'
else:
    flag = False
    i = num // 2
    while (i > 1) and not flag:
        if num % i == 0:
            flag = True
        i -= 1
    if flag:
        print(f'{num} не является простым')
    else:
        print(f'{num} является простым')
