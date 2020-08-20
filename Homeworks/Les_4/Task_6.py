"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
# Подключить функции из модулей.
from sys import argv
from itertools import count
from itertools import cycle

# Объявить функцию
def my_count(start_0, end_0):
    """Функция итератор принимает два аргумента
    start_0 - начало
    end_0 - конец
    """
    for i in count(start_0):
        if i > end_0:
            break
        print(i)

def my_cycle(num):
    """Функция итератор принимает один параметр
        num - количество итераций
        """
    n = 1
    for itm in cycle('Купи слона '):
        if n > num:
            break
        print(itm, end='')
        n += 1


_, command, *args = argv

# Создать меню для запуска функций.
menu = {'my_count': my_count,
        'my_cycle': my_cycle}

flag = True

for idx, itm in enumerate(args):
    try:
        args[idx] = int(itm)
    except ValueError:
        print('Ошибка ввода')
        flag = False
        break

if flag:
    menu[command](*args)


