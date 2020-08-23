"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from pathlib import Path

# Назначить имя файла.
file_name_wr = 'Task_5.txt'
# Путь к файлу.
file_path_wr = Path(__file__).parent.joinpath(file_name_wr)
# Создать файловый объект с режимом запись.
with open(file_path_wr, 'w', encoding='UTF-8') as file_object_wr:

    str_0 = ''
    while True:
        element = input('Введите число или "*" для выхода : ')
        if element == '*':
            break
        try:
            # До тех пор пока пользователь не введет число.
            if float(element):
                str_0 += str(element) + ' '
        except ValueError:
            print('Ввод только цыфры!!!')    # Замучаем пользователя, пока не введет верно.
    file_object_wr.write(str_0[:-1])    # Записать в файл исключая последний пробельный символ

file_object = open(file_path_wr, 'r', encoding='UTF-8')

sum_num = 0     # переменная для результата
line = file_object.readline()
list_num = line.split(' ')

for count in list_num:
    sum_num += float(count)
print(f'Сумма чисел в файле {file_name_wr} равна {sum_num}')

file_object.close()