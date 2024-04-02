from typing import Union


class Triangle:
    """
    Класс треугольников.
    """

    def __init__(self, a_side: Union[float, str, int], b_side: Union[float, str, int], c_side: Union[float, str, int]):
        """
        Создает треугольник, если такой треугольник существует.
        Аргументы:
            a - длина стороны треугольника
            b - длина стороны треугольника
            c - длина стороны треугольника
        """
        if not isinstance(a_side, float) or not isinstance(b_side, float) or not isinstance(c_side, float):
            try:
                a_side = float(a_side)
            except ValueError:
                raise ValueError('Значение стороны A указано неверно')
            try:
                b_side = float(b_side)
            except ValueError:
                raise ValueError('Значение стороны B указано неверно')
            try:
                c_side = float(c_side)
            except ValueError:
                raise ValueError('Значение стороны C указано неверно')
        self.a = a_side
        self.b = b_side
        self.c = c_side
        if not self.triangle_is_valid():
            raise ValueError('Треугольник с такими сторонами не существует')

    def triangle_is_valid(self) -> bool:
        """
        Проверяет существование треугольника,
        возвращает:
            triangle_is_valid: bool - истина, если треугольник с такими параметрами существует
        """
        return (self.a < (self.b + self.c)) and (self.b < (self.a + self.c)) and (self.c < (self.a + self.b))

    def triangle_is_isosceles(self) -> bool:
        """
        Проверяет, является ли треугольник равнобедренным
        Возвращает:
            triangle_is_isosceles: bool - истина, если треугольник равнобедренный
        """
        return self.a == self.b or self.a == self.c or self.b == self.c

    def triangle_is_equilateral(self) -> bool:
        """
        Проверяет, является ли треугольник равносторонним
        Возвращает:
            triangle_is_isosceles: bool - истина, если треугольник равнобедренный
        """
        return self.a == self.b == self.c

    def __str__(self) -> str:
        result = f'Треугольник со сторонами {self.a}, {self.b}, {self.c} '
        if self.triangle_is_equilateral():
            result += 'равносторонний'
        elif self.triangle_is_isosceles():
            result += 'равнобедренный'
        else:
            result += 'существует'
        return result


a = input('Введите сторону A\n>>')
b = input('Введите сторону B\n>>')
c = input('Введите сторону C\n>>')

try:
    print(Triangle(a, b, c))
except ValueError as e:
    print(e)
