"""
Соберите из созданных на уроке и в рамках домашнего задания
функций пакет для работы с файлами.
"""
import os
import json
import csv
import pickle


def traverse_directory(directory: str) -> list[dict[str, str | int]]:
    """
    Создает словарь со списком файлов, каталогов и их размеров
    Аргументы:
        directory: str - начальный путь к каталогу
    """
    current_dir = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for file_name in filenames:
            full_path = os.path.join(dirpath, file_name)
            current_dir.append({
                'Path': full_path,
                'Type': 'File',
                'Size': os.path.getsize(full_path)})
        for dir_name in dirnames:
            dir_path = os.path.join(dirpath, dir_name)
            current_dir.append({
                'Path': dir_path,
                'Type': 'Directory',
                'Size': get_dir_size(dir_path)})
            for record in traverse_directory(dir_name):
                current_dir.append(record)
    return current_dir


def get_dir_size(path: str) -> int:
    """
    Возвращает размер файлов в каталоге, рекурсивно
    Аргументы:
        path: str - начальный путь к каталогу
    """
    size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file_name in filenames:
            full_path = os.path.join(dirpath, file_name)
            size += os.path.getsize(full_path)
        for dir_name in dirnames:
            dir_path = os.path.join(dirpath, dir_name)
            size += get_dir_size(dir_path)
    return size


def save_results_to_json(data: list[dict[str, str | int]], file_name: str) -> None:
    """
    Сохраняет данные, собираемые функцией traverse_directory в JSON файл
    Аргументы:
        data: list[dict[str, str | int]] - собранные данные
        file_name: str - путь к файлу JSON
    """
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_results_to_csv(data, file_name):
    """
    Сохраняет данные, собираемые функцией traverse_directory в CSV файл
    Аргументы:
        data: list[dict[str, str | int]] - собранные данные
        file_name: str - путь к файлу CSV
    """
    with open(file_name, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_results_to_pickle(data, output_file):
    """
    Сохраняет данные, собираемые функцией traverse_directory в Pickle файл
        Аргументы:
        data: list[dict[str, str | int]] - собранные данные
        file_name: str - путь к файлу Pickle
    """
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)
