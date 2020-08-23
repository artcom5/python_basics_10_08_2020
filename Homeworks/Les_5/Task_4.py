"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from pathlib import Path

# Назначить имя файла.
file_name = 'Task_4.txt'
file_name_wr = 'Task_4new.txt'
# Путь к файлу.
file_path = Path(__file__).parent.joinpath(file_name)
file_path_wr = Path(__file__).parent.joinpath(file_name_wr)
# Создать файловый объект с режимом чтения
file_object = open(file_path, 'r', encoding='UTF-8')
# Создать файловый объект с режимом записи
file_object_wr = open(file_path_wr, 'w', encoding='UTF-8')
# Создать словарь числительных.
dict_num = {'One': 'Один', 'Two': 'Два', 'Three' : 'Три', 'Four': 'Четыре'}

for line in file_object:
    list_0 = line.split(' ')    # Строку в список.
    num = list_0[0]    # Первый элемент списка.
    list_0[0] = dict_num[num]      # Прочиать по ключу словарь и изм. элемент списка.
    file_object_wr.write(' '.join(list_0))    # Преобразовать в строку и записать в новый файл.

file_object.close()
file_object_wr.close()



