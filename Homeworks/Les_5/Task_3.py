"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

from pathlib import Path

# Назначить имя файла.
file_name = 'Task_3.txt'

# Путь к файлу.
file_path = Path(__file__).parent.joinpath(file_name)

wages = 0    # Аккумулятор для з/п
count = 0    # Количество сотрудников.
# Создать файловый объект с режимом чтения.
with open(file_path, 'r', encoding='UTF-8') as file_object:
    print('Сотрудники, которые имеют оклад менее 20000.00 руб.')
    for line in file_object:
        str_0 = line.rstrip('\n').split(' ')
        wages += float(str_0[1])
        if float(str_0[1]) < 20000:
            print(line, end='')
        count += 1
print()
print(f'Cредняя зароботная плата сотрудников составляет {round((wages / count), 2)} руб.')