# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция
# возвращает кортеж из трёх элементов: путь, имя файла, расширение файла

file_path = "C:/Users/User/Documents/example.txt"

import os

def get_file_info (file_path: str) -> tuple:
    file_name, file_extension = os.path.splitext(os.path.basename (file_path))
    dirname = file_path[:-(len(file_name) + len (file_extension))]
    return (dirname, file_name, file_extension)

print(get_file_info(file_path))
