"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

from pathlib import Path

# Назначить имя файла.
file_name = 'Task_2.txt'
# Путь к файлу.
file_path = Path(__file__).parent.joinpath(file_name)
# Создать файловый объект с режимом чтения
file_object = open(file_path, 'r')

num = 0    # Переменная для посчёта строк.

for line in file_object:
    str_0 = line.split(' ')    # Преобразовать строку в список.
    num += 1
    print(f' В {num} строке {len(str_0)} слов(a).')
file_object.close()
