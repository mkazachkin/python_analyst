# Напишите функцию для транспонирования матрицы

def transpose(in_matrix: list) -> list:
    """
    Транспонирует матрицу
    :param in_matrix: список списков со значениями матрицы
    :return: список списков со значениями транспонированной матрицы
    """
    in_rows_count = len(in_matrix)
    in_cols_count = len(in_matrix[0])

    out_matrix = []
    for in_col in range(in_cols_count):
        out_row = []
        for in_row in range(in_rows_count):
            out_row.append(in_matrix[in_row][in_col])
        out_matrix.append(out_row)
    return out_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose(matrix))
