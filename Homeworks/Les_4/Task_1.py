"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv    # Подключить список argv модуля sys.

# Объявить функцию my_func.
def my_func(work_hour, bet_hour, prem):
    """
    Функция расчёта заработной платы, где
    :param work_hour: выробатка в часах
    :param bet_hour: ставка в час
    :param prem: премия
    :return:
    """
    return (work_hour * bet_hour) + prem    # Вернуть результат

_, command, *args = argv    # Изменим список.

flag = True    # Флаг для проверки значений.
# Перебрать и проверить, полученные со списком аргументы.
for count, itm in enumerate(args):
    try:
        args[count] = float(itm)
    except ValueError:
        print('Ошибка ввода')
        flag = False
        break

if flag:     # Если True
    result = my_func(*args)    # Вызвать функцию передать аргументы.
    print(result)    # Вывести результат.