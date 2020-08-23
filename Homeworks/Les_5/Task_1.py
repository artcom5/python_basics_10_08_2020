"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

from pathlib import Path
# Назначить имя файла.
file_name = 'Task_1.txt'
# Путь к файлу.
file_path = Path(__file__).parent.joinpath(file_name)
# Создать файловый объект с режимом записи
file_object = open(file_path, 'w', encoding='UTF-8')

while True:
    str_0 = input('Введите данные: ')
    if str_0 == '':
        break
    file_object.write(str_0 + '\n')    # Произвести запись в файл с переносом строки.
file_object.close()    # Закрыть файл после заприси.