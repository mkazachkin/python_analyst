import fractions

def get_nod(a: int, b:int)->int:
    """
    Возвращает наибольший общий делитель двух натуральных чисел.
    При расчете НОД используется алгоритм Евклида
    Аргументы:
        a:int   - первое натуральное число
        b:int   - второе натуральное число
    Возвращает:
        get_nod: int    - НОД
    """
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a or b

def simple_frac(a: str)->str:
    """
    Производит упрощение дробей вида 2/4 => 1/2.
    Аргументы:
        a: str  - дробь
    Возвращает:
        simple_frac: str   - упрощенная дробь
    """
    numerator, denominator = [int(num) for num in a.split('/')]
    nod = get_nod(numerator, denominator)
    numerator //= nod
    denominator //= nod
    return f'{numerator}/{denominator}'

def get_frac_sum(a: str, b:str)->str:
    """
    Возвращает сумму дробей вида '1/2'.
    Аргументы:
        a: str  - первая дробь
        b: str  - вторая дробь
    Возвращает:
        get_frac_sum: str   - сумма дробей
    """
    numerator_a, denominator_a = [int(num) for num in a.split('/')]
    numerator_b, denominator_b = [int(num) for num in b.split('/')]
    numerator_0 = numerator_a * denominator_b + numerator_b * denominator_a
    denominator_0 = denominator_a * denominator_b
    return simple_frac(f'{numerator_0}/{denominator_0}')

def get_frac_mult(a: str, b:str)->str:
    """
    Возвращает произведение дробей вида '1/2'.
    Аргументы:
        a: str  - первая дробь
        b: str  - вторая дробь
    Возвращает:
        get_frac_mult: str  - произведение дробей
    """   
    numerator_a, denominator_a = [int(num) for num in a.split('/')]
    numerator_b, denominator_b = [int(num) for num in b.split('/')]
    numerator_0 = numerator_a * numerator_b
    denominator_0 = denominator_a * denominator_b
    return simple_frac(f'{numerator_0}/{denominator_0}')


frac1 = input('Введите первую дробь: ')
frac2 = input('Введите вторую дробь: ')
a = fractions.Fraction(frac1)
b = fractions.Fraction(frac2)

print(f'Сумма дробей: {get_frac_sum(frac1, frac2)}')
print(f'Сумма дробей (проверка): {a + b}')
print(f'Произведение дробей: {get_frac_mult(frac1, frac2)}')
print(f'Произведение дробей (проверка): {a * b}')

