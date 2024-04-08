num = int(input('Введите число: '))
ost = ''
test_res = f'Проверка результата: {hex(num)}'
while num > 0:
    ost_tmp = str(num % 16)
    ost = ost_tmp.replace('10', 'a').replace('11', 'b') \
        .replace('12', 'c').replace('13', 'd').replace('14', 'e') \
        .replace('15', 'f') + ost
    num = num // 16
print('Шестнадцатеричное представление числа:', '0x' + ost)
print(test_res)