# Напишите функцию группового переименования файлов. Она должна:
#   a. Принимать параметр желаемое конечное имя файлов. При переименовании
#   в конце имени добавляется порядковый номер.
#   b. Принимать параметр количество цифр в порядковом номере.
#   c. Принимать параметр расширение исходного файла. Переименование должно работать
#   только для этих файлов внутри каталога.
#   d. Принимать параметр расширение конечного файла.
#   e. Принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6]
#   берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное
#   имя, если оно передано. Далее счётчик файлов и расширение.
import argparse
from task02.filetools import rename_files

terminal_args = argparse.ArgumentParser()
terminal_args.add_argument(
    '--path',
    help='Путь к каталогу с файлами',
    type=str,
)
terminal_args.add_argument(
    '--se',
    help='Расширение файлов для переименования',
    type=str,
)
terminal_args.add_argument(
    '--tn',
    help='Целевое имя файлов',
    type=str,
)
terminal_args.add_argument(
    '--te',
    help='Целевое расширение файлов',
    type=str,
)
terminal_args.add_argument(
    '--dg',
    help='Количество цифр в счетчике',
    type=int,
)
args = terminal_args.parse_args()

rename_files(**{
    'path': args.path,
    'source_ext': args.se,
    'target_name': args.tn,
    'target_ext': args.te,
    'target_digits': args.dg
})
