# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами
import datetime
import os
import random


def rename_files(**kwargs) -> bool:
    """
    Функция пакетного переименования файлов
    Аргументы:
        source_ext: str - расширение файлов для переименования
        target_name: str - целевое имя файла
        target_ext: str - целевое расширение файла
        target_digits: int - количество цифр в счетчике
        path: str - путь к каталогу с файлами
    Возвращает:
        True в случае успеха, False, в случае ошибки
    """
    default_name = f'{datetime.datetime.today().date()}_'
    default_ext = ''
    default_digits = 3

    source_ext = '.' + kwargs.get('source_ext', default_ext)

    target_name = kwargs.get('target_name', default_name)
    target_ext = '.' + kwargs.get('target_ext', default_ext)
    target_digits = kwargs.get('target_digits', default_digits)

    path = kwargs.get('path')
    try:
        if source_ext == '.':
            file_list = [
                file_name for file_name in os.listdir(path)
            ]
        else:
            file_list = [
                file_name for file_name in os.listdir(path)
                if file_name.endswith(source_ext)
            ]
    except Exception as err:
        print(f'Возникла ошибка при сканировании каталога {err}')
        return False
    for i in range(len(file_list)):
        source_fullname = os.path.join(
            path,
            file_list[i]
        )
        target_fullname = os.path.join(
            path,
            target_name + str(i + 1).zfill(target_digits) + target_ext
        )
        try:
            os.rename(source_fullname, target_fullname)
        except Exception as err:
            print(f'При переименовании файлов возникла ошибка {err}')
            return False
        return True


def generate_number_file(count: int, full_path: str):
    """
    Заполняет файл случайными числами
    """
    min_num = -1000
    max_num = 1000
    with open(full_path, 'w', encoding='utf-8') as f:
        for i in range(count):
            f.write(f'{random.randint(min_num, max_num)}|{random.random() * 2000 - 1000}')
            f.write('\n' if i < count - 1 else "")


def generate_name_file(filename: str, count_name: int):
    """
    Генерация псевдоимен
    """
    max_len = 7
    min_len = 4
    min_letter = ord('a')
    max_letter = ord('z')
    vowels = {'a', 'o', 'y', 'i', 'u', 'e'}
    with open(filename, 'w', encoding='utf-8') as f:
        for j in range(count_name):
            len_name = random.randint(min_len, max_len)
            name = []
            for i in range(len_name):
                name.append(chr(random.randint(min_letter, max_letter)))
            has_vowels = False
            for letter in name:
                if letter in vowels:
                    has_vowels = True
                    break
            if not has_vowels:
                ind = random.randint(0, len_name - 1)
                letter = random.choice(list(vowels))
                name[ind] = letter
            print(f'{"".join(name).capitalize()}', file=f, end='')
            f.write('\n' if j < count_name - 1 else "")
